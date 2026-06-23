# ================================================================
# main.py — AI Resume Review Agent
# ================================================================
#
# HOW THIS FILE WORKS:
# 1. We load your secret API key from the .env file
# 2. We ask the user to paste their resume text
# 3. We send that resume to OpenAI GPT with a detailed prompt
# 4. GPT analyzes the resume and returns a structured review
# 5. We display the results in a clean, readable format
#
# ================================================================

# --- IMPORTS ---
# os: used to read environment variables (like our API key)
import os

# openai: the official OpenAI Python library to talk to GPT
from openai import OpenAI

# load_dotenv: reads the .env file and loads our API key into the environment
from dotenv import load_dotenv


# ================================================================
# STEP 1: Load the API Key from .env
# ================================================================

# This reads the .env file and makes OPENAI_API_KEY available via os.getenv()
load_dotenv()

# Fetch the API key from the environment
api_key = os.getenv("OPENAI_API_KEY")

# Safety check: if the key is missing or still placeholder, warn the user
if not api_key or api_key == "your_openai_api_key_here":
    print("❌ ERROR: OpenAI API key not found!")
    print("👉 Open the .env file and replace 'your_openai_api_key_here' with your real API key.")
    print("   Get your key at: https://platform.openai.com/api-keys")
    exit(1)  # Stop the program

# Create the OpenAI client using our API key
client = OpenAI(api_key=api_key)


# ================================================================
# STEP 2: Define the Resume Analysis Function
# ================================================================

def analyze_resume(resume_text: str) -> str:
    """
    Sends the resume text to OpenAI GPT for analysis.

    Parameters:
        resume_text (str): The full text of the user's resume

    Returns:
        str: The AI-generated review of the resume
    """

    # This is the "system prompt" — it tells GPT what role to play
    system_prompt = """
You are an expert career coach and professional resume reviewer with 15+ years of experience 
helping candidates land jobs at top companies. You provide honest, detailed, and constructive 
feedback in a beginner-friendly tone.

When given a resume, you MUST respond in exactly this format (use these exact headings):

📊 RESUME SCORE
Give a score out of 100 and a one-line summary of overall quality.

✅ STRENGTHS
List 3–5 strong points of the resume as bullet points. Be specific.

⚠️ WEAKNESSES
List 3–5 areas that need improvement as bullet points. Be specific.

💡 IMPROVEMENT SUGGESTIONS
Give 5 clear, actionable tips to make this resume stronger. Number them.

🎯 INTERVIEW QUESTIONS
Generate 5 likely interview questions based on this resume. Number them.

Keep your language clear and beginner-friendly. Avoid jargon. Be encouraging but honest.
"""

    # This is the "user message" — the actual resume we want analyzed
    user_message = f"""
Please review the following resume and provide a complete analysis:

--- RESUME START ---
{resume_text}
--- RESUME END ---
"""

    print("\n⏳ Analyzing your resume... Please wait.\n")

    # Send the request to OpenAI's GPT model
    response = client.chat.completions.create(
        model="gpt-4o-mini",       # Cost-effective and very capable model
        messages=[
            {"role": "system", "content": system_prompt},   # Sets GPT's behavior
            {"role": "user",   "content": user_message}     # The resume to analyze
        ],
        temperature=0.7,           # Controls creativity (0 = strict, 1 = creative)
        max_tokens=2000            # Maximum length of the response
    )

    # Extract just the text from the response object
    result = response.choices[0].message.content
    return result


# ================================================================
# STEP 3: Get Resume Input from the User
# ================================================================

def get_resume_input() -> str:
    """
    Prompts the user to paste their resume text.
    Accepts multi-line input until the user types 'DONE' on a new line.

    Returns:
        str: The resume text entered by the user
    """

    print("=" * 60)
    print("   📄 AI RESUME REVIEW AGENT")
    print("   Powered by OpenAI GPT")
    print("=" * 60)
    print()
    print("Paste your resume text below.")
    print("When you're done, type  DONE  on a new line and press Enter.")
    print("-" * 60)

    lines = []  # We'll collect each line here

    # Keep reading lines until the user types "DONE"
    while True:
        line = input()           # Read one line of input
        if line.strip().upper() == "DONE":
            break               # Stop collecting input
        lines.append(line)      # Add the line to our list

    # Join all lines into a single string with newlines between them
    resume_text = "\n".join(lines).strip()

    return resume_text


# ================================================================
# STEP 4: Display the Results Nicely
# ================================================================

def display_results(analysis: str) -> None:
    """
    Prints the analysis result in a clean, formatted way.

    Parameters:
        analysis (str): The AI-generated review text
    """

    print()
    print("=" * 60)
    print("   🤖 YOUR RESUME ANALYSIS RESULTS")
    print("=" * 60)
    print()
    print(analysis)
    print()
    print("=" * 60)
    print("✅ Analysis complete! Good luck with your job search! 🚀")
    print("=" * 60)


# ================================================================
# STEP 5: Main Program — Runs Everything Together
# ================================================================

def main():
    """
    The main entry point of the program.
    Orchestrates input → analysis → display.
    """

    # Ask user for their resume
    resume_text = get_resume_input()

    # Make sure they didn't submit an empty resume
    if not resume_text:
        print("❌ No resume text was entered. Please try again.")
        return

    # Check minimum length (a real resume should have some content)
    if len(resume_text) < 50:
        print("⚠️  The resume text seems too short. Please paste your full resume.")
        return

    # Send to OpenAI for analysis
    analysis = analyze_resume(resume_text)

    # Show the results
    display_results(analysis)

    # Ask if they want to analyze another resume
    print()
    another = input("Would you like to analyze another resume? (yes/no): ").strip().lower()
    if another in ("yes", "y"):
        main()  # Restart the program recursively


# ================================================================
# PROGRAM ENTRY POINT
# ================================================================

# This is standard Python: only run main() if this file is executed directly
# (not if it's imported as a module by another file)
if __name__ == "__main__":
    main()
