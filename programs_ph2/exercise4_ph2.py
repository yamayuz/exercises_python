"""
Create a program that asks the user for a number and then prints out 
a list of all the divisors of that number. 
(If you don’t know what a divisor is, it is a number that divides evenly into another number. 
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
"""

import json
import unittest

def cal_Primefactor(num):
    result = []
    try:
        for i in range(1, num+1):
            if num % i == 0: result.append(i)
    except Exception:
        pass # エラー時は空のリストを返却
    return result


# testdata
testdata_json = """
        [
            { "values": 7, "expected": [1, 7] },
            { "values": 10, "expected": [1, 2, 5, 10] },
            { "values": -1, "expected": [] },
            { "values": 0, "expected": [] },
            { "values": 7.6, "expected": [] }
        ]
    """

# unittest
class TestCalPrimefactor(unittest.TestCase):
    def test_cal_primefactor(self):
        testdata = json.loads(testdata_json)

        for entry in testdata:
            self.assertEqual(cal_Primefactor(entry['values']), entry['expected'])


if __name__ == "__main__":
    unittest.main()