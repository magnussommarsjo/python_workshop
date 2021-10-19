from dataclasses import dataclass


@dataclass
class Employee:
    name: str
    surname: str
    phone_number: str
    salery: int
    home_street: str
    home_street_number: str
    home_postal_code: str
    home_city: str
    work_street: str
    work_street_number: str
    work_postal_code: str
    work_city: str

    def print_home_address(self):
        text = f"""
        {self.home_street} {self.home_street_number}
        {self.home_postal_code}
        {self.home_city}
        """
        print(text)

    def print_work_address(self):
        text = f"""
        {self.work_street} {self.work_street_number}
        {self.work_postal_code}
        {self.home_city}
        """
        print(text)


employee = Employee(
    name="Kenny",
    surname="Svensson",
    phone_number="0701-234567",
    salery=30_000,
    home_street="Some street",
    home_street_number="7B",
    home_postal_code="123 45",
    home_city="Gothenburg",
    work_street="Hard lane",
    work_street_number="5",
    work_postal_code="651 25",
    work_city="Gothenburg",
)

employee.print_home_address()

employee.print_work_address()
