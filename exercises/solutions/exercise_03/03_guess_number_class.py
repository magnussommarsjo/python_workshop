"""
Guess a Number Game
"""

from random import randint


class GuessNumberGame:
    def __init__(self, lower_limit: int = 0, higher_limit: int = 10):
        """Guess a number guess game

        Parameters
        ----------
        lower_limit : int, optional
            Lower limit of numbers, by default 0
        higher_limit : int, optional
            Higher limit of numbers, by default 10
        """
        self.lower_limit = lower_limit
        self.higher_limit = higher_limit

    def start(self) -> None:
        """Starts a new game"""
        print("Welcome to a Guess a Number!")

        self._start_new_round()
        while self._should_start_new_round():
            self._start_new_round()

        print("End of game, Welcome back")

    def _start_new_round(self):
        """Start a new round of Guess a Number"""
        correct_number = randint(self.lower_limit, self.higher_limit)
        is_guess_correct = False
        while not is_guess_correct:
            guess = self._get_user_guess()
            if guess == correct_number:
                print("Correct!!")
                is_guess_correct = True
            else:
                print("Wrong guess, Try again!")

    def _should_start_new_round(self) -> bool:
        """Ask user for input, wheter or not a new round should be started"""
        answer = input("Do you want to start a new round? ")
        if any(answer.lower() == item for item in ["y", "yes"]):
            return True
        elif any(answer.lower() == item for item in ["n", "no"]):
            return False
        else:
            print("Did not understand your answer, please reply with Yes/No (Y/N)")
            return self._should_start_new_round()

    def _get_user_guess(self) -> int:
        """Get user input of a number guess"""
        guess = input(
            f"Guess a number between {self.lower_limit} and {self.higher_limit} "
        )

        try:
            guess = int(guess)
        except ValueError:
            print("Wrong type of input. Needs to be an integer")
            guess = self._get_user_guess(self.lower_limit, self.higher_limit)
        else:
            return guess


if __name__ == "__main__":
    game = GuessNumberGame(0, 3)
    game.start()
