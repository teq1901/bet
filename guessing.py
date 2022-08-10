import random

repeat = "y"
rounds = int(input("How many rounds do you want to play? "))
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
            if int(guess)>= 1 and int(guess) <= max: #check if number is in range
                valid = True 
            else:
                guess= input(f"invalid number entered. Number must be between 1 and {max}: ")   
        else: 
            guess = input (f"only numbers between 1 and {max} is allowed. Please enter a number: ")
    if int(guess) == num:
        print("Yay!! you've guessed the right number!")
        win += 1
    else:
        print(f"Sorry wrong guess. The correct number was {num}")
        lose +=1

    # repeat = input("Do you want to try again? y/n: ")

print(f"You won {win} times and lost {lose} times")