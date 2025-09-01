# guessing_game.py
import random

def display_title():
    """
    Shows title and the programming specifications.
    """
    print("==========================================")
    print("        Number Guessing Game Project       ")
    print("==========================================")
    print("Programming Specifications:")
    print("1. A random number between 1 and 10 is generated.")
    print("2. The user must guess the number.")
    print("3. Program will give hints if guess is 'Too low' or 'Too high'.")
    print("4. Game continues until the correct guess is made.")
    print("5. User can choose to play again or exit.")
    print("==========================================\n")

def get_random_number(low=1, high=10):
    """Return a random integer between low and high (inclusive)."""
    return random.randint(low, high)

def play_game():
    """
    Main game loop:
    - Generates a random number.
    - Continues prompting user until guess matches.
    - Shows hints 'Too low' / 'Too high' / 'You guessed it'.
    """
    number_to_guess = get_random_number(1, 10)
    while True:
        user_input = input("Enter your guess (1–10): ").strip()
        # validate integer
        if not user_input.isdigit():
            print("Invalid input! Please enter an integer between 1 and 10.")
            continue

        guess = int(user_input)
        if guess < 1 or guess > 10:
            print("Out of range. Enter a number between 1 and 10.")
            continue

        if guess < number_to_guess:
            print("Too low. Try again.")
        elif guess > number_to_guess:
            print("Too high. Try again.")
        else:
            print("You guessed it! 🎉")
            break

    # return to caller (main)
    return

def main():
    display_title()
    play_again = "yes"
    while play_again.lower() == "yes":
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").strip()
        if play_again == "":
            play_again = "no"
    print("\nThanks for playing! Goodbye 👋")

if __name__ == "__main__":
    main()
