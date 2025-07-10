from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/voice', methods=['POST'])
def receive_voice():
    data = request.get_json()
    command = data.get("command", "").lower()
    print("🎙️ Received Command:", command)

    # Example logic
    if "sales" in command:
        return jsonify({"response": "Showing total sales"})
    elif "region" in command:
        return jsonify({"response": "Filtering by region"})
    else:
        return jsonify({"response": "Unknown command"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
