"""
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
and makes a new list of only the first and last elements of the given list. For practice, 
write this code inside a function.
"""

def create_list(list):
    return [list[0], list[-1]]


if __name__ == "__main__":
    a = [5, 10, 15, 20, 25]

    print(create_list(a))