# Her Government

An AI-powered chatbot designed to educate and assist users on women's rights, civic engagement, and local resources. The chatbot, Civi, provides clear, actionable guidance and educational information.

## Features

- Ask questions about local civic participation and women's rights.  
- Quick-reply buttons for common questions.  
- Responsive design for desktop and mobile devices.  
- Local conversation history saved in the browser.  
- Safe, empathetic, and informative responses tailored for civic engagement.  

## Project Structure

her-government-chatbot/  
├─ server.py               # Flask backend  
├─ requirements.txt        # Python dependencies  
├─ templates/  
│  └─ index.html           # Main HTML page  
├─ static/  
│  ├─ style.css            # CSS for styling  
│  └─ script.js            # JavaScript functionality  
├─ .env                    # Your OpenAI API key (ignored by Git)  
└─ README.md               # This file  

## Local Setup & Testing

Important: Do not commit your `.env` file to GitHub. It contains your private OpenAI API key.

1. Clone the repository:  
git clone https://github.com/FairyDust001/HerGoverment.git  
cd HerGoverment  

2. Create a virtual environment:  
python -m venv venv  

Activate the environment:  
macOS/Linux: `source venv/bin/activate`  
Windows: `venv\Scripts\activate`  

3. Install dependencies:  
pip install -r requirements.txt  

4. Create a `.env` file in the root folder:  
OPENAI_API_KEY=your_openai_api_key_here  

5. Run the Flask server:  
python server.py  

6. Open your browser and navigate to:  
http://127.0.0.1:5000  

7. Test the chatbot by typing a question or using the quick-reply buttons.  

## Notes for Reviewers

- HTML, CSS, and JS are included and visible for review.  
- The chatbot requires a valid OpenAI API key in the `.env` file.  
- Local conversation history is stored in browser `localStorage` (does not affect your system).  
- The `.gitignore` prevents sensitive files (`.env`) from being uploaded to GitHub.  

## License

MIT License. Feel free to use and modify for educational purposes.

