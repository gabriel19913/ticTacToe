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
            print('+' * 65)
            nextPlay = next('player')
            return 'player', nextPlay
        else:
            print("That's good! I am lucky!")
            print('+' * 65)
            nextPlay = next('cpu')
            return 'cpu', nextPlay

def next(firstTurn):
    if firstTurn == 'player':
        nextTurn = 'cpu'
    if firstTurn == 'cpu':
        nextTurn = 'player'
    return nextTurn

def printBoard(board):
    print(board['topL'] + '|' + board['topM'] + '|' + board['topR'])
    print('-' * 5)
    print(board['midL'] + '|' + board['midM'] + '|' + board['midR'])
    print('-' * 5)
    print(board['lowL'] + '|' + board['lowM'] + '|' + board['lowR'])

def turn(turn):
    if turn == 'player':
        print('-' * 65)
        print('Where do you wanna play?')
        print('You can choose: topL, topM, topR, midL, midM, midR, lowL, lowM, lowR')
        position = input('So what do you choose? ')
        #i = positionList.index(position)
        #chosenList = []
        #chosen = positionList.pop(i)
        #chosenList.append(chosen)
        #if position in chosenList:
        #    print('You already pick this position. Try other one.')
        positionList.remove(position)
        if positionList == []:
            winner()
            sys.exit()
        print(positionList)
        print(chosenList)
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
        #i = positionList.index(position)
        #chosenList = []
        #chosen = positionList.pop(i)
        #chosenList.append(chosenList)
        #if position in chosenList:
        #    print('You already pick this position. Try other one.')
        positionList.remove(position)
        if positionList == []:
            winner()
            sys.exit()
        print(positionList)
        print(chosen)
        print("My choice is " + position + ': ')

        '''
        while theboard.setdefault(position):
            print("That's sad, someone already chose this position.")
            print("A will choose again...")
            if position in positionsList:
                positionsList.remove(position)
            print('.')
            time.sleep(1)
            position = random.choice(positionsList)
            print("My new choice is " + position + ': ')'''
        c = True
        p = False
    return position, p, c

def move(position, player, cpu):
    if player == True:
        theboard[position] = 'X'
    if cpu == True:
        theboard[position] = 'O'
    return theboard[position]


'''
def winner():
    values = list(theboard.values())
    for i in range(0, 7, 3):
        if (values[i] == values[i+1]) and (values[i+1] == values[i+2]):
            if values[i] == 'X':
                print('*+*' * 18)
                print("You have won the game! That's why you are my master!")
                print('*+*' * 18)
            if values[i] == 'O':
                print('*+*' * 18)
                print("I have won the game! The creation beats its creator!")
                print('*+*' * 18)
    for i in range(3):
        if (values[i] == values[i+3]) and (values[i+3] == values[i+6]):
            if values[i] == 'X':
                print('*+*' * 18)
                print("You have won the game! That's why you are my master!")
                print('*+*' * 18)
            if values[i] == 'O':
                print('*+*' * 18)
                print("I have won the game! The creation beats its creator!")
                print('*+*' * 18)
    for i in range(0, 3, 2):
        if i == 0:
            if (values[i] == values[i+4]) and (values[i+4] == values[i+8]):
                if values[i] == 'X':
                    print('*+*' * 18)
                    print("You have won the game! That's why you are my master!")
                    print('*+*' * 18)
                if values[i] == 'O':
                    print('*+*' * 18)
                    print("I have won the game! The creation beats its creator!")
                    print('*+*' * 18)
        if i == 2:
            if (values[i] == values[i+2]) and (values[i+2] == values[i+4]):
                if values[i] == 'X':
                    print('*+*' * 18)
                    print("You have won the game! That's why you are my master!")
                    print('*+*' * 18)
                if values[i] == 'O':
                    print('*+*' * 18)
                    print("I have won the game! The creation beats its creator!")
                    print('*+*' * 18)
'''
positionList = list(theboard.keys())
menu()
choice, face = start()
firstTurn, nextTurn = first(choice, face)
while positionList:
    playerPosition, p, c = turn(firstTurn)
    move(playerPosition, p, c)
    printBoard(theboard) 
    playerPosition, p, c = turn(nextTurn)
    move(playerPosition, p, c)
    printBoard(theboard)
    '''
    for values in theboard.values():
        if theboard.setdefault(values):
            aux = 'end'
    if aux == 'end':
        break'''
    #cpu continua jogando mesmo estando tudo completo
