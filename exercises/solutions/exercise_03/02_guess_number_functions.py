"""
Guess a Number Game
"""

from random import randint


def start_game(lower_limit: int = 0, higher_limit: int = 10) -> None:
    """Starts a new game"""
    print("Welcome to a Guess a Number!")

    start_new_round(lower_limit, higher_limit)
    while should_start_new_round():
        start_new_round(lower_limit, higher_limit)

    print("End of game, Welcome back")


def start_new_round(lower_limit: int, higher_limit: int):
    """Start a new round of Guess a Number

    Parameters
    ----------
    lower_limit : int
        lower limit allowed for a number
    higher_limit : int
        higher limit allowed for a number
    """
    correct_number = randint(lower_limit, higher_limit)
    is_guess_correct = False
    while not is_guess_correct:
        guess = get_user_guess(lower_limit, higher_limit)
        if guess == correct_number:
            print("Correct!!")
            is_guess_correct = True
        else:
            print("Wrong guess, Try again!")


def should_start_new_round() -> bool:
    """Ask user for input, wheter or not a new round should be started

    Returns
    -------
    bool
        True if a  new round should be started, else False
    """
    answer = input("Do you want to start a new round? ")
    if any(answer.lower() == item for item in ["y", "yes"]):
        return True
    elif any(answer.lower() == item for item in ["n", "no"]):
        return False
    else:
        print("Did not understand your answer, please reply with Yes/No (Y/N)")
        return should_start_new_round()


def get_user_guess(lower_limit: int, higher_limit: int) -> int:
    """Get user input of a number guess

    Parameters
    ----------
    lower_limit : int
        lower limit allowed for a number
    higher_limit : int
        higher limit allowed for a number

    Returns
    -------
    int
        The number guessed 
    """
    guess = input(f"Guess a number between {lower_limit} and {higher_limit} ")

    try:
        guess = int(guess)
    except ValueError:
        print("Wrong type of input. Needs to be an integer")
        guess = get_user_guess(lower_limit, higher_limit)
    else:
        return guess


if __name__ == "__main__":
    start_game()
