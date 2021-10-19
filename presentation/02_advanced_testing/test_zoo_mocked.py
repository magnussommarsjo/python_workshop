"""Naive way of testing the zoo functions"""

import pytest
from unittest.mock import Mock, patch

from zoo import feed_animals, get_number_of_animals
from database import Database

@pytest.fixture
def mock_database():
    # Treat Mock object as a Database
    mock_database = Mock(spec=Database)  

    # Apply a return value to 'get_animals' method
    mock_database.get_animals.return_value = {'Lions': 1, 'Tigers': 2} 
    return mock_database


def test_feed_animals(mock_database):
    feed_animals(mock_database)
    #  Note: Does not really test anything!


def test_feed_animals_better(mock_database):
    with patch('builtins.print') as mock_print:
        feed_animals(mock_database)
        mock_print.assert_called()
        #  Note: Now it tests that print was called at least once
    
        mock_database.get_animals.assert_called_once()
        #We also checked that the 'get_animals' method was called exactly once


def test_get_number_of_animals(mock_database):
    with patch('database.Database', return_value=mock_database):
        num_animals = get_number_of_animals()
    assert num_animals == 13
    # Still one major issue in this!
