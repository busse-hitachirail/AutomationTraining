# An enum (short for enumeration) is a special data type used to define a set of named constant values.
# Think of it like a list of related options with clear names—except
# you can’t accidentally change them, and they make your code more readable and reliable.

from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# Accessing enum members
print(Color.RED)          # Color.RED
print(Color.RED.name)     # 'RED'
print(Color.RED.value)    # 1

for color in Color:
    print(f"{color.name} = {color.value}")


if Color.RED == Color.RED:
    print("Same color!")

if Color.RED != Color.BLUE:
    print("Different colors!")


from enum import Enum

class Status(Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"

print(Status.APPROVED.value)  # 'approved'



