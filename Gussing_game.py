# import random

# def guessing_game():
#     # Randomly generate a number between 1 and 100
#     number_to_guess = random.randint(1, 100)
    
#     # Set the maximum number of attempts
#     max_attempts = 10
#     attempts_left = max_attempts
    
#     print("Welcome to the Guessing Game!")
#     print("I'm thinking of a number between 1 and 100.")
#     print(f"You have {max_attempts} attempts to guess the number.")

#     # Start the guessing loop
#     while attempts_left > 0:
#         guess = int(input(f"\nYou have {attempts_left} attempts left. Enter your guess: "))
        
#         # Check if the guess is correct
#         if guess == number_to_guess:
#             print("Congratulations! You guessed the number correctly!")
#             break
        
#         # Provide hints for high or low guesses
#         if guess < number_to_guess:
#             print("Too low!")
#         else:
#             print("Too high!")

#         # Offer additional hints based on how close the guess is
#         if attempts_left <= 5:  # Give closer hints after 5 attempts
#             difference = abs(number_to_guess - guess)
#             if difference <= 10:
#                 print("You're within 10 of the number!")
#             if difference <= 5:
#                 print("You're very close! Within 5 of the number!")
        
#         attempts_left -= 1

#     # If the player runs out of attempts
#     if attempts_left == 0:
#         print(f"Sorry, you're out of attempts. The number was {number_to_guess}.")

# # Run the game
# guessing_game()
