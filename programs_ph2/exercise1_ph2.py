"""
Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that 
they will turn 100 years old. Note: for this exercise, 
the expectation is that you explicitly write out the year (and therefore be out of date the next year).
"""
import datetime
import json
import unittest


def calc_hundred_year(age):
    dt_now = datetime.datetime.now()
    dt_now_year = dt_now.year
    return dt_now_year - age + 100


# テストデータ
testdata_json = """
        [
            { "value": 0, "expected": 2122 },
            { "value": 1, "expected": 2121 },
            { "value": 2, "expected": 2120 },
            { "value": 3, "expected": 2119 },
            { "value": 4, "expected": 2118 }
        ]
    """

# unittest
class TestCalcHundredYear(unittest.TestCase):
    def test_calc_hundred_year(self):
        testdata_list = json.loads(testdata_json)
        for entry in testdata_list:
            self.assertEqual(calc_hundred_year(entry['value']), entry['expected'])


if __name__ == "__main__":
    unittest.main()

    
    
    