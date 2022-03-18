"""
Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
"""

if __name__ == "__main__":
    number = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    result = [ num for num in number if num % 2 == 0]

    print(number)
    print(result)