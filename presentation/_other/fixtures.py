import pytest


@pytest.fixture
def simple_data() -> dict:
    return {"Dummy": "Data"}


def test_using_fixture(simple_data: dict):  # Good to annotate the data type
    assert "Dummy" in simple_data.keys()


class Database:
    def connect(self):
        print("Connecting ...")

    def get_data(self) -> dict:
        return {"Dummy": "Data"}

    def close(self):
        print("Closed connectin to DB!")


@pytest.fixture
def database() -> Database:

    db = Database()  # Set up
    db.connect()

    yield db  # Return the database

    db.close()  # Tear down


def test_database_content(database: Database):
    assert "Dummy" in database.get_data().keys()


# ===== SEPERATE FILES ===

# src/database.py
class Database:
    ...

# tests/conftest.py
@pytest.fixture
def database() -> Database:

    db = Database()  # Set up
    db.connect()

    yield db  # Return the database

    db.close()  # Tear down


# tests/unit/test_database.py
def test_database_content(database: Database):
    assert "Dummy" in database.get_data().keys()