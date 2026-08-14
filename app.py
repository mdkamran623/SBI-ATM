"""
SBI-style ATM backend — real Python server.
PIN check, balance, withdraw, mini-statement, change-pin all done server side.
Run: pip install flask flask-cors
     python atm_backend.py
Serves on http://127.0.0.1:5000
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
import uuid, time, random

app = Flask(__name__)
CORS(app)

MASTER_PIN = "1234"   # sab card ke liye same pin, jaisa maanga tha
CASH_TRAY = {500: 400, 200: 300, 100: 500}  # ATM cash tray inventory (notes available)

# in-memory "accounts" — one fresh account per card, keyed by session token
SESSIONS = {}

TXN_SEED = [
    {"desc": "UPI/Swiggy Order", "amt": -486},
    {"desc": "Salary Credit", "amt": 52000},
    {"desc": "ATM Withdrawal", "amt": -2000},
    {"desc": "Electricity Bill", "amt": -1240},
    {"desc": "UPI/Zomato", "amt": -355},
]


def new_account():
    return {
        "balance": 245678.50,
        "acc_last4": str(random.randint(1000, 9999)),
        "pin": MASTER_PIN,
        "attempts": 3,
        "txns": [dict(t, date=time.strftime("%d %b")) for t in TXN_SEED],
    }


@app.post("/api/insert-card")
def insert_card():
    """Card inserted -> backend creates a session, doesn't know PIN result yet."""
    token = str(uuid.uuid4())
    SESSIONS[token] = new_account()
    return jsonify({"token": token})


@app.post("/api/verify-pin")
def verify_pin():
    data = request.json or {}
    token, pin = data.get("token"), data.get("pin", "")
    acc = SESSIONS.get(token)
    if not acc:
        return jsonify({"ok": False, "error": "no_session"}), 400

    if acc["attempts"] <= 0:
        return jsonify({"ok": False, "retained": True})

    if pin == acc["pin"]:
        acc["attempts"] = 3
        return jsonify({"ok": True, "acc_last4": acc["acc_last4"]})

    acc["attempts"] -= 1
    retained = acc["attempts"] <= 0
    return jsonify({"ok": False, "attempts_left": acc["attempts"], "retained": retained})


@app.get("/api/balance")
def balance():
    token = request.args.get("token")
    acc = SESSIONS.get(token)
    if not acc:
        return jsonify({"error": "no_session"}), 400
    return jsonify({"balance": acc["balance"], "acc_last4": acc["acc_last4"]})


@app.post("/api/withdraw")
def withdraw():
    data = request.json or {}
    token, amount = data.get("token"), int(data.get("amount", 0))
    acc = SESSIONS.get(token)
    if not acc:
        return jsonify({"error": "no_session"}), 400
    if amount <= 0 or amount % 100 != 0:
        return jsonify({"error": "invalid_amount"}), 400
    if amount > acc["balance"]:
        return jsonify({"error": "insufficient_funds"}), 400

    # real cash-tray denomination logic — checks actual note stock
    remaining = amount
    dispense = {}
    for note in (500, 200, 100):
        if remaining <= 0:
            break
        can_give = min(remaining // note, CASH_TRAY[note])
        if can_give > 0:
            dispense[note] = can_give
            remaining -= can_give * note
    if remaining > 0:
        return jsonify({"error": "cash_tray_low"}), 409

    for note, count in dispense.items():
        CASH_TRAY[note] -= count
    acc["balance"] -= amount
    acc["txns"].insert(0, {"desc": "ATM Withdrawal", "amt": -amount, "date": time.strftime("%d %b")})

    return jsonify({"ok": True, "dispense": dispense, "balance": acc["balance"]})


@app.get("/api/mini-statement")
def mini_statement():
    token = request.args.get("token")
    acc = SESSIONS.get(token)
    if not acc:
        return jsonify({"error": "no_session"}), 400
    return jsonify({"txns": acc["txns"][:5]})


@app.post("/api/change-pin")
def change_pin():
    data = request.json or {}
    token, new_pin = data.get("token"), data.get("new_pin", "")
    acc = SESSIONS.get(token)
    if not acc:
        return jsonify({"error": "no_session"}), 400
    if len(new_pin) != 4 or not new_pin.isdigit():
        return jsonify({"error": "invalid_pin"}), 400
    acc["pin"] = new_pin
    return jsonify({"ok": True})


@app.post("/api/eject-card")
def eject_card():
    token = (request.json or {}).get("token")
    SESSIONS.pop(token, None)
    return jsonify({"ok": True})


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)