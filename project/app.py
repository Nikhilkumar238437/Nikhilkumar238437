from flask import Flask, request, jsonify
import webbrowser
app = Flask(__name__)

@app.route('/voice', methods=['POST'])
def receive_voice():
    data = request.get_json()
    command = data.get("command", "").lower()
    print("🎙️ Received Command:", command)

    if "sales" in command:
        dashboard_url = "https://app.powerbi.com/links/YOUR-DASHBOARD-LINK"
        webbrowser.open(dashboard_url)
        return jsonify({"response": "Opening sales dashboard"})

    elif "region" in command:
        return jsonify({"response": "Filtering by region"})

    else:
        return jsonify({"response": "Unknown command"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
