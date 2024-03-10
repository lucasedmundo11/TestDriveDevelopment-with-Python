from datetime import date

class Employee:
    def __init__(self, name, birth_date, salary):
        self._name = name
        self._birth_date = birth_date
        self._salary = salary

    @property
    def name(self):
        return self._name

    @property
    def salary(self):
        return self._salary
    
    def surname(self):
        return self._name.strip().split(' ')[-1]

    def age(self):
        birth_year = self._birth_date.split('/')[-1]
        current_year = date.today().year
        return current_year - int(birth_year)

    def calculate_bonus(self):
        value = self._salary * 0.1
        if value > 1000:
            raise Exception('Salary ineligible for bonus.')
        return value
    
    def _is_director(self):
        directors_surnames = ['Silva', 'Souza', 'Santos']
        return (self._salary >= 10000) and (self.surname() in directors_surnames)
    
    def salary_decrease(self):
        if self._is_director():
            self._salary *= 0.9
        pass

    def __str__(self):
        return f'Employee({self._name}, {self._birth_date}, {self._salary})'