<p align="center">
  <img src="https://img.shields.io/badge/State_Bank_of_India-0077B5?style=for-the-badge&logo=bank&logoColor=white" alt="SBI"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask"/>
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5"/>
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge" alt="Status"/>
</p>

<h1 align="center">🏦 SBI-ATM Simulator</h1>

<p align="center">
  <strong>A realistic, full-stack ATM kiosk simulation built with Flask and HTML — <br/>inspired by the State Bank of India's user experience.</strong>
</p>

<p align="center">
  <a href="#live-demo">🌐 Live Demo</a> •
  <a href="#features">✨ Features</a> •
  <a href="#tech-stack">⚙️ Tech Stack</a> •
  <a href="#installation">🚀 Installation</a> •
  <a href="#api-endpoints">📡 API Endpoints</a>
</p>

<br/>

---

## 🌟 Live Demo

> **🚧 Coming Soon!** The live demo is currently in development and will be deployed shortly. Stay tuned!

<p align="center">
  <a href="#" style="background: #0077B5; color: white; padding: 14px 40px; border-radius: 50px; text-decoration: none; font-weight: 600; font-size: 18px; display: inline-block; box-shadow: 0 4px 15px rgba(0,119,181,0.4);">
    ▶ Launch SBI ATM Simulator
  </a>
</p>

---

## 📖 Overview

The **SBI-ATM Simulator** is a full-stack web application that replicates the core functionality of a real ATM kiosk. Built with a **Flask** backend and a sleek, responsive **HTML/CSS** frontend, this project demonstrates:

- **Secure PIN-based authentication**
- **Real-time balance inquiry**
- **Cash withdrawal with dynamic denomination dispensing**
- **Mini-statement generation**
- **PIN change functionality**
- **Session-based card management**

Whether you're a developer exploring full-stack integration, a student learning Flask, or just someone who wants to experience an ATM interface — this project offers a realistic and interactive simulation.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 💳 **Card Insertion** | Simulate card insertion to start a session |
| 🔐 **PIN Verification** | Secure 4-digit PIN check with attempt tracking |
| 💰 **Balance Inquiry** | View account balance with last 4 digits of account |
| 🏧 **Cash Withdrawal** | Withdraw amounts in multiples of 100 with denomination breakdown (₹500, ₹200, ₹100) |
| 🧾 **Mini Statement** | View the last 5 transactions (UPI, salary, bills, withdrawals) |
| 🔄 **Change PIN** | Securely change your 4-digit ATM PIN |
| 🚪 **Card Ejection** | End session and eject card |
| 📱 **Responsive UI** | Optimized for both desktop and mobile screens |
| ⚡ **Real-time Feedback** | Instant responses with appropriate error handling |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Frontend** | HTML5, CSS3, JavaScript (Vanilla) |
| **Backend** | Python 3.x, Flask |
| **CORS** | Flask-CORS |
| **Server** | Flask built-in server (development) |
| **Deployment** | Render / PythonAnywhere (coming soon) |

---

## 🚀 Installation

Follow these steps to run the SBI-ATM Simulator locally:

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Step 1: Clone the Repository

```bash
git clone https://github.com/mdkamran623/SBI-ATM.git
cd SBI-ATM
Step 2: Install Dependencies
bash
pip install flask flask-cors
Step 3: Start the Backend Server
bash
python atm_backend.py
The server will start at http://127.0.0.1:5000 🚀

Step 4: Open the Frontend
Open atm-realistic.html in your browser — or serve it with any static server.

💡 Tip: For the best experience, use Live Server in VS Code or serve with python -m http.server.

🎮 Usage Guide
Insert Card — Click the TAP CARD area on the ATM screen.

Enter PIN — Use the on-screen keypad to enter the default PIN: 1234.

Choose an Operation:

Balance Inquiry — Check your current balance.

Cash Withdrawal — Enter an amount (multiples of ₹100).

Mini Statement — View recent transactions.

Change PIN — Set a new 4-digit PIN.

Eject Card — End your session.

📡 API Endpoints
The backend exposes a clean RESTful API for all ATM operations.

Method	Endpoint	Description
POST	/api/insert-card	Creates a new session token
POST	/api/verify-pin	Verifies the 4-digit PIN
GET	/api/balance	Returns current balance & account info
POST	/api/withdraw	Processes withdrawal with denomination logic
GET	/api/mini-statement	Returns last 5 transactions
POST	/api/change-pin	Updates the PIN for the session
POST	/api/eject-card	Terminates the session
🗂️ Project Structure
text
SBI-ATM/
├── atm-realistic.html       # Frontend ATM kiosk UI
├── atm_backend.py           # Flask backend server
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
🤝 Contributing
Contributions, issues, and feature requests are welcome!
Feel free to check the issues page or submit a pull request.

Fork the repository

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

📄 License
This project is licensed under the MIT License — see the LICENSE file for details.

👨‍💻 Created By
<p align="center"> <strong style="font-size: 20px; color: #0077B5;">MD KAMRAN</strong> <br/> <a href="https://github.com/mdkamran623">GitHub</a> • <a href="https://linkedin.com/in/mdkamran">LinkedIn</a> • <a href="https://twitter.com/mdkamran">Twitter</a> </p><p align="center"> <img src="https://img.shields.io/badge/Made_with_❤️_by_MD_KAMRAN-0077B5?style=for-the-badge&logo=github&logoColor=white" alt="Made with love"/> </p>
<p align="center"> <sub>Built with passion — because every transaction matters. 💳</sub> </p> ```
