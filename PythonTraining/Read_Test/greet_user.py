from pathlib import Path
import json

path = Path('username.json')
contents = path.read_text()
print(contents)
username = json.loads(contents)

print(f"Welcome back, {username}!")
 