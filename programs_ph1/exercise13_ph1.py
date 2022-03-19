"""
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
Take this opportunity to think about how you can use functions. 
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is 
the sum of the previous two numbers in the sequence. 
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""

def gen_fib(num):
    if num == 0 or num < 0:
        return None

    fibonnaci = [1]
    for i in range(num):
        if i == 1:
            fibonnaci.append(1)
        if i >= 2:
            fibonnaci.append(fibonnaci[i-1] + fibonnaci[i-2])

    return fibonnaci


if __name__ == "__main__":
    num = int(input('作成するフィボナッチ数の個数を入力してください:'))
    print(gen_fib(num))