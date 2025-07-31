from flask import Flask, request
import json
import requests

app = Flask(__name__)

TOKEN = 'JGCC0LAEQPJNLCEFQTRLRGYBCEJRNNMTYJKBAKZZDWRPJMLOBJPAYZKAPJDPPFPK'
URL = f"https://botapi.rubika.ir/v3/{TOKEN}/sendMessage"

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        data = request.json
        if data and "message" in data:
            user_id = data["message"]["user"]["user_guid"]
            if "text" in data["message"]:
                text = data["message"]["text"]
                if text == "/start":
                    send_buttons(user_id)
                elif text == "واسطه معتبر":
                    send_text(user_id)
        return "ok"
    return "YamurBot Running"

def send_buttons(user_id):
    payload = {
        "chat_id": user_id,
        "text": "لطفاً یکی از گزینه‌های زیر را انتخاب کنید 👇",
        "buttons": [[{"text": "واسطه معتبر"}]]
    }
    requests.post(URL, json=payload)

def send_text(user_id):
    payload = {
        "chat_id": user_id,
        "text": "✨ تنها واسطه معتبر در روبیکا ✨\n"
                "🔹 واسطه رسمی و مورد اعتماد یامور\n"
                "🔹 آیدی واسطه: @YamuR_Sa\n\n"
                "برای اطمینان کامل، فقط با این آیدی در ارتباط باشید!"
    }
    requests.post(URL, json=payload)
