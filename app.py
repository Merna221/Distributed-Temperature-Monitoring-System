# app.py
from flask import Flask, render_template, request, jsonify, Response
from flask_socketio import SocketIO
import sqlite3
import datetime
import eventlet

eventlet.monkey_patch()

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')

DB_NAME = 'temperature.db'

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS temperature (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        timestamp TEXT,
                        sensor_id TEXT,
                        value REAL)''')
        conn.commit()

def insert_temperature(sensor_id, value):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute("INSERT INTO temperature (timestamp, sensor_id, value) VALUES (?, ?, ?)", (timestamp, sensor_id, value))
        conn.commit()
    socketio.emit('update_temperature', {'sensor_id': sensor_id, 'value': value})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/history', methods=['GET'])
def history():
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute("SELECT timestamp, sensor_id, value FROM temperature ORDER BY id DESC LIMIT 20")
        data = c.fetchall()
    return jsonify(data)

@app.route('/sensor/<sensor_id>', methods=['GET'])
def get_sensor_data(sensor_id):
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute("SELECT timestamp, sensor_id, value FROM temperature WHERE sensor_id=? ORDER BY id DESC", (sensor_id,))
        data = c.fetchall()
    return jsonify(data)

@app.route('/add', methods=['POST'])
def add_reading():
    data = request.json
    sensor_id = data.get('sensor_id')
    value = data.get('value')
    if not sensor_id or value is None:
        return jsonify({'error': 'Invalid data'}), 400
    insert_temperature(sensor_id, float(value))
    return jsonify({'status': 'success'})

@app.route('/export', methods=['GET'])
def export_csv():
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute("SELECT timestamp, sensor_id, value FROM temperature")
        rows = c.fetchall()
    csv = 'Timestamp,Sensor ID,Temperature\n' + '\n'.join([','.join(map(str, row)) for row in rows])
    return Response(csv, mimetype="text/csv", headers={"Content-Disposition": "attachment;filename=temperature_data.csv"})

if __name__ == '__main__':
    init_db()
    print("🌐 Flask REST API running at http://localhost:5000")
    socketio.run(app, host='0.0.0.0', port=5000)

