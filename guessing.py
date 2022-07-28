import random

repeat = "y"
max = 4
win = lose = 0

for i in range(5):
    #generate a random number
    num = random.randint(1, max)
    guess= int(input(f"Guess a number between 1 and {max}: "))
    if guess == num:
        print("Yay!! you've guessed the right number!")
        win += 1
    else:
        print(f"Sorry wrong guess. The correct number was {num}")
        lose +=1

    # repeat = input("Do you want to try again? y/n: ")

print(f"You won {win} times and lost {lose} times")