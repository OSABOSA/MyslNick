# console_client.py
import requests

API_URL = "http://localhost:8000/process"
API_KEY = "my-secret-key"  # Same as the server expects

def send_to_server(data: str):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    try:
        response = requests.post(API_URL, json={"data": data}, headers=headers)
        if response.status_code == 200:
            print("✅ Server response:", response.json()["result"])
        else:
            print("❌ Error:", response.status_code, response.text)
    except Exception as e:
        print("⚠️ Exception:", e)

def main():
    print("🖥️ Console Client (type 'exit' to quit)")
    while True:
        user_input = input("Enter data to send: ").strip()
        if user_input.lower() in {"exit", "quit"}:
            break
        send_to_server(user_input)

if __name__ == "__main__":
    main()
