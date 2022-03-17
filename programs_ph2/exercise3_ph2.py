"""
Take a list, say for example this one:
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.
Extras:
1. Instead of printing the elements one by one, 
   make a new list that has all the elements less than 5 from this list in it and print out this new list.
2. Write this in one line of Python.
3. Ask the user for a number and return a list that contains only elements 
   from the original list a that are smaller than that number given by the user.
"""
import json
import unittest


def create_under_list(target, num):
    result = [ i for i in target if i < num ]
    return result


# testdata
testdata_json = """
        [
            { "values": { "numbers": [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], "num": 5 }, "expected": [1, 1, 2, 3] },
            { "values": { "numbers": [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], "num": 20 }, "expected": [1, 1, 2, 3, 5, 8, 13] },
            { "values": { "numbers": [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], "num": 0 }, "expected": [] },
            { "values": { "numbers": [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], "num": -1 }, "expected": [] },
            { "values": { "numbers": [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], "num": 5.5 }, "expected": [1, 1, 2, 3, 5] }
        ]
    """

# unittest
class TestCreateUnderList(unittest.TestCase):
    def test_create_under_list(self):
        testdata = json.loads(testdata_json)
        for entry in testdata:
            self.assertEqual(create_under_list(entry['values']['numbers'], 
                                               entry['values']['num']), entry['expected'])


if __name__ == "__main__":
    unittest.main()

    


