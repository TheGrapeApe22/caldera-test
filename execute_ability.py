import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("CALDERA_URL")
RED_KEY = os.getenv("CALDERA_RED_KEY")

headers = {
    "KEY": RED_KEY,
    "Content-Type": "application/json"
}

# ----------------------------
# Get the first active agent
# ----------------------------
agents = requests.get(
    f"{BASE_URL}/api/v2/agents",
    headers=headers
)

agents.raise_for_status()

agents = agents.json()

if not agents:
    raise RuntimeError("No active agents found.")

paw = agents[0]["paw"]

print(f"Using agent: {paw}")

# ----------------------------
# Create a Link
# ----------------------------
ability_id = "8b160fd0-6323-412b-83b9-3a33e0f8fd1c"

payload = {
    "paw": paw,
    "ability_id": ability_id,
    "obfuscator": "plain-text"
}

response = requests.post(
    f"{BASE_URL}/plugin/access/exploit",
    headers=headers,
    json=payload
)


if response.status_code != 200:
    raise RuntimeError(f"Failed to create link: {response.text}")

print(response.status_code)
print(response.json())

def check(s):
    response = requests.get(
        f"{BASE_URL}{s}",
        headers=headers
    )
    return response.status_code

for endpoint in ["/api/v2/abilities", "/api/v2/agents", "/api/v2/results"]:
    print(f"Endpoint: {endpoint}, Status Code: {check(endpoint)}")