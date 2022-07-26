import random

#generate a random number
num = random.randint(1, 3)
guess= int(input("Guess the number: "))
if guess == num:
    print("Yay!! you've guessed the right number!")
else:
    print(f"Sorry wrong guess. The correct number was {num}")