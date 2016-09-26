#import predefined random integer generator from python

from random import randint 

#create board variable

board = []

#append 5 O's (not zeros) to create board 

for x in range(0, 5):
    board.append(["O"] * 5)

#define function to print board using .join to print the 5 O's from above
#and put a " " space or other defined character between each one

def print_board(board):
    for row in board:
        print " ".join(row)

#define functions to randomly choose and assign integer value, using length of board -1 instead of set value in case we change size of board

def random_row(board):
    return randint (0, len(board) -1)
def random_col(board):
    return randint(0, len(board) -1)

#print output of randomized row/column chosen by functions

#print "row", random_row(board), "column", random_col(board)

#store the random coordinates from above in variables to put ship on board

ship_row = random_row(board)
ship_col = random_col(board)

#DEBUG print output of random placement of ship. ***REMEMBER*** the -1 adjustment means output will display as one less than actual answer location to use regular coordinates instead of python index starting with 0 as 1

#print ship_row
#print ship_col

#Game start

print "----------Welcome to BATTLESHIP----------"
name = raw_input("What is your name?")
print 'Hello, Captain %s.' % name
print "You have 8 guesses to find my battleship on a 5X5 game board shown below"
print_board(board)

#ask for user raw_input to allow player to guess where the ship is using integers added the -1 on each variable below to force coordinates to display properly when placing x on the game board after guesses due to python indexing including 0 as first number
for turn in range(8):
    print "Turn:", (turn+1)
    guess_row = int(raw_input("Guess Row:")) -1
    guess_col = int(raw_input("Guess Col:")) -1

#use if statement to print you win if the input coordinates match the randomly generated ones

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You Sank my battleship! May the legend of Captain 'Deadeye' %s forever decorate the annals of maritime mythology for having destroyed a single ship." % name 
        break

    
#else if the guesses do not match, print you missed then put an X on a displayed game board to show where the miss was located
    
    else:
#check if row/col guessed is within range defined by board size, \ continues next line
        if guess_row not in range(len(board)) or \
            guess_col not in range(len(board)):
            print "Oops, that's not even in the ocean."
        
#Check if x exists on board for the location guessed to avoid guessing same spot
        
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
        if turn == 7:
            print "Game Over. May the world ever remember Captain 'Blindfire' %s, the legendary mismanager of accuracy and ammunition" % name
        print_board(board)
        
#use raw_input to display enter to exit text instead of terminating script without reviewing output
    	
raw_input("Press enter to exit.")