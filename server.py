# server.py
import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv
import openai

load_dotenv()  # loads .env file if present

OPENAI_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_KEY:
    raise RuntimeError("Set OPENAI_API_KEY in environment or .env")

openai.api_key = OPENAI_KEY

app = Flask(__name__, static_folder='.')
CORS(app)

@app.route("/")
def index():
    return send_from_directory('.', 'index.html')

@app.route("/chat", methods=["POST"])
def chat():
    """
    Expect JSON { "message": "..." }
    Returns JSON {"reply": "..."}
    """
    data = request.get_json() or {}
    user_message = data.get("message", "").strip()
    if not user_message:
        return jsonify({"reply": "Please send a message."}), 400

    # Build messages for the model: we include a short system prompt to guide persona
    messages = [
        {"role": "system", "content": (
            "You are 'Her Government' — a helpful, empathetic assistant focused on women's rights, civic participation, "
            "and practical local resources. Keep answers concise, cite when you can, and suggest safe, actionable next steps."
        )},
        {"role": "user", "content": user_message}
    ]

    try:
        # Use ChatCompletion (adjust model to your available model)
        resp = openai.ChatCompletion.create(
            model="gpt-4o-mini",     # replace with a model you have access to
            messages=messages,
            max_tokens=400,
            temperature=0.6
        )
        reply = resp.choices[0].message.get("content", "").strip()
    except Exception as e:
        # for debugging, return safe error message
        reply = f"Sorry, the AI service returned an error: {str(e)}"

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
