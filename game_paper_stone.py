def Paper_Stone():
    print('player 1')
    print('''1.stone
2.paper
3.scissor''')
    player1 = int(input('choice ='))
    print('player 2')
    print('''1.stone
2.paper
3.scissor''')
    player2 = int(input('choice ='))
    if 0 < player1 < 4 and 0 < player2 < 4:
        if player1 ==2 and player2 == 1 or player1 == 1 and player2 == 3 or player1 == 3 and player2 == 2:
            print('player1 wins')
        elif player2 ==2 and player1 == 1 or player2 == 1 and player1 == 3 or player2 == 3 and player1 == 2:
            print('player2 wins')
        elif player1 == player2:
            print('equal, try more!')
    else:
        print('choice correct!')
Paper_Stone()