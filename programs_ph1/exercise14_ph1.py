"""
Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
Extras:
Write two different functions to do this - one using a loop and constructing a list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a different function.
"""

import random

def create_list_1(tar1, tar2):
    return list(set(tar1) - set(tar2))


def del_dupl_list(target):
    result = []
    for i in range(len(target)):
        if not target[i] in result: result.append(target[i])
    return result


def del_dupl_set(target):
    return list(set(target))


if __name__ == "__main__":
    tar1 = [random.randint(0, 20) for i in range(15)]
    tar2 = [random.randint(0, 20) for i in range(20)]

    print('exercise5')
    print(f'tar1: {tar1}')
    print(f'tar2: {tar2}')
    print(f'result: {create_list_1(tar1, tar2)}')
    print('-' * 10)
    print(f'tar1: {tar1}')
    print(f'result: {del_dupl_list(tar1)}')
    print('-' * 10)
    print(f'tar1: {tar1}')
    print(f'result: {del_dupl_set(tar1)}')