from flask import Flask, request
import requests
import os

app = Flask(__name__)

ID_INSTANCE = os.getenv("7107523876")
API_TOKEN = os.getenv("ab8b2d61db724012a48bbac216cab074f7303236b2aa48faa5")


def send_message(chat_id, text):
    url = f"https://api.green-api.com/waInstance{ID_INSTANCE}/sendMessage/{API_TOKEN}"

    payload = {
        "chatId": chat_id,
        "message": text
    }

    r = requests.post(url, json=payload)
    print("SEND:", r.text)


@app.route("/")
def home():
    return "Bot is running 🚀"


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("WEBHOOK:", data)

    try:
        if data.get("typeWebhook") != "incomingMessageReceived":
            return "ok"

        sender = data["senderData"]["chatId"]
        message = data["messageData"]["textMessageData"]["textMessage"].lower()

        if "привет" in message:
            send_message(sender, "👋 Привет! Production бот работает!")

        else:
            send_message(sender, "Напиши 'привет'")

    except Exception as e:
        print("ERROR:", e)

    return "ok"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)