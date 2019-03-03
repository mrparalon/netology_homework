from application.salary import calculate_salary
from application.db import people


if __name__ == "__main__":
    employees = people.get_employees()
    salary_list = calculate_salary(employees, 12)
    print(salary_list)