import unittest
from employee_function import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.myEmployee = Employee('john', 'smith')
        self.custom_raise = 8000

    def test_give_default_raise(self):
        message = self.myEmployee.give_raise()
        self.assertEqual("Hi, John Smith, you have raised: $5000", message)

    def test_give_custom_raise(self):
        message = self.myEmployee.give_raise(8000)
        self.assertEqual("Hi, John Smith, you have raised: $8000", message)

unittest.main()
