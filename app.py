# ================================================================
# app.py — Flask Web Server for AI Resume Review Agent
# ================================================================
#
# This file runs a local web server on your computer.
# When you run this file, you can open your browser and
# use the Resume Agent through a beautiful web interface.
#
# How it works:
# 1. Flask serves the HTML page when you visit localhost:5000
# 2. When you submit your resume, it sends it to this server
# 3. This server calls the OpenAI API and streams the response
# 4. The response appears word-by-word in your browser (like ChatGPT)
#
# ================================================================

import os
from flask import Flask, render_template, request, Response, stream_with_context
from openai import OpenAI
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()

# Create the Flask app
app = Flask(__name__)

# Create the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# ================================================================
# ROUTE 1: Home Page — serves the main HTML interface
# ================================================================

@app.route("/")
def index():
    """Serve the main web page."""
    return render_template("index.html")


# ================================================================
# ROUTE 2: Analyze — receives resume and streams AI response
# ================================================================

@app.route("/analyze", methods=["POST"])
def analyze():
    """
    Receives the resume text from the frontend,
    sends it to OpenAI, and streams the response back
    word-by-word (like ChatGPT typing effect).
    """

    # Get the resume text sent from the browser
    resume_text = request.json.get("resume", "").strip()

    # Validate: make sure resume isn't empty
    if not resume_text or len(resume_text) < 50:
        return {"error": "Please provide a complete resume (at least 50 characters)."}, 400

    # The system prompt — tells GPT how to behave
    system_prompt = """
You are an expert career coach and professional resume reviewer with 15+ years of experience 
helping candidates land jobs at top companies. You provide honest, detailed, and constructive 
feedback in a beginner-friendly tone.

When given a resume, you MUST respond in exactly this format (use these exact headings with emojis):

📊 RESUME SCORE
Give a score out of 100 and a one-line summary of overall quality.

✅ STRENGTHS
List 3–5 strong points of the resume as bullet points. Be specific.

⚠️ WEAKNESSES
List 3–5 areas that need improvement as bullet points. Be specific.

💡 IMPROVEMENT SUGGESTIONS
Give 5 clear, actionable tips to make this resume stronger. Number them 1-5.

🎯 INTERVIEW QUESTIONS
Generate 5 likely interview questions based on this resume. Number them 1-5.

Keep your language clear and beginner-friendly. Be encouraging but honest.
"""

    user_message = f"""
Please review the following resume and provide a complete analysis:

--- RESUME START ---
{resume_text}
--- RESUME END ---
"""

    def generate():
        """
        Generator function that streams OpenAI response chunks.
        Each chunk is sent to the browser as it arrives.
        """
        try:
            # Create a streaming request to OpenAI
            stream = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user",   "content": user_message}
                ],
                temperature=0.7,
                max_tokens=2000,
                stream=True   # ← This enables word-by-word streaming
            )

            # Send each word/chunk as it arrives from OpenAI
            for chunk in stream:
                content = chunk.choices[0].delta.content
                if content:
                    # SSE format: "data: <content>\n\n"
                    yield f"data: {content}\n\n"

            # Signal to frontend that streaming is done
            yield "data: [DONE]\n\n"

        except Exception as e:
            yield f"data: ❌ Error: {str(e)}\n\n"
            yield "data: [DONE]\n\n"

    # Return a streaming response with Server-Sent Events content type
    return Response(
        stream_with_context(generate()),
        mimetype="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no"
        }
    )


# ================================================================
# START THE SERVER
# ================================================================

if __name__ == "__main__":
    print("=" * 55)
    print("  🚀 AI Resume Review Agent - Web Version")
    print("=" * 55)
    print()
    print("  ✅ Server is starting...")
    print("  🌐 Open your browser and go to:")
    print()
    print("       http://localhost:5000")
    print()
    print("  Press CTRL+C to stop the server.")
    print("=" * 55)

    # debug=True shows errors in browser (good for development)
    app.run(debug=True, port=5000)
