import random

number = random.randint(1,9)
chances = 0

while chances < 5:
    guess = int(input("Enter your Guess: "))
    
    if guess != number and guess < number:
        print(f"Your guess was too low: Guess a number higher than {guess}\n")
        chances += 1
    elif guess != number and guess > number:
        print(f"Your guess as too high: Guess a number lower than {guess}\n")
        chances += 1
    
    if guess == number:
        print("Congratulations YOU WON!!!")
        break
    
    if guess != number and chances == 5:
        print("You unfortunately lost this game...")
        break