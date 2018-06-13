import random
import time
import sys

theboard = {'topL': '', 'topM': '', 'topR': '',
            'midL': '', 'midM': '', 'midR': '',
            'lowL': '', 'lowM': '', 'lowR': ''}

def start():
    option = input()
    faceCoin = random.choice('ht')
    return option, faceCoin

def menu():
    print('+' * 65)
    print('Hello, this is the Tic Tac Toe Game!')
    print('Do you think you can beat an intelligent computer like me?')
    print("Let's the God of Luck decide who will start!")
    print('Do you want head or tails? Type "h" or "t" in the keyboard: ')
    
def first(c, coin):
    if c not in 'ht':
        print("You aren't following the rules. I don't want to play anymore.")
        print("Bye!")
    else:
        if coin == c:
            print('O gosh you start!')
            nextPlay = next('player')
            return 'player', nextPlay
        else:
            print("That's good! I am lucky!")
            nextPlay = next('cpu')
            return 'cpu', nextPlay

def next(firstTurn):
    if firstTurn == 'player':
        nextTurn = 'cpu'
    if firstTurn == 'cpu':
        nextTurn = 'player'
    return nextTurn

def printBoard(board):
    print('{:^3}{}{:^3}{}{:^3}'.format(board['topL'], '|', board['topM'], '|', board['topR']))
    #print(board['topL'] + '|' + board['topM'] + '|' + board['topR'])
    print('-' * 11)
    print('{:^3}{}{:^3}{}{:^3}'.format(board['midL'], '|', board['midM'], '|', board['midR']))
    #print(board['midL'] + '|' + board['midM'] + '|' + board['midR'])
    print('-' * 11)
    print('{:^3}{}{:^3}{}{:^3}'.format(board['lowL'], '|', board['lowM'], '|', board['lowR']))
    #print(board['lowL'] + '|' + board['lowM'] + '|' + board['lowR'])

def turn(turn):
    if turn == 'player':
        print('-' * 65)
        print('Where do you wanna play?')
        print('You can choose: topL, topM, topR, midL, midM, midR, lowL, lowM, lowR')
        while True:
            try:
                position = input('So what do you choose? ')
                positionList.remove(position)
                break
            except ValueError:
                while ValueError:
                    print('.-.' * 18)
                    print("This position was already chosen. Pick another one.")
                    print('.-.' * 18)
                    break
        p = True
        c = False
    if turn == 'cpu':
        print('-' * 65)
        print("Hmm... You're a very smart guy.")
        print("Let me think")
        print('.')
        time.sleep(1)
        print('.')
        time.sleep(1)
        print('.')
        time.sleep(1)
        position = random.choice(positionList)
        positionList.remove(position)
        #if positionList == []:
        #    winner()
        #    sys.exit()
        print("My choice is " + position + ': ')
        c = True
        p = False
    return position, p, c

def move(position, player, cpu):
    if player == True:
        theboard[position] = 'X'
    if cpu == True:
        theboard[position] = 'O'
    return theboard[position]

def winner():
    playerWin = False
    cpuWin = False
    draw = True
    values = list(theboard.values())
    for i in range(0, 7, 3):
        if (values[i] == values[i+1]) and (values[i+1] == values[i+2]):
            if values[i] == 'X':
                playerWin = True
                cpuWin = False
                draw = False
            if values[i] == 'O':
                cpuWin = True
                playerWin = False
                draw = False
    for i in range(3):
        if (values[i] == values[i+3]) and (values[i+3] == values[i+6]):
            if values[i] == 'X':
                playerWin = True
                cpuWin = False
                draw = False
            if values[i] == 'O':
                cpuWin = True
                playerWin = False
                draw = False
    for i in range(0, 3, 2):
        if i == 0:
            if (values[i] == values[i+4]) and (values[i+4] == values[i+8]):
                if values[i] == 'X':
                    playerWin = True
                    cpuWin = False
                    draw = False
                if values[i] == 'O':
                    cpuWin = True
                    playerWin = False
                    draw = False
        if i == 2:
            if (values[i] == values[i+2]) and (values[i+2] == values[i+4]):
                if values[i] == 'X':
                    playerWin = True
                    cpuWin = False
                    draw = False
                if values[i] == 'O':
                    cpuWin = True
                    playerWin = False
                    draw = False
    return playerWin, cpuWin, draw

def winnerMessage(pWin, cWin):
    if pWin == True:
        print('*+*' * 18)
        print("You have won the game! That's why you are my master!")
        print('*+*' * 18)
    if cWin == True:
        print('*+*' * 18)
        print("I have won the game! The creation beats its creator!")
        print('*+*' * 18)

positionList = list(theboard.keys())
menu()
choice, face = start()
firstTurn, nextTurn = first(choice, face)
while positionList:
    pWin, cWin, draw = winner()
    if (pWin == True) or (cWin == True):
        break
    position1, p1, c1 = turn(firstTurn)
    move(position1, p1, c1)
    printBoard(theboard)
    pWin, cWin, draw = winner()
    if (pWin == True) or (cWin == True):
        break
    if (positionList == []) and (pWin == False) and (cWin == False) and (draw == True):
        print('*+*' * 18)
        print("It's a draw!")
        print('*+*' * 18)
        sys.exit()
    position2, p2, c2 = turn(nextTurn)
    move(position2, p2, c2)
    printBoard(theboard)
    # When the winner happens in the last round it shows the draw message (kinda workind know, maybe it's better to make another function to put inside the loop)
winnerMessage(pWin, cWin)
