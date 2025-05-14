import requests

BOT_TOKEN = "7906718715:AAF1_603YRHqNAVVyMLpFfBqHduJKc7c6p0"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"

response = requests.get(url)
print(response.json())
