from caldera_helper import request, save_json, BASE_URL

commands = request('GET', 'deploy_commands')

# find Sandcat windows
agent = next((c for c in commands['abilities'] if c['name'] == 'Sandcat' and c['platform'] == 'windows'), None)
command = agent['command']

command = (
    command
    .replace("#{app.contact.http}", BASE_URL)
    .replace("#{agents.architecture}", "amd64")
    .replace("#{agents.implant_name}", "cheese_sandcat_agent")
)

print(command)