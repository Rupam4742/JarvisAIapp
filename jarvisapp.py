from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Replace with your actual OpenAI API key
openai.api_key = "your-openai-api-key-here"

@app.route('/')
def home():
    return "Jarvis API is running!"

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    message = data.get('message', '')

    if not message:
        return jsonify({"error": "No message provided"}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or gpt-4 if available
            messages=[{"role": "user", "content": message}]
        )
        reply = response['choices'][0]['message']['content'].strip()
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
