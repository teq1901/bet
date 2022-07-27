import random

repeat = "y"

win = 0

lose = 0

while repeat == "y":
    #generate a random number
    num = random.randint(1, 3)
    guess= int(input("Guess a number between 1 and 3: "))
    if guess == num:
        print("Yay!! you've guessed the right number!")
        win += 1
    else:
        print(f"Sorry wrong guess. The correct number was {num}")
        lose +=1

    repeat = input("Do you want to try again? y/n: ")

print(f"You won {win} times and lost {lose} times")