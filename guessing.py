import random

repeat = "y"
rounds = input("How many rounds do you want to play? ")
valid_rounds = False
while not valid_rounds:
    if rounds.isnumeric():
        rounds = int (rounds)
        if rounds>= 1:
            valid_rounds = True 
        else:
            rounds= input(f"invalid number entered. Number must be between 1 or more: ")   
    else: 
        rounds = input (f"it must be positve numbers only: ")

print(f"You have {rounds} rounds to play")
max = 4
win = lose = 0


for i in range(rounds):
    print(f"Round {i+1}")
    #generate a random number
    num = random.randint(1, max)
    valid = False
    guess= input(f"Guess a number between 1 and {max}: ")
    while not valid:
        if guess.isnumeric():
            guess = int (guess)
            if guess>= 1 and guess <= max: #check if number is in range
                valid = True 
            else:
                guess= input(f"invalid number entered. Number must be between 1 and {max}: ")   
        else: 
            guess = input (f"only numbers between 1 and {max} is allowed. Please enter a number: ")
    if guess == num:
        print("Yay!! you've guessed the right number!")
        win += 1
    else:
        print(f"Sorry wrong guess. The correct number was {num}")
        lose +=1

    # repeat = input("Do you want to try again? y/n: ")

print(f"You won {win} times and lost {lose} times")