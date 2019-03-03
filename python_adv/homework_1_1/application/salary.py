def calculate_salary(person_salary_dict, months):
    salary_list = []
    for person, salary in person_salary_dict.items():
        salary_list.append((person, salary * months))
    return salary_list