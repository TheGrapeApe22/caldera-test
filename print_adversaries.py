import os
import requests
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("CALDERA_URL")
RED_KEY = os.getenv("CALDERA_RED_KEY")

# Define headers using the Red Team API Key
headers = {
    "KEY": RED_KEY,
    "Content-Type": "application/json"
}

try:
    response = requests.get(f"{BASE_URL}/api/v2/agents", headers=headers)
    if response.status_code == 200:
        print(response.json()[:3])
    else:
        print(f"Failed. Status Code: {response.status_code}")
        print(response.text)

except Exception as e:
    print(f"Error connecting to Caldera server: {e}")