from flask import Flask, request, jsonify, render_template
from openai import OpenAI

app = Flask(__name__)

# 🔐 Put your API key here
client = OpenAI(api_key="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")

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    
    messages = [
    {
        "role": "system",
        "content": """
You are a compassionate mental health support companion who not only listens but also gently helps the user feel better.

Your response structure MUST follow this:

1. 💛 Start with empathy
   - Acknowledge feelings
   - Make user feel heard and not alone

2. 🧠 Understand
   - Briefly reflect what they said
   - Ask a soft follow-up (optional)

3. 🌿 Give 2-3 simple remedies (VERY IMPORTANT)
   - Breathing exercises
   - Grounding techniques
   - Journaling prompts
   - Small actions (walk, music, hydration, talking to someone)

4. 🌈 End with encouragement
   - Reassure them things can improve
   - Keep tone warm and hopeful

Rules:
- Keep answers short (5–8 lines max)
- Be natural, not robotic
- Do NOT give medical advice
- Do NOT overwhelm with too many suggestions
- Remedies should feel easy and doable

Example tone:
"I'm really sorry you're feeling this way… that sounds heavy. You're not alone in this.

Maybe you can try something small right now:
• Take 5 slow deep breaths
• Step outside for fresh air
• Write down what’s on your mind

You don’t have to fix everything at once 💛"
"""
    },
    {"role": "user", "content": user_message}
]

    try:
        response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    temperature=0.7,
    max_tokens=120
)  
        

        reply = response.choices[0].message.content.strip()

    except Exception as e:
        reply = "I'm here with you… but I'm having trouble responding right now. Please try again 💛"

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)