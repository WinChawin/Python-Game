import random

target = random.randint(1,100)
count = 0
attempts = 0
win = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

print("Select a difficulty level:")
level = input("'e' for easy or 'm' for medium or 'h' for hard: ").lower()

if(level == 'e'):
    print("You have 10 attempts to guess the number.")
    attempts = 10
elif(level == 'm'):
    print("You have 7 attempts to guess the number.")
    attempts = 7
elif(level == 'h'):
    print("You have 4 attempts to guess the number.")
    attempts = 4


while count < attempts:
    guess = int(input("Make a guess: "))
    count += 1

    if(guess > target):
        print("Too high.")
    elif(guess < target):
        print("Too low.")
    else:
        win += 1
        break

if(win):
    print("You got it!")
else:
    print("You've run out of attempts. The number was", target)