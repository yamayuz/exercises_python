"""
Ask the user for a string and print out whether this string is a palindrome or not.
 (A palindrome is a string that reads the same forwards and backwards.)
"""

import json
import unittest


def is_palindrome(word):
    result = False
    word = word.replace(',', '').replace('.', '').replace(' ', '').lower()
    re_word = word[::-1]

    if word == re_word: result = True
    return result


# testdata
testdata_json = """
        [
            { "values": "Go, dog.", "expected": true },
            { "values": "Good morning!", "expected": false },
            { "values": "No lemon, no melon.", "expected": true },
            { "values": "No, it never propagates if I set a gap or prevention.", "expected": true },
            { "values": "This is pen.", "expected": false }
        ]
    """

# unittest
class TestIsPalingrome(unittest.TestCase):
    def test_is_palindrome(self):
        testdata = json.loads(testdata_json)
        for entry in testdata:
            self.assertAlmostEqual(is_palindrome(entry['values']), entry['expected'])


if __name__ == "__main__":
    unittest.main()
