"""
Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
"""

import json
from re import L
import unittest

def select_even_elements(number):
    return [ num for num in number if num % 2 == 0]


# testdata
testdata_json = """
        [
            { "values": [1, 4, 9, 16, 25, 36, 49, 64, 81, 100], "expected": [4, 16, 36, 64, 100] },
            { "values": [1, 4, 9], "expected": [4] },
            { "values": [1, 4, 9, 16, 25], "expected": [4, 16] },
            { "values": [], "expected": [] },
            { "values": [1], "expected": [] }
        ]
    """

# unittest
class TestSelectEvenElements(unittest.TestCase):
    def test_select_even_elements(self):
        testdata = json.loads(testdata_json)
        for entry in testdata:
            self.assertEquals(select_even_elements(entry['values']), entry['expected'])


if __name__ == "__main__":
    unittest.main()