# This requires Python 3.11 or newer
message = ""

try:
    # Raising a group of exceptions
    raise ExceptionGroup("Multiple exceptions", [
        TypeError("Type issue"),
        FileNotFoundError("File missing"),
        ValueError("Invalid value")
    ])
except* TypeError:
    message += "Handling TypeError\n"
except* IOError:  # FileNotFoundError is a subclass of IOError
    message += "Handling IOError\n"
except* ValueError:
    message += "Handling ValueError\n"
finally:
    print(message)
