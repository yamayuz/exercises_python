"""
Ask the user for a number and determine whether the number is prime or not. 
(For those who have forgotten, a prime number is a number that has no divisors.). 
You can (and should!) use your answer to Exercise 4 to help you. 
Take this opportunity to practice using functions, described below.
"""

def is_prime(number):
    if number == 0 or number < 0:
        return False

    for i in range(2, number):
        if number % i == 0: return False

    return True


if __name__ == "__main__":
    number = int(input('整数を入力してください:'))

    if is_prime(number):
        print(f'{number}は素数です')
    else:
        print(f'{number}は素数ではありません')
