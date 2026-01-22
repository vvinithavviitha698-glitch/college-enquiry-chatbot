from flask import Flask, render_template, request, jsonify
from data import college_info
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"].lower()

    for key in college_info:
        if key in user_message:
            return jsonify({"reply": college_info[key]})

    return jsonify({"reply": "Sorry, I don't understand your question."})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
