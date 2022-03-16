"""
Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that 
they will turn 100 years old. Note: for this exercise, 
the expectation is that you explicitly write out the year (and therefore be out of date the next year).
"""
import datetime


if __name__ == "__main__":
    dt_now = datetime.datetime.now()
    dt_now_year = dt_now.year

    age = int(input('年齢を入力してください：'))
    num = int(input('数字を入力してください：'))

    dt_hundred_year = dt_now_year - age + 100
    for i in range(num):
        print(f'あなたが100歳になるのは西暦{dt_hundred_year}年です。')

    
    
    