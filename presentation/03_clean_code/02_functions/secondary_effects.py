from typing import List

animals = ["Dog", "Cat", "Lizard", "Snake"]


def print_list(items: List):
    """Print items of a list in a nice format"""

    while items:
        item = items.pop()
        print("- ", item)


print_list(animals)

print(len(animals))
