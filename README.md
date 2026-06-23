# 📄 AI Resume Review Agent

An intelligent Python-based AI agent that analyzes your resume and provides:
- 📊 A **resume score** out of 100
- ✅ Your **strengths**
- ⚠️ Your **weaknesses**
- 💡 **Improvement suggestions**
- 🎯 Likely **interview questions**

Powered by **OpenAI GPT** and built with beginner-friendly Python code.

---

## 📁 Project Structure

```
Resume ai agent/
│
├── main.py           → The main Python program (all the AI logic)
├── requirements.txt  → List of Python packages to install
├── .env              → Your secret API key (never share this!)
└── README.md         → This guide
```

---

## 🔧 Setup Instructions (Step by Step)

### Step 1: Make sure Python is installed

Open your terminal and type:
```bash
python --version
```
You should see something like `Python 3.9.0` or higher.
If not, download Python from [python.org](https://www.python.org/downloads/).

---

### Step 2: Install the required packages

In your terminal, navigate to the project folder and run:
```bash
pip install -r requirements.txt
```

This installs:
- `openai` — lets Python talk to ChatGPT
- `python-dotenv` — loads your API key from the `.env` file

---

### Step 3: Get your OpenAI API Key

1. Go to [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. Sign in or create a free account
3. Click **"Create new secret key"**
4. Copy the key (it starts with `sk-...`)

> ⚠️ **Important**: You'll need some API credits. OpenAI gives new accounts free credits to start.

---

### Step 4: Add your API key to the `.env` file

Open the `.env` file and replace the placeholder:

```
# Before (placeholder):
OPENAI_API_KEY=your_openai_api_key_here

# After (your real key):
OPENAI_API_KEY=sk-abc123yourrealkeyhere
```

> 🔒 **Never share your `.env` file** or upload it to GitHub. It contains your private key!

---

### Step 5: Run the program

```bash
python main.py
```

---

## 🖥️ How to Use

1. Run `python main.py`
2. **Paste your resume text** into the terminal
3. Type `DONE` on a new line and press **Enter**
4. Wait a few seconds for GPT to analyze it
5. Read your personalized review! ✨

### Example Session:

```
============================================================
   📄 AI RESUME REVIEW AGENT
   Powered by OpenAI GPT
============================================================

Paste your resume text below.
When you're done, type  DONE  on a new line and press Enter.
------------------------------------------------------------
John Doe
Software Engineer
Skills: Python, JavaScript, React...
[paste your full resume here]
DONE

⏳ Analyzing your resume... Please wait.

============================================================
   🤖 YOUR RESUME ANALYSIS RESULTS
============================================================

📊 RESUME SCORE
Score: 74/100 — Good foundation, but needs stronger impact statements.

✅ STRENGTHS
• Clear contact information and professional formatting
• Relevant technical skills listed...

[full analysis continues...]
```

---

## 📦 File Explanations

### `main.py`
The heart of the project. Contains 4 functions:
| Function | What it does |
|---|---|
| `get_resume_input()` | Collects multi-line resume text from the user |
| `analyze_resume()` | Sends the resume to OpenAI GPT and gets the review |
| `display_results()` | Prints the review in a clean format |
| `main()` | Runs everything in order |

### `requirements.txt`
Lists the external Python packages needed. Run `pip install -r requirements.txt` to install them all at once.

### `.env`
Stores your **secret API key**. The program reads it automatically using `python-dotenv`. Never hardcode your key directly in Python files!

### `README.md`
This file — a guide to understand and use the project.

---

## 🛠️ Troubleshooting

| Problem | Solution |
|---|---|
| `❌ ERROR: OpenAI API key not found!` | Open `.env` and paste your real API key |
| `ModuleNotFoundError: No module named 'openai'` | Run `pip install -r requirements.txt` |
| `AuthenticationError` | Your API key is invalid — get a new one from OpenAI |
| `RateLimitError` | You've exceeded your API quota — check your OpenAI billing |
| Program exits immediately | Make sure you're running `python main.py` in the correct folder |

---

## 💡 Tips for Best Results

- **Paste your complete resume** — the more detail, the better the analysis
- **Include everything**: experience, education, skills, projects, achievements
- **Run it multiple times** — each analysis may highlight different things

---

## 🚀 Possible Enhancements (Ideas for Later)

- [ ] Read resume from a `.txt` or `.pdf` file instead of typing
- [ ] Save the analysis results to a file
- [ ] Add a job description input for tailored feedback
- [ ] Build a web interface with Flask or Streamlit
- [ ] Support multiple languages

---

## 📜 License

This project is open-source and free to use for learning purposes.

---

*Built with ❤️ using Python and OpenAI GPT*
