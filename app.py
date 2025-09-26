from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

# Configure your API key
API_KEY 
#enter api key to make the code to run . to get the api key go to the google ai studio website and get the apo key
genai.configure(api_key=API_KEY)

# Initialize Flask and CORS
app = Flask(__name__)
CORS(app) # This allows the frontend to communicate with the backend

# Initialize the chat model
model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

@app.route('/chat', methods=['POST'])
def handle_chat():
    """Handles chat requests from the frontend."""
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({"error": "No message provided"}), 400
    
    try:
        response = chat.send_message(user_message)
        return jsonify({"text": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
