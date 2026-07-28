import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("CALDERA_URL")
RED_KEY = os.getenv("CALDERA_RED_KEY")

def request(method: str, url: str, payload=None):
    response = requests.request(
        method,
        f"{BASE_URL}/api/v2/{url}",
        headers={
            "KEY": RED_KEY,
            "Content-Type": "application/json"
        },
        json=payload
    )
    try:
        return response.json()
    except json.JSONDecodeError:
        return response.text

def save_json(data, filename):
    with open(f'out/{filename}.json', 'w') as f:
        json.dump(data, f, indent=4)

