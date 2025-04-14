import random

def guess_my_number():
    print("Welcome to 'Guess My Number'!")
    print("I'm thinking of a number between 0 and 99.")

    # Random number generate karo between 0 and 99
    secret_number = random.randint(0, 99)
    guess = None

    # Jab tak guess sahi nahi hota, loop chalta rahega
    while guess != secret_number:
        try:
            guess = int(input("Enter your guess: "))

            if guess < 0 or guess > 99:
                print("Please enter a number between 0 and 99.")
                continue

            if guess > secret_number:
                print("Your guess is too high.")
            elif guess < secret_number:
                print("Your guess is too low.")
            else:
                print(f"Congrats! The number was: {secret_number}")
        except ValueError:
            print("Please enter a valid number.")

# Run the game
if __name__ == "__main__":
    guess_my_number()
