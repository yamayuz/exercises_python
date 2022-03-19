"""
Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), compare them, 
print out a message of congratulations to the winner, and ask if the players want to start a new game)
Remember the rules:
・Rock beats scissors
・Scissors beats paper
・Paper beats rock
"""
import random as rd
import itertools as it

# if __name__ == "__main__":
    # id2janken = { 0: 'rock', 1: 'scissors', 2: 'paper' }
    # janken2id = { 'rock': 0, 'scissors': 1, 'paper': 2 }
    # comb = [[[0, 1], 0], # 負け -1
    #         [[0, 2], 1], # 勝ち -2
    #         [[1, 0], 1], # 勝ち 1
    #         [[1, 2], 0], # 負け -1
    #         [[2, 0], 0], # 負け 0
    #         [[2, 1], 1], # 勝ち 1
    # ]

    # while True:
    #     npc = rd.randint(0, 2)
    #     player = janken2id[input('じゃんけん ぽん → :')]
    #     shobu = [npc, player]
    #     result = 2

    #     for i in comb:
    #         if i[0] == shobu: result = i[1]

    #     print(f'npc: {id2janken[npc]}')
    #     if result == 0:
    #         print('あなたの負けです！')
    #     elif result == 1:
    #         print('あなたの勝ちです！')
    #     elif result == 2:
    #         print('あいこです！')

    #     cont = input('続けますか？(Yes:1, No:0):')
    #     if cont == '0': break

def judge_winorlose(npc, player):
    result = npc - player

    if result == 0:
        return 'あいこです！'
    elif result in [-2, 1]:
        return 'あなたの勝ちです！'
    elif result in [-1, 2]:
        return 'あなたの負けです！'


if __name__ == "__main__":
    id2janken = { 1: 'rock', 2: 'scissors', 3: 'paper' }
    janken2id = { 'rock': 1, 'scissors': 2, 'paper': 3 }
    
    while True:
        npc = rd.randint(1, 3)
        print('rock, scissors, paper')
        player = janken2id[input('じゃんけん ぽん → :')]

        print(f'npc: {id2janken[npc]}')
        print(judge_winorlose(npc, player))

        cont = input('続けますか？(Yes:1, No:0):')
        if cont == '0': break