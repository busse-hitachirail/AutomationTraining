from pathlib import Path
import json
# Why did I not use Try/Catch here?
path = Path('username.json')
if path.exists(): # Look at Exists
    contents = path.read_text()
    username = json.loads(contents)
    print(f"Welcome back, {username}!")
else:
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"We'll remember you when you come back, {username}!")

