"""
Take two lists, say for example these two:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that 
are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes.
"""

import json
import unittest
import random

def create_comelements(target1, target2):
    result = []
    for i in target1:
        if i in target2 and i not in result: result.append(i)

    return result


# testdata
testdata_json = """
        [
            { "values": { "list1": [1, 1, 2, 3, 5], "list2": [1, 2] }, "expected": [1, 2] },
            { "values": { "list1": [3, 9, 5, 1, 0], "list2": [9, 0, 5, 90, 54] }, "expected": [9, 5, 0] }
        ]
    """

# unittest
class TestCreateComelements(unittest.TestCase):
    def test_create_comelements(self):
        testdata = json.loads(testdata_json)
        for entry in testdata:
            self.assertEqual(create_comelements(entry['values']['list1'], 
                                                entry['values']['list2']), entry['expected'])


if __name__ == "__main__":
    unittest.main()