import random

def guess_the_number():
    name = input("Hello! What is your name? ")
    number_to_guess = random.randint(1, 20)
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    guesses_taken = 0
    while True:
        guess = int(input("Take a guess: "))
        guesses_taken += 1

        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break

guess_the_number()
