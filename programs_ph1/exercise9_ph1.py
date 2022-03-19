"""
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, 
then tell them whether they guessed too low, too high, or exactly right. 
(Hint: remember to use the user input lessons from the very first exercise)
Extras:
1. Keep the game going until the user types “exit”
2. Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""

import random as rd

def compaer_number(rd_num, guess):
    if rd_num == guess:
        return '正解です！'
    elif rd_num < guess:
        return '大きすぎます！'
    elif rd_num > guess:
        return '小さすぎます！'


if __name__ == "__main__":
    count = 0
    guess = 0
    rd_num = rd.randint(1, 9)

    while rd_num != guess and guess != 'exit':
        guess = input('1～9の数字を入力してください:')

        if guess == 'exit':
            break

        count += 1
        guess = int(guess)
        print(compaer_number(rd_num, guess))

    print(f'答え: {rd_num}')
    print(f'チャレンジ回数: {count}')


    # count = 0
    # while True:
    #     count += 1
    #     number = rd.randint(1, 9)
    #     predict_number = int(input('予想する数字を入力してください(1～9):'))

    #     print(f'答えは{number}！')
    #     if number == predict_number:
    #         print('ぴったり正解です！')
    #     elif number < predict_number:
    #         print('大きすぎます！')
    #     elif number > predict_number:
    #         print('小さすぎます！')

    #     is_continue = input('続けますか？(y: Yes, n: No) :')
    #     if is_continue == 'n':
    #         break

    # print(f'{count}回予測しました。')
