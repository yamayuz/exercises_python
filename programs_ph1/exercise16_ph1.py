"""
Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, 
uppercase letters, numbers, and symbols. The passwords should be random, 
generating a new password every time the user asks for a new password. 
Include your run-time code in a main method.
Extra:
Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
"""

import random as rd

def gen_pass():
    PASS_LEN = 10
    alp = 'abcdefghijklmnopqrstuvwxyz'
    alp_low = list(set(alp))
    alp_upp = list(set(alp.upper()))
    number = list(set('123456789'))
    symbol = list(set('!@#%^&*'))

    temp = []
    for i in range(PASS_LEN):
        temp.append(alp_low[rd.randint(0, len(alp_low) - 1)])
        temp.append(alp_upp[rd.randint(0, len(alp_upp) - 1)])
        temp.append(number[rd.randint(0, len(number) - 1)])
        temp.append(symbol[rd.randint(0, len(symbol) - 1)])

    return ''.join(rd.sample(temp, PASS_LEN))


if __name__ == "__main__":
    print(gen_pass())