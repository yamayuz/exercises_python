"""
以下のようなボードをプリントする。
ただし、ボードのサイズはユーザーが入力できるようにすること。
 --- --- --- 
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- --- 
"""

def print_horiz(board_size):
    print(' ---' * board_size)


def print_vert(board_size):
    print('|   ' * (board_size + 1))


def print_board(board_size):
    for i in range(board_size):
        print_horiz(board_size)
        print_vert(board_size)
    print_horiz(board_size)


if __name__ == "__main__":
    board_size = int(input('ボードのサイズを入力してください:'))
    print_board(board_size)
    