import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):

    """
    测试 name_function.py
    方法名必须以 test_打头，这样它才会在运行 test_name_function.py 时自动运行
    """

    def test_first_last_name(self):
        formatted_name = get_formatted_name('john', 'smith')
        self.assertEqual(formatted_name, 'John Smith')

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('john', 'smith', 'middle')
        self.assertEqual(formatted_name, 'John Middle Smith')

unittest.main()