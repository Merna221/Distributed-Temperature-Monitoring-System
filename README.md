# Distributed-Temperature-Monitoring-System
A real-time distributed temperature monitoring system using Flask, WebSockets, Google Sheets, and Telegram alerts. Simulated sensor clients send data to a central dashboard with logging, export, and threshold-based notifications.

A distributed real-time temperature monitoring system built using **Flask**, **WebSockets**, **SQLite**, and **Telegram** integration. The system simulates multiple sensor clients reporting data, logs the readings in a central database and Google Sheets, and issues alerts when critical temperature thresholds are exceeded.

---

## ⚙️ Key Features

- 📡 Real-time data updates using Flask-SocketIO
- 🧾 Sensor readings stored in a local SQLite database
- 📊 Web dashboard with live readings, export to CSV, and threshold alerts
- 🔁 Simulated sensor clients sending temperature data every 3 seconds
- 📤 Data logging to **Google Sheets**
- 🚨 Telegram notifications for high-temperature alerts

---

## 📁 Project Structure

```

Distributed-Temperature-Monitoring-System/
├── app.py                 # Flask app with API routes and WebSocket setup
├── sensor\_client.py       # Simulated sensor client script
├── temperature\_logger.py  # Google Sheets logger + Telegram alert system
├── templates/
│   └── index.html         # Dashboard UI
├── static/
│   ├── script.js          # Real-time frontend logic
│   └── alert.mp3          # Alert sound
├── temperature.db         # SQLite database (auto-created)
├── credentials.json       # Google Sheets API credentials
└── requirements.txt       # Python dependencies

````

---

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Distributed-Temperature-Monitoring-System.git
cd Distributed-Temperature-Monitoring-System
````

### 2. Install Dependencies

Make sure Python 3 is installed, then:

```bash
pip install -r requirements.txt
```

> You'll also need a Google Cloud service account and a `credentials.json` file with access to a Google Sheet named `TemperatureLog`.

### 3. Start the Flask Server

```bash
python app.py
```

Flask will run on `http://127.0.0.1:5000`.

### 4. Run a Sensor Client

```bash
python sensor_client.py Sensor1
```

Run this in separate terminals for multiple sensors (e.g., Sensor2, Sensor3...).

### 5. Start the Logger (Google Sheets + Telegram Alerts)

```bash
python temperature_logger.py
```

---

## 🖥️ Web Dashboard

* View at: `http://127.0.0.1:5000/`
* Live current temperature
* Set alert threshold
* Real-time update table
* Export readings as CSV

---

## 🧪 API Endpoints

| Endpoint       | Method | Description                      |
| -------------- | ------ | -------------------------------- |
| `/add`         | POST   | Receive sensor readings          |
| `/history`     | GET    | Fetch recent temperature logs    |
| `/sensor/<id>` | GET    | Get all readings from one sensor |
| `/export`      | GET    | Download full dataset as CSV     |

---

## 🔒 Environment Requirements

* Python 3.8+
* Google Cloud account (for Sheets API)
* Telegram Bot Token & Chat ID

---

## 📜 License

MIT License

---

## 👥 Authors

* Merna Hesham
* Merna Ahmed
* Ali Hazim

---

````

---

### 📦 Files to Include

1. `app.py`
2. `sensor_client.py`
3. `temperature_logger.py`
4. `templates/index.html`
5. `static/script.js`
6. `static/alert.mp3`
7. `credentials.json` (add to `.gitignore` or don't upload publicly)
8. `requirements.txt` — you can generate this by running:

```bash
pip freeze > requirements.txt
````

Example contents:

```text
Flask
flask-socketio
requests
eventlet
gspread
oauth2client
```

---

### ✅ Setup Steps for GitHub

1. Create a new repo: `Distributed-Temperature-Monitoring-System`
2. Add a short description: *Real-time Flask-based temperature monitoring system with sensor simulation and Telegram alerts.*
3. Upload all your project files.
4. Add the `README.md` and `.gitignore` (optional).
5. Push and publish your repository.

