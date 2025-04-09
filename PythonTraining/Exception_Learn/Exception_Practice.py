# Python uses special objects called exceptions to manage errors that arise during a program’s execution.
# Whenever an error occurs that makes Python unsure of what to do next, it creates an exception object.

#print(5/0) # Remove Code

# Try / Except Block
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")


# Handling errors correctly is especially important when the program has more work to do after the error occurs.
# This happens often in programs that prompt users for input.


print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

"""while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)"""

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)





