# Mock whole object

from unittest.mock import Mock


class Database:
    def get_something(self) -> dict:
        ...


mock_database = Mock(spec=Database)
mock_database.get_something.return_value = {"Dummy": "Data"}
# or
mock_database.get_something.side_effect = ValueError()

# Mock parts of the code

from unittest.mock import Mock


class Database:
    def get_something(self) -> dict:
        ...


database = Database()
database.get_something = Mock(return_value={"Dummy": "Data"})


# Patch as context manager

from unittest.mock import patch


class Database:
    def get_something(self) -> dict:
        ...


def function_calling_database():
    data = Database().get_something()
    print(data)


with patch("__main__.Database.get_something", return_value={"Dummy": "Data"}):
    function_calling_database()

# Patch as decorator

from unittest.mock import patch, Mock


class Database:
    def get_something(self) -> dict:
        ...


def function_calling_database():
    data = Database().get_something()
    print(data)


@patch("__main__.Database.get_something", return_value={"Dummy": "Data"})
def test_function_calling_database(mock_get_something: Mock):
    function_calling_database()
    mock_get_something.assert_called_once()  # Teaser


test_function_calling_database()

# Assert statements
mock = Mock()

mock.assert_called() # assert that the mock was called at least once
mock.assert_called_once() # assert that the mock was called only once.
mock.assert_called_with(args=...)  # assert that the mock was called with the specified arguments.
mock.assert_not_called() # assert that the mock was never called.
# etc...
