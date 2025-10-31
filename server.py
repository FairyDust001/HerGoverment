# server.py
import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from dotenv import load_dotenv
import openai

# Load .env
load_dotenv()
OPENAI_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_KEY:
    raise RuntimeError("Set OPENAI_API_KEY in environment or .env")

openai.api_key = OPENAI_KEY

app = Flask(__name__)
CORS(app)

# Serve homepage
@app.route("/")
def index():
    return render_template("index.html")

# Chat API
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json() or {}
    user_message = data.get("message", "").strip()
    if not user_message:
        return jsonify({"reply": "Please send a message."}), 400

    messages = [
        {
            "role": "system",
            "content": (
            "You are 'Her Government' — a helpful, empathetic assistant focused on women's rights, "
            "civic participation, and practical local resources. \n\n"
            "When replying, format the answer as HTML with clear spacing:\n"
            "- Use <h2> for main titles.\n"
            "- Use <h3> for subheadings.\n"
            "- Use <p> for paragraph text.\n"
            "- Use <ul><li> for bullet points.\n"
            "- Add line spacing between sections so each block is visually distinct.\n"
            "- Do not include markdown like ** or __.\n"
            "- Keep content concise, readable, and professional.\n\n"
            "Example:\n"
            "<h2>Voting Rights Overview</h2>\n"
            "<h3>Who Can Vote</h3>\n"
            "<p>Citizens over 18 can vote. Register online or at local offices.</p>\n"
            "<h3>How to Participate</h3>\n"
            "<ul>\n"
            "<li>Check registration</li>\n"
            "<li>Find polling place</li>\n"
            "<li>Vote safely</li>\n"
            "</ul>\n"
            )
        },
        {"role": "user", "content": user_message}
    ]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=400,
            temperature=0.6
        )
        reply = response.choices[0].message.get("content", "").strip()
    except Exception as e:
        reply = f"Sorry, the AI service returned an error: {str(e)}"

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
