import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("CALDERA_URL")
RED_KEY = os.getenv("CALDERA_RED_KEY")
ABILITY_ID = "8b160fd0-6323-412b-83b9-3a33e0f8fd1c"

headers = {
    "KEY": RED_KEY,
    "Content-Type": "application/json"
}

def post(url, payload=None):
    response = requests.post(
        f"{BASE_URL}{url}",
        headers=headers,
        json=payload
    )
    return response.json()

def save_json(data, filename):
    with open(f'out/{filename}.json', 'w') as f:
        json.dump(data, f, indent=4)

a = post(
    '/api/v2/adversaries',
    {
        "adversary_id": "cheese_adversary_id",
        "name": "cheese adversary",
        "atomic_ordering": [ABILITY_ID]
    }
)

b = post(
    '/api/v2/operations',
    {
        "id": "cheese_operation_id",
        "name": "cheese operation",
        "adversary": {"adversary_id": "cheese_adversary_id"},
        "planner": {"id": "atomic"},
        "source": {"id": "basic"}
    }
)

c = post(
    '/api/v2/operations/cheese_operation_id/report', {"enable_agent_output": "true"}
)

save_json(a, 'a')
save_json(b, 'b')
save_json(c, 'c')