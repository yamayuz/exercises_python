"""
Ask the user for a string and print out whether this string is a palindrome or not.
 (A palindrome is a string that reads the same forwards and backwards.)
"""

if __name__ == "__main__":
    word = input("文字列を入力してください:")

    word = word.replace(',', '').replace('.', '').replace(' ', '').lower()
    re_word = word[::-1]

    if word == re_word:
        print('その文章は回文です。')
    else:
        print('その文章は回文ではありません。')
