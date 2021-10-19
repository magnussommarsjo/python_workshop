"""Module to handle a zoo"""

from database import Database

# Database as an argument
def feed_animals(database: Database):
    animals = database.get_animals()
    for animal, number in animals.items():
        print(f"{number} of our {animal} was fed!")

# Database instance created in method
def get_number_of_animals() -> int:
    database = Database()
    animals = database.get_animals()
    return sum(animals.values())
