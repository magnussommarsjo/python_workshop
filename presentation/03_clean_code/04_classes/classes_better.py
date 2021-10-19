from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Employee:
    name: str
    surname: str
    phone_number: str
    salery: int
    home_address: Address
    work_address: Address

@dataclass
class Address:
    street: str
    street_number: str
    postal_code: str
    city: str

    def __str__(self) -> str:
        text = f"""
        {self.street} {self.street_number}
        {self.postal_code}
        {self.city}
        """
        return(text)


work_address = Address(
    street="Hard lane",
    street_number="5",
    postal_code="651 25",
    city="Gothenburg"
)

home_address = Address(
    street="Some street",
    street_number="7B",
    postal_code="123 45",
    city="Gothenburg",
)

employee = Employee(
    name="Kenny",
    surname="Svensson",
    phone_number="0701-234567",
    salery=30_000,
    work_address=work_address,
    home_address=home_address
)



print(employee.home_address)

print(employee.work_address)
