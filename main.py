import random
from colorama import init,Back
import os
init()
with open('words.txt','r') as f:
    words = f.readlines()
os.system('clear')
word = random.choice(words).strip('\n')
print('Welcome to wordle!\nGuess the word in 6 tries!\nAfter each guess the color of the letters will change\nif it changes to green if it is in the correct spot\nit will change to yellow if the letter is in the word but in the wrong position\nand if it remains the same the color the letter is not in the word.')
def parse_state(char,state):
    if not state:return char
    if state == 'correct':
        return f'{Back.GREEN}{char}{Back.RESET}'
    elif state == 'in':
        return f'{Back.YELLOW}{char}{Back.RESET}'
def check_input(inp):
    if len(inp)!= 5:
        print('Word must be 5 letters long')
        return False
    elif inp in words:
        print('Word not in word list')
        return False
    return True
def ensure_input(msg): 
    while True:
        inp = input(msg)
        if check_input(inp):
            return inp 
board = []

def displayBoard(clear=True):
    if clear:os.system('clear')
    adds = 6-len(board)
    add = [[' ' for _ in range(5)] for _ in range(adds)]
    b = board[:]
    b.extend(add)
    for j in b:
        print('------------')
        print(f'|{j[0]} {j[1]} {j[2]} {j[3]} {j[4]}|',end='')
        print()
        
displayBoard(clear=False)
while True:
    if len(board) == 6:
        print(f'Out of guesses, the word was {word}')
        break
    inp = ensure_input('Enter a word: ')
    if inp == word:
        board.append([parse_state(i,'correct') for i in inp])
        displayBoard()
        print('Well done!')
        break
    bged = {}
    for ind,i in enumerate(list(inp)):
        if not i in bged:
            bged[i] = 0
        if word[ind] == i:
            bged[i]+=1
    inpword = []
    for ind,i in enumerate(list(inp)):
        if not i in bged:
            bged[i] = 0
        if word[ind] == i:
            inpword.append(parse_state(i,'correct'))
            continue
        elif i  in word:
            bged[i]+=1
            print(bged[i],word.count(i))
            if word.count(i)<bged[i]:
                inpword.append(i)
                continue
            inpword.append(parse_state(i,'in'))
        else:
            inpword.append(i)
    board.append(inpword)
    displayBoard()