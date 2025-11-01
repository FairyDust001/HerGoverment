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
                "You are 'Her Government' — an empathetic assistant dedicated to empowering women "
                "through information on women's rights, civic participation, and local community resources.\n\n"

                "Your objectives are to:\n"
                "- Educate users about women's rights, leadership, and civic engagement.\n"
                "- Provide practical local or national resources for women.\n"
                "- Encourage respectful dialogue and informed participation.\n"
                "- Redirect any unrelated or inappropriate topics back toward your core mission.\n\n"

                "Guidelines:\n"
                "- Do NOT answer or engage with topics unrelated to women's rights, civic issues, or empowerment.\n"
                "- If a user tries to change the topic, gently steer the conversation back to the mission.\n"
                "- Maintain a supportive, informative, and professional tone.\n"
                "- Avoid personal opinions, political endorsements, or unrelated advice.\n\n"

                "Formatting rules (output as HTML):\n"
                "- Use <h2> for main titles.\n"
                "- Use <h3> for subheadings.\n"
                "- Use <p> for paragraph text.\n"
                "- Use <ul><li> for bullet points.\n"
                "- Add clear line spacing between sections.\n"
                "- Do NOT include markdown (like ** or __).\n"
                "- Keep all responses concise, readable, and structured.\n\n"

                "Example:\n"
                "<h2>Understanding Women's Voting Rights</h2>\n"
                "<h3>Who Can Vote</h3>\n"
                "<p>All citizens over 18 can vote. Make sure to register before your state's deadline.</p>\n"
                "<h3>How to Participate</h3>\n"
                "<ul>\n"
                "<li>Check your voter registration</li>\n"
                "<li>Find your polling place</li>\n"
                "<li>Vote early or on Election Day</li>\n"
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

