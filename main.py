from src import Employee

def main():
    employee = Employee('Lucas Silva', '01/01/2000', 10000)
    print(employee)
    print(employee.age())
    print(employee.surname())
    print(employee.calculate_bonus())
    print(employee.salary_decrease())

if __name__ == '__main__':
    main()

