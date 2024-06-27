import random  # Import the random module to generate random numbers

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Set the number of guesses allowed
num_guesses = 5

# Start the game loop
while num_guesses > 0:
    # Prompt the player to enter a guess
    guess = int(input("Guess a number between 1 and 100: "))

    # Check if the guess is correct
    if guess == secret_number:
        print("Congratulations! You guessed the number correctly.")
        break  # Exit the game loop

    # Provide feedback based on the guess
    elif guess < secret_number:
        print("Your guess is too low. Try a higher number.")
    else:
        print("Your guess is too high. Try a lower number.")

    # Decrement the number of guesses
    num_guesses -= 1

# If the player runs out of guesses, reveal the secret number
if num_guesses == 0:
    print("Sorry, you ran out of guesses. The secret number was:", secret_number)