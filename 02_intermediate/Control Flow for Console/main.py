import random

def high_low_game():
    print("Welcome to the High-Low Game!")
    rounds = int(input("How many rounds would you like to play? "))
    score = 0

    for round_num in range(1, rounds + 1):
        print(f"\n--- Round {round_num} ---")
        user_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        print(f"Your number is: {user_number}")
        guess = input("Do you think your number is (H)igher or (L)ower than the computer's? ").strip().upper()

        # Show computer's number after guess
        print(f"Computer's number was: {computer_number}")

        # Game logic
        if (guess == 'H' and user_number > computer_number) or \
           (guess == 'L' and user_number < computer_number):
            print("Correct guess! You get a point.")
            score += 1
        else:
            print("Wrong guess! No point this round.")

    print("\nGame Over!")
    print(f"Your final score is: {score} out of {rounds}")

# Run the game
if __name__ == "__main__":
    high_low_game()
