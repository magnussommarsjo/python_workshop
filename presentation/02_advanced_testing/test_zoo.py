"""Naive way of testing the zoo functions"""

from zoo import feed_animals, get_number_of_animals
from database import Database


def test_feed_animals():
    database = Database()
    feed_animals(database)
    #  Note: Does not really test anything!


def test_get_number_of_animals():
    num_animals = get_number_of_animals()
    assert num_animals == 13
    # What if the number of animals change in the database?!
