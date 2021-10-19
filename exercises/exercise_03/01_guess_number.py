"""
Guess a Number Game
"""

from random import randint

ll, hl = 0, 10  # lower and higher limit
print("Welcome to a Guess a Number!")

should_start_new_round = True
while should_start_new_round:
    correct_number = randint(ll, hl) # Correct number
    is_guess_correct = False
    
    # As long as we are not guessing correct run this
    while not is_guess_correct:

        is_valid_answer = False  # Checks if valid answer is being supplied by user
        while not is_valid_answer:
            # Get guess from user
            guess = input(f"Guess a number between {ll} and {hl} ")
            try:
                guess = int(guess)
            except ValueError:
                # Make sure that we have correct type
                print("Wrong type of input. Needs to be an integer")
                is_valid_answer = False
            else:
                # Change flag so that we can run while loop again and keep 
                # asking for input
                is_valid_answer = True
    
        if guess == correct_number:
            print("Correct!!")
            is_guess_correct = True
        else:
            print("Wrong guess, Try again!")

    # Should we start a new round or not
    is_valid_answer = False  # Flag for valid answer
    while not is_valid_answer:
        answer = input("Do you want to start a new round? ")
        # Handeling of answers
        if answer.lower() == "y":
            should_start_new_round=True
            is_valid_answer = True
        elif answer.lower() == "yes": 
            should_start_new_round=True
            is_valid_answer = True
        elif answer.lower() == "n":
            should_start_new_round=False
            is_valid_answer = True
        elif answer.lower() == 'no':
            should_start_new_round=False
            is_valid_answer = True
        else:
            # If we do not have a valid answer then change flag to False to run
            # while loop again
            print("Did not understand your answer, please reply with Yes/No (Y/N)")
            is_valid_answer  = False

print("End of game, Welcome back")

