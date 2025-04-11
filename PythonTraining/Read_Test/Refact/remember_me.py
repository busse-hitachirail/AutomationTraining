from pathlib import Path
import json

def get_stored_username(path):
        """Get stored username if available."""
        if path.exists():
                contents = path.read_text()
                username = json.loads(contents)
                return username
        else:
                return None
def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name? ")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We'll remember you when you come back, {username}!")

greet_user() # Show indentation error to the team


"""Summary 
you learned how to work with files. 
You learned to read the entire contents of a file, and 
then work through the contents one line at a time if you need to. 
You learned to write as much text as you want to a file. 
You also read about exceptions and how to handle the exceptions 
you’re likely to see in your programs. 
Finally, you learned how to store Python data structures 
so you can save information your users provide, 
preventing them from having to start over each time 
they run a program.
Absolute pathnames specify the exact location of a file in a 
filesystem without any ambiguity; they do this by 
listing the entire path to that file, starting from the 
root of the filesystem.
Relative pathnames specify the position of a file relative 
to some other point in the filesystem, 
and that other point isn’t specified in the relative pathname 
itself; instead, the absolute starting point for relative 
pathnames is provided by the context in which they’re used.
"""
