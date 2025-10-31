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
MIT License

Copyright (c) 2025 Iyonawan Adonri.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
<img width="959" height="562" alt="HerGoverment" src="https://github.com/user-attachments/assets/e30397ed-0e2e-446f-a0d6-ce7a0fb1d84d" />
<img width="959" height="562" alt="HerGoverment1" src="https://github.com/user-attachments/assets/3271cd37-37bd-4ff4-938a-677b98d93643" />
<img width="959" height="562" alt="HerGoverment2" src="https://github.com/user-attachments/assets/86da7e86-d472-4ce9-96e4-2bb333acb848" />


