"""
Write a function that takes an ordered list of numbers
 (a list where the elements are in order from smallest to largest) and another number. 
 The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.
Extras:
Use binary search.
"""

def find(numbers, num):
    left_idx = -1
    right_idx = len(numbers) - 1

    result = None
    while right_idx - left_idx > 1:
        middle_idx = left_idx + (right_idx - left_idx) // 2

        if numbers[middle_idx] == num:
            result = middle_idx
            break
        elif numbers[middle_idx] < num:
            left_idx = middle_idx   
        else:
            right_idx = middle_idx
        
        if numbers[right_idx] == num:
            result = right_idx
            break
    return result


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    num = 4

    print(find(numbers, num))

