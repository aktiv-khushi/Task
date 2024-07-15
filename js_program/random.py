import random

random_number = random.randint(1, 10)
user_guess = int(input("Enter your guess (between 1 and 10): "))

if user_guess == random_number:
    print("Good Work! Your guess is correct.")
else:
    print(f"Not matched. The correct number was {random_number}.")
