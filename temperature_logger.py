import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
import random
import time
import requests

# === GOOGLE SHEETS SETUP ===
SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
CREDS_FILE = "credentials.json"

creds = ServiceAccountCredentials.from_json_keyfile_name(CREDS_FILE, SCOPE)
client = gspread.authorize(creds)

SPREADSHEET_NAME = "TemperatureLog"
sheet = client.open(SPREADSHEET_NAME).sheet1

# === TELEGRAM SETUP ===
TELEGRAM_BOT_TOKEN = "7906718715:AAF1_603YRHqNAVVyMLpFfBqHduJKc7c6p0"
TELEGRAM_CHAT_ID = "5068601753"
THRESHOLD = 30.0  # Celsius

# === RUN FOREVER UNTIL YOU STOP THE PROGRAM ===
reading_number = 1

while True:
    temperature = round(random.uniform(20, 40), 2)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Append to Google Sheets
    try:
        sheet.append_row([timestamp, temperature])
        print(f"[{reading_number}] Logged: {timestamp} - {temperature}°C")
    except Exception as e:
        print(f"❌ Error writing to Google Sheets: {e}")

    # Send Telegram alert if temp is high
    if temperature > THRESHOLD:
        alert_message = f"🚨 High Temperature Alert #{reading_number}: {temperature}°C at {timestamp}"
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        data = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": alert_message
        }
        try:
            response = requests.post(url, data=data)
            if response.status_code == 200:
                print("  🔔 Telegram alert sent!")
            else:
                print("  ❌ Telegram error:", response.text)
        except Exception as e:
            print("  ❌ Error sending Telegram alert:", e)

    reading_number += 1
    time.sleep(2)  # Adjust frequency here (2 seconds)
