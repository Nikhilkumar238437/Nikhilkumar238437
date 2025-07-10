import requests

FLOW_URL = "https://your_webhook_url_from_power_automate"

def send_to_flow(command):
    payload = {"command": command}
    headers = {"Content-Type": "application/json"}
    response = requests.post(FLOW_URL, json=payload, headers=headers)
    print("📡 Sent to flow:", command, "| Status:", response.status_code)