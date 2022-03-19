"""
Write a program (using functions!) that asks the user for a long string containing multiple words. 
Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
  My name is Michele
Then I would see the string:
  Michele is name My
shown back to me.
"""

def rev_sentence(string):
    temp = string.split()
    return ' '.join(temp[::-1])


if __name__ == "__main__":
    string = input('文章を入力してください(英文で）:')
    print(rev_sentence(string))
