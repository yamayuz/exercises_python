"""
Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), compare them, 
print out a message of congratulations to the winner, and ask if the players want to start a new game)
Remember the rules:
・Rock beats scissors
・Scissors beats paper
・Paper beats rock
"""
import json
import unittest
import random as rd
import itertools as it


def judge_winorlose(npc, player):
    result = npc - player

    if result == 0:
        return 'あいこです！'
    elif result in [-2, 1]:
        return 'あなたの勝ちです！'
    elif result in [-1, 2]:
        return 'あなたの負けです！'


# testdata
testdata_json = """
        [
            { "values": { "npc": 1, "player": 1 }, "expected": "あいこです！" },
            { "values": { "npc": 1, "player": 2 }, "expected": "あなたの負けです！" },
            { "values": { "npc": 1, "player": 3 }, "expected": "あなたの勝ちです！" },
            { "values": { "npc": 2, "player": 1 }, "expected": "あなたの勝ちです！" },
            { "values": { "npc": 2, "player": 2 }, "expected": "あいこです！" },
            { "values": { "npc": 2, "player": 3 }, "expected": "あなたの負けです！" },
            { "values": { "npc": 3, "player": 1 }, "expected": "あなたの負けです！" },
            { "values": { "npc": 3, "player": 2 }, "expected": "あなたの勝ちです！" },
            { "values": { "npc": 3, "player": 3 }, "expected": "あいこです！" }
        ]
    """

# unittest
class TestJudgeWinorlose(unittest.TestCase):
    def test_judge_winororlose(self):
        testdata = json.loads(testdata_json)
        for entry in testdata:
            self.assertEquals(judge_winorlose(entry['values']['npc'], 
                                              entry['values']['player']), entry['expected'])


if __name__ == "__main__":
    unittest.main()
