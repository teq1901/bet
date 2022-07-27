import random

repeat = "y"

while repeat == "y":
    #generate a random number
    num = random.randint(1, 3)
    guess= int(input("Guess a number between 1 and 3: "))
    if guess == num:
        print("Yay!! you've guessed the right number!")
    else:
        print(f"Sorry wrong guess. The correct number was {num}")

    repeat = input("Do you want to try again? y/n: ")