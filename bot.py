

# curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=GEMINI_API_KEY" \
# -H 'Content-Type: application/json' \
# -X POST \
# -d '{
#   "contents": [{
#     "parts":[{"text": "Explain how AI works"}]
#     }]
#    }'

#    AIzaSyAb3w5X9Ma0sK5fLbsEoY0wjLfTnydpAv0




from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

API_KEY = "AIzaSyAb3w5X9Ma0sK5fLbsEoY0wjLfTnydpAv0"
URL_API = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

def gemini(prompt):
    data = {
        "contents": [{
        "parts":[{"text": prompt}]
    }]
    }

    yc = requests.post(URL_API, json=data, headers = {"Content-Type": "application/json"})
    if yc.ok:
        try:
            return yc.json()["candidates"][0]["content"]["parts"][0]["text"]
        except Exception as e:
            return " YC err"
        else:
            return f"err API"
        
@app.route("/", methods = ["GET", "POST"])
def chat():
    if request.method == "POST":
        prompt = request.form.get("message", "Cân bằng phương trình trên")
        if not prompt:
            return jsonify({"response": "vlntn"})
        return jsonify({"response": gemini(prompt)})
    return render_template("chatbot.html")

if __name__ == "__main__":
    app.run(debug=True)