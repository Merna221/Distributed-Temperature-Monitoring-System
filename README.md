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
Distributed-Temperature-Monitoring-System/
├── app.py # Flask app with API routes and WebSocket setup
├── sensor_client.py # Simulated sensor client script
├── temperature_logger.py # Google Sheets logger + Telegram alert system
├── templates/
│ └── index.html # Dashboard UI
├── static/
│ ├── script.js # Real-time frontend logic
│ └── alert.mp3 # Alert sound
├── temperature.db # SQLite database (auto-created)
├── credentials.json # Google Sheets API credentials
└── requirements.txt # Python dependencies
