from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import json

app = Flask(__name__)
CORS(app)  # Allow requests from React frontend

@app.route('/run-python', methods=['POST'])
def run_python_script():
    try:
        # Get user input from request body
        data = request.get_json()
        print(data)
        user_input = data.get("userInput", "")
        print(user_input)

        if not user_input:
            return jsonify({"error": "No input provided"}), 400

        # Run the Python script as a subprocess
        process = subprocess.Popen(
            ["python", "./src/Scripts/Rag.py", user_input],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        # Capture output and errors
        stdout, stderr = process.communicate()

        if stderr:
            print(f"Python Error: {stderr.decode()}")
            return jsonify({"error": "Python script error"}), 500

        # Parse and return JSON response
        result = json.loads(stdout.decode().strip())
        return jsonify({"result": result})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Server error"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000) 