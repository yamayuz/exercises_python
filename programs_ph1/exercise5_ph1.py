"""
Take two lists, say for example these two:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that 
are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes.
"""

import random

if __name__ == "__main__":
    target_list1 = [random.randint(0, 20) for i in range(15)]
    target_list2 = [random.randint(0, 20) for i in range(20)]

    result = []
    for i in target_list1:
        if i in target_list2 and i not in result: result.append(i)
            
    print(f'a: {target_list1}')
    print(f'b: {target_list2}')
    print(f'result: {result}')