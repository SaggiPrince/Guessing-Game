import random

#Random number generator ranging from 1-100
randm = random.randint(1,100)

#Introduction to the game including the rules
print("WELCOME TO GUESS ME!\n"
      "I'm thinking of a number between 1 and 100\n"
      "If your guess is more than 10 away from my number, I'll tell you you're COLD\n"
      "If your guess is within 10 of my number, I'll tell you you're WARM\n"
      "If your guess is farther than your most recent guess, I'll say you're getting COLDER\n"
      "If your guess is closer than your most recent guess, I'll say you're getting WARMER\n"
      "LET'S PLAY!\n")

#Storage for each guess
guesses = [0]

while True:
    guess = int(input("I'm thinking of a number between 1 and 100.\n  What is your guess? "))

    if guess < 1 or guess > 100:
        print("OUT OF BOUNDS! Please try again: ")
        continue

    break

while True:
    guess = int(input("I'm thinking of a number between 1 and 100.\n  What is your guess?"))

    if guess < 1 or guess > 100:
        print("OUT OF BOUNDS! Please try again: ")
        continue

    #Comparing the player's guess to our number
    if guess == randm:
        print(f'CONGRATULATIONS, YOU GUESSED IT IN ONLY {len(guesses)} GUESSES!!')
        break

    #if wrong add guess to the list
    guesses.append(guess)

    #When testing the first guess, guesses[-2] == 0, which evaluates to False
    if guesses[-2]:
        if abs(randm-guess) < abs(randm-guesses[-2]):
            print('WARMER!')
        else:
            print('COLDER!')
    else:
        if abs(randm-guess) <= 10:
            print('WARM!')
        else:
            print('COLD!')