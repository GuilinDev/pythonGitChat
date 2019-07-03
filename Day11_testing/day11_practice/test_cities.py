import unittest
from city_functions import cityCountry

class CityTestCases(unittest.TestCase):

    def testCiyAndCountry(self):
        formatted_name = cityCountry('Denver', "USA")
        self.assertEqual(formatted_name, 'Denver, USA')

    def testCiyAndCountryAndPopulation(self):
        formatted_name = cityCountry('Denver', "USA", 500000)
        self.assertEqual(formatted_name, 'Denver, USA, 500000')

unittest.main()