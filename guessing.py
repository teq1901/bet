import random

def valid_guess(prompt):
    valid = False
    guess= input(prompt)
    while not valid:
        if guess.isnumeric():
            guess = int (guess)
            if guess>= 1 and guess <= max: #check if number is in range
                valid = True 
            else:
                guess= input(f"invalid number entered. Number must be between 1 and {max}: ")   
        else: 
            guess = input (f"only numbers between 1 and {max} is allowed. Please enter a number: ")
    return guess

    #this code starts here
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
max = 5
score = 0


for i in range(rounds):
    print(f"Round {i+1}")
    #generate a random number
    num = random.randint(1, max)
    
    guess = valid_guess(f"Guess a number between 1 and {max}: ")
    
    while guess != num:

        if guess > num:
            guess = valid_guess(f"try again, guess lower: ")
            score -=2
        else:
            guess = valid_guess(f"try again guess higher: ")
            score -=2

    if guess == num:
        print("Yay!! you've guessed the right number!")
        score += max

    print(f"your score is now {score} ")

print(f"Your total score was {score}")