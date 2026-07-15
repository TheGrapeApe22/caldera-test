import os
import requests
from dotenv import load_dotenv

# Load variables from the .env file
load_dotenv()

# Grab the variables safely from the environment
BASE_URL = os.getenv("CALDERA_URL")
RED_KEY = os.getenv("CALDERA_RED_KEY")

# Construct the v2 API URL
AGENTS_ENDPOINT = f"{BASE_URL}/api/v2/agents"

# Define headers using the Red Team API Key
headers = {
    "KEY": RED_KEY,
    "Content-Type": "application/json"
}

try:
    # Use standard GET request (v2 standard)
    response = requests.get(AGENTS_ENDPOINT, headers=headers)
    
    if response.status_code == 200:
        agents = response.json()
        print(f"Successfully connected! Found {len(agents)} active agent(s):")
        for agent in agents:
            print(f"- PAW: {agent.get('paw')} | Host: {agent.get('host')} | OS: {agent.get('platform')}")
    else:
        print(f"Failed. Status Code: {response.status_code}")
        print(response.text)

except Exception as e:
    print(f"Error connecting to Caldera server: {e}")