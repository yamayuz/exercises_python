"""
Ask the user for a number. Depending on whether the number is even or odd, 
print out an appropriate message to the user. 
Hint: how does an even / odd number react differently when divided by 2?
Extras:
1. If the number is a multiple of 4, print out a different message.
2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
   If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""
import json
import unittest


def check_div(num, check):
    return True if num % check == 0 else False


# テストデータ
testdata_json = """
        [
            { "values": { "num": 12, "check": 2 }, "expected": true },
            { "values": { "num": 12, "check": 5 }, "expected": false },
            { "values": { "num": 178, "check": 9 }, "expected": false },
            { "values": { "num": 6, "check": 5 }, "expected": false },
            { "values": { "num": 120, "check": 30 }, "expected": true }        
        ]
    """

# unittest
class TestCheckDiv(unittest.TestCase):
    def test_check_div(self):
        testdata_list = json.loads(testdata_json)
        for entry in testdata_list:
            self.assertAlmostEqual(check_div(entry['values']['num'], 
                                             entry['values']['check']), entry['expected'])


if __name__ == "__main__":
    unittest.main()