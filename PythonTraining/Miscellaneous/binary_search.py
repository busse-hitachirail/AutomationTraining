def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Avoids potential overflow

        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Target not found


# Taking user input for sorted list within 1 to 100
while True:
    try:
        arr = list(map(int, input("Enter sorted numbers from 1 to 100 (space-separated): ").split()))

        # Check if all numbers are within range and sorted
        if all(1 <= num <= 100 for num in arr) and arr == sorted(arr):
            break
        else:
            print("Invalid input! Please enter sorted numbers within the range 1 to 100 in ascending order.")
    except ValueError:
        print("Invalid input! Please enter numbers only.")

# Choose difficulty level
while True:
    difficulty = input("Choose difficulty level (Easy/Medium/Hard): ").strip().lower()
    if difficulty == "easy":
        attempts = 7
        break
    elif difficulty == "medium":
        attempts = 5
        break
    elif difficulty == "hard":
        attempts = 3
        break
    else:
        print("Invalid choice! Please choose Easy, Medium, or Hard.")

# Randomly pick a number from the list for the user to guess
import random

correct_number = random.choice(arr)

left, right = 0, len(arr) - 1  # Binary search boundaries

while attempts > 0:
    try:
        target = int(input(f"You have {attempts} attempts left. Guess a number between {arr[left]} and {arr[right]}: "))

        if 1 <= target <= 100:
            result = binary_search(arr, target)
            if result != -1:
                print(f"🎉 Congratulations! {target} is in the list at index {result}. You won! 🎯")
                break
            else:
                print(f"❌ {target} is not in the list.")

                # Adjust hints using binary search logic
                if target < correct_number:
                    print("🔼 Try a higher number!")
                else:
                    print("🔽 Try a lower number!")

                attempts -= 1
        else:
            print("Invalid guess! Enter a number between 1 and 100.")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

# Reveal the correct number if the user runs out of attempts
if attempts == 0:
    print(f"😢 You've used all your attempts. The correct number was {correct_number}. Better luck next time!")
