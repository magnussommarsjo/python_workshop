import time
from typing import Dict


class Database:
    """Sample database"""

    def get_animals(self) -> Dict[str, str]:
        return {"Cats": 2, "Dogs": 10, "Zebras": 1}


class CantConnectDatabase(Database):
    """Sample database that have connection issues"""

    def __init__(self):
        raise ConnectionError("Could not connect to database")


class SlowDatabase(Database):
    """Sample database that have has slow connection"""
    def get_animals(self) -> Dict[str, str]:
        time.sleep(5)
        return super().get_animals()
