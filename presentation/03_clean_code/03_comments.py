from dataclasses import dataclass
from enum import Enum

class EmploymentType(Enum, str):
    FULL_TIME: str = "Full time"
    PART_TIME: str = "Part time"
    

@dataclass
class Employee:
    age: int
    employment_type: EmploymentType

    def is_eligible_for_extra_week_vacation(self):
        if self.age >= 40 and self.employment_type == EmploymentType.FULL_TIME:
            return True
        else:
            return False

# Example


employee = Employee(50, EmploymentType.FULL_TIME)

# Check to see if employee is eligible for an extra week of vacation
if employee.age >= 40 and employee.employment_type == EmploymentType.FULL_TIME:
    ...

if employee.is_eligible_for_extra_week_vacation():
    ...


