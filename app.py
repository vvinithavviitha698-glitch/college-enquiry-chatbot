from flask import Flask, render_template, request, jsonify
from chatbot import get_response
import os
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chat():
    user_msg = request.json["msg"]
    bot_reply = get_response(user_msg)
    return jsonify({"response": bot_reply})

if __name__ == "__main__":
    port=int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

