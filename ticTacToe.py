'''This is a simple TicTacToe game. You will play against the computer. If you have any doubts about the code you can contact me. Currently the computer plays randomcly, I will try to implement a AI soon, stay tunned ;)'''
import random
import time
import sys

'''The dictionary bellow stores the position and what is inside of it.'''
theboard = {'topL': '', 'topM': '', 'topR': '',
            'midL': '', 'midM': '', 'midR': '',
            'lowL': '', 'lowM': '', 'lowR': ''}

def start():
    '''This function simulates a flip of a coin to determine who will start playing.'''
    option = input()
    faceCoin = random.choice('ht')
    return option, faceCoin

def menu():
    '''This function shows the menu messages.'''
    print('+' * 65)
    print('Hello, this is the Tic Tac Toe Game!')
    print('Do you think you can beat an intelligent computer like me?')
    print("Let's the God of Luck decide who will start!")
    print('Do you want heads or tails? Type "h" or "t" in the keyboard: ')
    
def first(c, coin):
    '''This function verifies who won the coin flip.'''
    if c not in 'ht':
        print("You aren't following the rules. I don't want to play anymore.")
        print("Bye!")
    else:
        if coin == c:
            # If the player won, the function next receives the parameter 'player' to determine that cpu will play next.
            print('O gosh you start!')
            nextPlay = next('player')
            return 'player', nextPlay
        else:
            # If the cpu won, the function next receives the parameter 'cpu' to determine that the player will play next.
            print("That's good! I am lucky!")
            nextPlay = next('cpu')
            return 'cpu', nextPlay

def next(firstTurn):
    '''This function return who will play next, the player or the cpu.'''
    if firstTurn == 'player':
        nextTurn = 'cpu'
    if firstTurn == 'cpu':
        nextTurn = 'player'
    return nextTurn

def printBoard(board):
    '''This function shows to the player the board with the marks in the positions that were chosen.'''
    print('{:^3}{}{:^3}{}{:^3}'.format(board['topL'], '|', board['topM'], '|', board['topR']))
    print('-' * 11)
    print('{:^3}{}{:^3}{}{:^3}'.format(board['midL'], '|', board['midM'], '|', board['midR']))
    print('-' * 11)
    print('{:^3}{}{:^3}{}{:^3}'.format(board['lowL'], '|', board['lowM'], '|', board['lowR']))

def turn(turn):
    '''This function took the position that the player or the cpu choose to play.'''
    if turn == 'player':
        print('-' * 65)
        print('Where do you wanna play?')
        print('You can choose: topL, topM, topR, midL, midM, midR, lowL, lowM, lowR')
        while True:
            # In case the player chooses an invalid position, or one that was have already been chosen the block try/except/else solve this problem.
            try:
                # When the player chooses a position, it will be removed from the available positions in the list.
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
        # The cpu chooses a random position available in the positionList
        position = random.choice(positionList)
        # When the cpu chooses a position, it will be removed from the available positions in the list.
        positionList.remove(position)
        print("My choice is " + position + ': ')
        c = True
        p = False
    return position, p, c

def move(position, player, cpu):
    '''This function assigns the X or the O in the correct position in theboard dictionary either if the player or the cpu make a move.'''
    if player == True:
        theboard[position] = 'X'
    if cpu == True:
        theboard[position] = 'O'
    return theboard[position]

def winner():
    '''This function determines the winner and return it.'''
    playerWin = False
    cpuWin = False
    draw = True
    values = list(theboard.values())
    # The for loop bellow verifies each line of the board to recognize if there is a line with X or O in all the positions.
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
    # The for loop bellow verifies each collumn of the board to recognize if there is a collumn with X or O in all the positions.
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
     # The for loop bellow verifies each diagonal of the board to recognize if there is a diagonal with X or O in all the positions.
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
    '''This function shows the message for the winner.'''
    if pWin == True:
        print('*+*' * 18)
        print("You have won the game! That's why you are my master!")
        print('*+*' * 18)
    if cWin == True:
        print('*+*' * 18)
        print("I have won the game! The creation beats its creator!")
        print('*+*' * 18)

def play():
    '''This function calls the other functions inside a loop until a winner or draw condition happen.'''
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
    winnerMessage(pWin, cWin)

'''This is the main part of the file. It will call all the functions to make the code run properly'''
positionList = list(theboard.keys())
menu()
choice, face = start()
firstTurn, nextTurn = first(choice, face)
play()
