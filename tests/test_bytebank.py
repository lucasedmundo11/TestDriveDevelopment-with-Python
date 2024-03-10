import sys
import pytest
from pytest import mark

from src.bytebank import Employee

class TestClass:
    # GWT Test Methodology

    @mark.xfail
    def test_when_age_is_23(self): 
        # Given
        birth_date = '01/01/2000'
        expected_age = 23
        test_employee = Employee('Test', birth_date, 0)

        # When - Then
        result = test_employee.age()
        assert result == expected_age

    @mark.skipif(sys.version_info < (3, 10), reason='Python version is less than 3.10.')
    def test_when_surname_is_silva(self): 
        # Given
        name = 'Lucas Silva '
        expected_surname = 'Silva'
        test_employee = Employee(name, '', 0)

        # When - Then
        result = test_employee.surname()
        assert result == expected_surname

    # @mark.skip(reason='Not implemented yet.')
    def test_when_salary_decrease_is_9000(self):
        # Given
        salary = 10000
        expected_salary = 9000
        test_employee = Employee('Lucas Silva ', '', salary)

        # When - Then
        test_employee.salary_decrease()
        result = test_employee.salary
        assert result == expected_salary

    @mark.calculate_bonus
    def test_when_calculate_bonus_is_100(self):
        # Given
        salary = 1000
        expected_bonus = 100
        test_employee = Employee('', '', salary)

        # When - Then
        result = test_employee.calculate_bonus()
        assert result == expected_bonus

    @mark.calculate_bonus
    def test_when_calculate_bonus_is_ineligible(self):
        with pytest.raises(Exception):
            # Given
            salary = 1000000
            test_employee = Employee('', '', salary)

            # When - Then
            result = test_employee.calculate_bonus()
            assert result

    def test_employee_print(self):
        # Given
        name = 'Lucas Silva'
        birth_date = '01/01/2000'
        salary = 1000
        expected_print = f'Employee({name}, {birth_date}, {salary})'
        test_employee = Employee(name, birth_date, salary)

        # When - Then
        result = test_employee.__str__()
        assert result == expected_print