import math
import sys

''' *****************************************
# def startGame()
#
# Gives the start command on wheather the player
# will play the game or not
#
# Author :  David Castellanos-Bentio
***************************************** '''
def startGame():
    # Gives the start coordinates of the user
    startX = 2
    startY = 13
    # Ask the user if they want to play the game
    response = input("Would you like to play? (Yes or No)")
    # make whatever input was given to the same case and ignore spaces
    response = response.lower().strip()
    # if the response was yes: do this if statement
    if response == "yes":
        print("The game has started")
        # Prints the map
        printMainMap(startX, startY)
        # Calls the function "playGame" to start the game
        playGame(startX, startY)

        # If the response was no: exit the game
    if response == "no" or response == None:
        sys.exit()


''' *****************************************
# def printMainMap()
#
# Prints a map to the user to see where the user is
# currently positioned at given xpos and ypos
# Using a while loop, the map will be created
#
# Author : David Castellanos-Benito
***************************************** '''
def printMainMap(xpos, ypos):
    # dash is the path
    dash = "-"
    # the users obstacal
    wall = "#"
    # Current position of the user
    currentPos = "x"
    finish = "=>"
    # Gives the actual value of the current position (x, y)
    curX = xpos
    curY = ypos
    i = 0
    # Draws the map
    while i < 15:
        # Will draw the first line that is the edge of the map
        if i == 0:
            print(wall * 60)
            i += 1
        # will show the player where the user needs to go by printing the equal sign
        if i == 1:
            # If the user ypos is set to 1,
            # The condition will track the user as well
            if ypos == 1:
                print(wall + (dash * (xpos - 1)) +
                      currentPos + (dash * (58 - xpos) + finish))
            # Otherwise, the program will just print the dash with the equal sign
            else:
                print(wall + dash * 58 + finish)
            # The condition increments at the end of it
            i += 1
        # *** Lose Game ***
        if (i == 6 and (xpos == 6 and ypos == 16)):
            sys.exit()
        # Will draw the last line that is the edge of the map
        if i == 14:
            print(wall * 60)
            break
        # Will print the map with the curret location of the user
        if i == ypos:
            # will always print a wall for the sides, calculate where the current position of the user is and then print another wall
            print(wall + (dash * (xpos - 1)) +
                  currentPos + (dash * (58 - xpos) + wall))
        # Other wise, the map will just print a plain map with dash

        else:
            print(wall + dash * 58 + wall)
        # Increment the loop
        i += 1
    # print a statement to the user to let them know where the current position is
    print("You are currently here, in the x position. ")
    # Prints coordinates for the user
    print("X:{} Y:{}".format(curX, curY))
    return curX, curY


''' *****************************************
# def printUpdatedMap()
#
# Prints an updated map with the current position of the user
# Given the x and y of the user
# A map will be printed to show the player where they are currently located
# and where they need to go. 
#
# Author : David Castellanos-Benito
***************************************** '''
def printUpdatedMap(xpos, ypos):

    walls = [
        # row 0
        [4, 7, 11, 12, 27, 37, 57],
        # row 1
        [2, 5, 9, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 29, 30, 31, 32, 33,
         34, 35, 36, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56],
        # row 2
        [2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 23, 25, 27, 29, 36, 45, 58],
        # row 3
        [10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 25, 27, 29, 28, 29, 30, 31, 32,
         33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 46, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57],
        # row 4
        [1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 23, 25, 26, 27, 37, 44, 46, 51, 57],
        # row 5
        [8, 9, 10, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 29,
         30, 31, 32, 34, 37, 46, 47, 48, 49, 51, 53, 54, 55, 57],
        # row 6
        [2, 4, 5, 6, 8, 23, 24, 25, 26, 27, 28, 29,
         34, 41, 42, 43, 44, 45, 46, 51, 52, 53, 57],
        # row 7
        [2, 4, 8, 10, 12, 21, 24, 31, 32, 33,
         34, 35, 36, 37, 38, 39, 55, 56, 57],
        # row 8
        [2, 4, 7, 8, 10, 12, 14, 15, 16, 17, 18, 19,
         20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
        # row 9
        [2, 4, 5, 8, 10, 12, 14, 18, 22, 26, 30, 33, 34, 35,
         36, 37, 39, 41, 42, 43, 44, 45, 47, 48, 49, 50, 51, 58],
        # row 10
        [2, 5, 6, 8, 10, 12, 16, 20, 24, 28, 32, 33, 45, 47, 52],
        # row 11
        [2, 3, 5, 8, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 35, 36, 37, 39, 40, 41, 42, 43, 45, 46, 47, 49, 50, 51, 52, 54, 55, 56, 57],
        # row 12
        [3, 10, 12, 13, 35, 43, 47, 54]
    ]

    # *** Functionality ***
    # dash is the path
    dash = "-"
    # the users obstacal
    wall = "#"
    # Current position of the user
    currentPos = "x"
    finish = "=>"
    row = wall
    # Gives the actual value of the current position (x, y)
    curX = xpos
    curY = ypos
    i = 0
    # Draws the map
    while i < 15:
        # Will draw the first line that is the edge of the map
        if i == 0:
            print(wall * 60)
            i += 1
        # *** First row
        # Draws the first line of the map
        if i == 1:
            # set value of x to 1, not 0 or else the map will extend more by 1
            x = 1
            # loop x to print the row
            # row contains 58 items (2 of them are the edges)
            while x < 60:
                # if the value of x (x coordinate) is in the first list of walls,
                if x in walls[0]:
                    # Add a wall string to the row string
                    row += wall
                    # increment x by 1 to matina everything smooth
                    x += 1
                    # continue with the loop again
                    continue
                # if the y value of the player is the same as i (so same as the row)
                if ypos == i:
                    # if the x value of the player is the same x (so same as the column)
                    if xpos == x:
                        # print the current location of the player
                        row += currentPos
                        # increment the value of x
                        x += 1
                        # contniue with the loop and skipp the rest of the conditional statements
                        continue
                        # if the value of x is in walls[0] (first list)
                        if x in walls[0]:
                            # add a wall to the row which would be next to the player
                            row += wall
                            # add 1 to x
                            x += 1
                            continue
                # if the value of x reaches 59 (the 59th column)
                if x == 59:
                    # add the finish line (or wall for the edge for other rows)
                    row += finish
                    # break from the loop
                    break
                # otherwise, add a dash to the row
                else:
                    row += dash
                # increment x by 1 (incrementing column)
                x += 1
            # print the row after finishing the loop
            print(row)
            # increment i by 1 (row)
            i += 1
        # *** Second Row
        if i == 2:
            x = 1
            row = wall
            while x < 60:
                if x in walls[1]:
                    row += wall
                    x += 1
                    continue
                if ypos == i:
                    if xpos == x:
                        row += currentPos
                        x += 1
                        continue
                        if x in walls[1]:
                            row += wall
                            x += 1
                            continue
                if x == 59:
                    row += wall
                    break
                else:
                    row += dash
                x += 1
            print(row)
            i += 1
        # *** 3rd Row
        if i == 3:
            x = 1
            row = wall
            while x < 60:
                if x in walls[2]:
                    row += wall
                    x += 1
                    continue
                if ypos == i:
                    if xpos == x:
                        row += currentPos
                        x += 1
                        continue
                        if x in walls[2]:
                            row += wall
                            x += 1
                            continue
                if x == 59:
                    row += wall
                    break
                else:
                    row += dash
                x += 1
            print(row)
            i += 1
        # *** row 4
        if i == 4:
            x = 1
            row = wall
            while x < 60:
                if x in walls[3]:
                    row += wall
                    x += 1
                    continue
                if ypos == i:
                    if xpos == x:
                        row += currentPos
                        x += 1
                        continue
                        if x in walls[3]:
                            row += wall
                            x += 1
                            continue
                if x == 26:
                    row += "O"
                    x += 1
                    continue
                if x == 59:
                    row += wall
                    break
                else:
                    row += dash
                x += 1
            print(row)
            i += 1
        # *** row 5
        if i == 5:
            x = 1
            row = wall
            while x < 60:
                if x in walls[4]:
                    row += wall
                    x += 1
                    continue
                if ypos == i:
                    if xpos == x:
                        row += currentPos
                        x += 1
                        continue
                        if x in walls[4]:
                            row += wall
                            x += 1
                            continue
                if x == 9:
                    row += "O"
                    x += 1
                    continue
                if x == 59:
                    row += wall
                    break
                else:
                    row += dash
                x += 1
            print(row)
            i += 1
        # *** row 6
        if i == 6:
            x = 1
            row = wall
            while x < 60:
                if x in walls[5]:
                    row += wall
                    x += 1
                    continue
                if ypos == i:
                    if xpos == x:
                        row += currentPos
                        x += 1
                        continue
                        if x in walls[5]:
                            row += wall
                            x += 1
                            continue
                if x == 53:
                    row += "O"
                    x += 1
                    continue
                if x == 59:
                    row += wall
                    break
                else:
                    row += dash
                x += 1
            print(row)
            i += 1
        # *** row 7
        if i == 7:
            x = 1
            row = wall
            while x < 60:
                if x in walls[6]:
                    row += wall
                    x += 1
                    continue
                if ypos == i:
                    if xpos == x:
                        row += currentPos
                        x += 1
                        continue
                        if x in walls[6]:
                            row += wall
                            x += 1
                            continue
                if x == 59:
                    row += wall
                    break
                else:
                    row += dash
                x += 1
            print(row)
            i += 1
        # *** row 8
        if i == 8:
            x = 1
            row = wall
            while x < 60:
                if x in walls[7]:
                    row += wall
                    x += 1
                    continue
                if ypos == i:
                    if xpos == x:
                        row += currentPos
                        x += 1
                        continue
                        if x in walls[7]:
                            row += wall
                            x += 1
                            continue
                if x == 23 or x == 25:
                    row += "O"
                    x += 1
                    continue
                if x == 59:
                    row += wall
                    break
                else:
                    row += dash
                x += 1
            print(row)
            i += 1
        # *** row 9
        if i == 9:
            x = 1
            row = wall
            while x < 60:
                if x in walls[8]:
                    row += wall
                    x += 1
                    continue
                if ypos == i:
                    if xpos == x:
                        row += currentPos
                        x += 1
                        continue
                        if x in walls[8]:
                            row += wall
                            x += 1
                            continue
                if x == 59:
                    row += wall
                    break
                else:
                    row += dash
                x += 1
            print(row)
            i += 1
        # *** row 10
        if i == 10:
            x = 1
            row = wall
            while x < 60:
                if x in walls[9]:
                    row += wall
                    x += 1
                    continue
                if ypos == i:
                    if xpos == x:
                        row += currentPos
                        x += 1
                        continue
                        if x in walls[9]:
                            row += wall
                            x += 1
                            continue
                if x == 59:
                    row += wall
                    break
                else:
                    row += dash
                x += 1
            print(row)
            i += 1
        # *** row 11
        if i == 11:
            x = 1
            row = wall
            while x < 60:
                if x in walls[10]:
                    row += wall
                    x += 1
                    continue
                if ypos == i:
                    if xpos == x:
                        row += currentPos
                        x += 1
                        continue
                        if x in walls[10]:
                            row += wall
                            x += 1
                            continue
                if x == 46:
                    row += "O"
                    x += 1
                    continue
                if x == 59:
                    row += wall
                    break
                else:
                    row += dash
                x += 1
            print(row)
            i += 1
        # *** row 12
        if i == 12:
            x = 1
            row = wall
            while x < 60:
                if x in walls[11]:
                    row += wall
                    x += 1
                    continue
                if ypos == i:
                    if xpos == x:
                        row += currentPos
                        x += 1
                        continue
                        if x in walls[11]:
                            row += wall
                            x += 1
                            continue
                if x == 6:
                    row += "O"
                    x += 1
                    continue
                if x == 59:
                    row += wall
                    break
                else:
                    row += dash
                x += 1
            print(row)
            i += 1
        # *** row 13
        if i == 13:
            x = 1
            row = wall
            while x < 60:
                if x in walls[12]:
                    row += wall
                    x += 1
                    continue
                if ypos == i:
                    if xpos == x:
                        row += currentPos
                        x += 1
                        continue
                        if x in walls[12]:
                            row += wall
                            x += 1
                            continue
                if x == 14 or x == 55:
                    row += "O"
                    x += 1
                    continue
                if x == 59:
                    row += wall
                    break
                else:
                    row += dash
                x += 1
            print(row)
            i += 1

        if i == 14:
            print(wall * 60)
            break
        if i == ypos:
            # will always print a wall for the sides, calculate where the current position of the user is and then print another wall
            print(wall + (dash * (xpos - 1)) +
                  currentPos + (dash * (58 - xpos) + wall))
        # Increment the loop
        i += 1
    return xpos, ypos


''' *****************************************
# def moveUp(y)
#
# given y
# the user will move up by 1
#
# Author: David Castellanos-Benito
***************************************** '''
def moveUp(x, y):
    # subtracts 1 from y to move up
    y -= 1
    # The user will be prompted with this message when they hit
    # the top edge
    # The player will not be allowed to move into the wall
    if y == 0:
        print("!" * 5)
        print("You hit a wall!")
        print("!" * 5)
        y += 1
    # If the function "blocks" is true
    # That means that there is a wall in the direction they want to go
    # and cannot walk into the wall
    if blocks(x, y) == True:
        y += 1
    # returns a new value
    return y


''' *****************************************
# def moveDown(y)
#
# Given y
# the user will move down by 1
#
# Author: David Castellanos-Benito
***************************************** '''
def moveDown(x, y):
    # adds 1 to y to move down
    y += 1
    # The user will be prompted with this message when they hit
    # the bottom edge
    # The player will not be allowed to move into the wall
    if y == 14:
        print("!" * 5)
        print("You hit a wall!")
        print("!" * 5)
        y -= 1
    # If the function "blocks" is true
    # That means that there is a wall in the direction they want to go
    # and cannot walk into the wall
    if blocks(x, y) == True:
        y -= 1
    # Returns a new y value
    return y


''' *****************************************
# def moveR(x) = control("D")
#
# Given x and y
# the user will move to the right by 1
#
# Author: David Castellanos-Benito
***************************************** '''
def moveR(x, y):
    # adds 1 to x to move right
    x += 1
    # The user will be prompted with this message when they hit
    # the right edge
    # The player will not be allowed to move into the wall
    if y == 1 and x == 59:
        return x
    elif y > 1 and x == 59:
        print("!" * 5)
        print("You hit a wall!")
        print("!" * 5)
        x -= 1
    # If the function "blocks" is true
    # That means that there is a wall in the direction they want to go
    # and cannot walk into the wall
    if blocks(x, y) == True:
        x -= 1
    # returns a new x
    return x


''' *****************************************
# def moveL(x)
#
# Given x
# the user will move to the left by 1
#
# Author: David Castellanos-Benito
***************************************** '''
def moveL(x, y):
    # subtracts 1 from x to move right
    x -= 1
    # The user will be prompted with this message when they hit
    # the left edge
    # The player will not be allowed to move into the wall
    if x == 0:
        print("!" * 5)
        print("You hit a wall!")
        print("!" * 5)
        x += 1
    # If the function "blocks" is true
    # That means that there is a wall in the direction they want to go
    # and cannot walk into the wall
    if blocks(x, y) == True:
        x += 1
    # Returns a new x
    return x


''' *****************************************
#  def moveSystem(x, y)
#
# Given x and y
# The program will ask the user for one of the following inputs
# After the user gives one of the following inputs
# The input will change to become all lowercase to measure the samething
# Depending on the the user input, a new function will be called to have the user move that
#
# Author: David Castellanos-Benito
***************************************** '''
def moveSystem(x, y):
    # The player will be prompted with this question everytime after a move
    moveUser = input(
        "Please type an input to move\n( A || W || S || D )\nWould you like to see an updated map? Type: \n(map)\nWould you like to Exit? Type : \n(exit)\n")
    # Make the input of the user lower case to handle both Upper and lower case
    moveUser = moveUser.lower()
    # If the user types "a"
    # The player will left up by 1
    if moveUser == "a":
        x = moveL(x, y)
    # If the user types "w"
    # The player will move up by 1
    if moveUser == "w":
        y = moveUp(x, y)
    # If the user types "s"
    # The player will up up by 1
    if moveUser == "s":
        y = moveDown(x, y)
    # If the user types "d"
    # The player will right up by 1
    if moveUser == "d":
        x = moveR(x, y)
    if moveUser == "map":
        x, y = printUpdatedMap(x, y)
    # If the player wants to exit the game
    if moveUser == 'exit':
        sys.exit()
    return x, y


''' *****************************************
# def playGame(x, y)
#
# Given x and y
# The game will begin to play
# The game will continue to play until the player
# has reached the finish of the maze
# The Finish is "=", so while the current string is not that
# The player can still keep playing
#
# Author: David Castellanos-Benito
***************************************** '''
def playGame(x, y):
    string = ""
    # The finish line for the player to win
    finish = "="
    # The Game will continue until the player reaches the finsh line
    while string != finish:
        if (y == 4 and x == 26) or (y == 5 and x == 9) or (y == 6 and x == 52) or (y == 8 and (x == 23 or x == 25)) or (y == 11 and x == 46) or (y == 12 and x == 6) or (y == 13 and (x == 14 or x == 15)):
            print("/" * 26)
            print("///   You Lose!        ///\n///Try again next time!///")
            print("/" * 26)
            sys.exit()
        if y == 1 and x == 59:
            string = "="
            print("!" * 20)
            print("Congradulations! You Won!")
            print("!" * 20)
            # Add more to the command prompt to congradulate the player on winning.
            sys.exit()
        # Calling the function "moveSystem", the return values will be set for x and y
        x, y = moveSystem(x, y)
        # A new map is printed with the new coordinate points
        printMainMap(x, y)


''' *****************************************
# def blocks(x, y)
#
# Given x and y
# The function will determine if the move that
# the user wants to make is a wall or not
# The program has various list that represent the X-coordinates of each row
# x will always be checked if the value is in the same list depending on the y
#
# Author: David Castellanos-Benito
***************************************** '''
def blocks(x, y):
    # Set the state to False
    state = False
    # X Coordinates for row 1 (when y = 1)
    r1 = [4, 7, 11, 12, 27, 37, 57]
    # X Coordinates for row 2 (when y = 2)
    r2 = [2, 5, 9, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 29, 30, 31, 32, 33,
          34, 35, 36, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56]
    # X Coordinates for row 3 (when y = 3)
    r3 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 23, 25, 27, 29, 36, 45, 58]
    # X Coordinates for row 4 (when y = 4)
    r4 = [10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 25, 27, 29, 28, 29, 30, 31, 32,
          33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 46, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57]
    # X Coordinates for row 5 (when y = 5)
    r5 = [1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 23, 25, 26, 27, 37, 44, 46, 51, 57]
    # X Coordinates for row 6 (when y = 6)
    r6 = [8, 9, 10, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 29,
          30, 31, 32, 34, 37, 46, 47, 48, 49, 51, 53, 54, 55, 57]
    # X Coordinates for row 7 (when y = 7)
    r7 = [2, 4, 5, 6, 8, 23, 24, 25, 26, 27, 28, 29,
          34, 41, 42, 43, 44, 45, 46, 51, 52, 53, 57]
    # X Coordinates for row 8 (when y = 8)
    r8 = [2, 4, 8, 10, 12, 21, 24, 31, 32, 33,
          34, 35, 36, 37, 38, 39, 55, 56, 57]
    # X Coordinates for row 9 (when y = 9)
    r9 = [2, 4, 7, 8, 10, 12, 14, 15, 16, 17, 18, 19,
          20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
    # X Coordinates for row 10 (when y = 10)
    r10 = [2, 4, 5, 8, 10, 12, 14, 18, 22, 26, 30, 33, 34, 35,
           36, 37, 39, 41, 42, 43, 44, 45, 47, 48, 49, 50, 51, 58]
    # X Coordinates for row 11 (when y = 11)
    r11 = [2, 5, 6, 8, 10, 12, 16, 20, 24, 28, 32, 33, 45, 47, 52]
    # X Coordinates for row 12 (when y = 12)
    r12 = [2, 3, 5, 8, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
           30, 31, 32, 33, 35, 36, 37, 39, 40, 41, 42, 43, 45, 46, 47, 49, 50, 51, 52, 54, 55, 56, 57]
    # X Coordinates for row 13 (when y = 13)
    r13 = [3, 10, 12, 13, 35, 43, 47, 54]

    # checks if y (row)
    if (y == 1 and (x in r1)) or (y == 2 and (x in r2)) or (y == 3 and (x in r3)) or (y == 4 and (x in r4)) or (y == 5 and (x in r5)) or (y == 6 and (x in r6)) or (y == 7 and (x in r7)) or (y == 8 and (x in r8)) or (y == 9 and (x in r9)) or (y == 10 and (x in r10)) or (y == 11 and (x in r11)) or (y == 12 and (x in r12)) or (y == 13 and (x in r13)):
        state = True

    if state == True:
        print("You Hit a wall! check another way!")
    return state


if __name__ == '__main__':
    startGame()

# y == 0 =>
# y == 1 => x == 4 || x == 7 || x == 11-12 || x == 27 || x == 37 || x == 57 || = == 59
# y == 2 => x == 2 || x == 5 || x == 9 || x == 12 || x == 14-25 || x == 27 || x == 29-37 || x == 39-56
# y == 3 => x == 2-10 || x == 12 || x == 23 || x == 25 || x == 27 || x == 29 || x == 36 || x == 45 || x == 58
# y == 4 => x ==10 || x == 12-21 || x ==23 || x == 25 || O == 26 || x == 27 || x == 29-35 || x == 37-44 || x == 46 || x == 48-57
# y == 5 => x == 1-8 || W == 9 || x == 10 || x == 12 || x == 23 || x == 25-27 || x == 37 || x ==  44 || x == 46 || x == 51 || x == 57
# y == 6 => x == 8-10 || x == 14-23 || x == 29-32 || x == 34 || x == 37 ||  x == 46-49 || x == 51 || W == 52 || x == 53-55 || x == 47
# y == 7 => x == 2 || x == 4-6 || x == 8 || x == 23-29 || x == 34 || x == 41-46 || x == 51-53 || x == 57
# y == 8 => x == 2 || x == 4 || x == 8 || x == 10 || x == 12 || x == 21 || O == 23 || x == 24 || O == 25 || x == 31-39 || x == 55 - 57
# y == 9 => x == 2 || x == 4 || x == 7-8 || x == 10 || x == 12 || x == 14-31
# y == 10 => x == 2 || x == 4-5 || x == 8 || x == 10 || x == 12 || x == 14 || x == 18 || x == 22 || x == 26 || x == 30 || x == 33=37 || x == 39 || x == 41-45 || x == 47-50 || x == 51 == 58
# y == 11 => x == 2 || x == 5-6 || x == 8 || x == 10 || x == 12 || x == 16 || x == 20 || x == 24 || x == 28 || x == 32-33 || x == 45 || W == 46 || x == 47 || x == 52
# y == 12 => x == 2 || x == 3 || x == 5 || O == 6 || x == 8 || x == 10 || x == 12-33 || x == 35-37 || x == 39-43 || x == 45-47 || x == 49-52 || x == 54-57
# y == 13 => x == 3 || x == 10 || x == 12-13 || w == 14 || x == 35 || x == 43 || x == 47 || x == 54 || O ==55

# 15 rows: (0-14)

# W: End Game
# O: End Game
#                                                                58
#        123456789						                          |
# 0 --- ############################################################
# 1 --- #---#--#---##--------------#---------#-------------------#-=>
# 2 --- #-#--#---#--#-############-#-#########-##################--#
# 3 --- #-#########-#----------#-#-#-#-------#--------#-----------##
# 4 --- #---------#-##########-#-#O#-#######-########-#-##########-#
# 5 --- #########W#-#----------#-###---------#------#-#----#-----#-#
# 6 --- #-------###---##########-----####-#--#--------####-#W###-#-#
# 7 --- #-#-###-#--------------#######----#------######----###---#-#
# 8 --- #-#-#---#-#-#--------#-O#O-----#########---------------###-#
# 9 --- #-#-#--##-#-#-##################---------------------------#
# 10--- #-#-##--#-#-#-#---#---#---#---#--#####-#-#####-####-########
# 11--- #-#--##-#-#-#---#---#---#---#---##-----------#W#----#------#
# 12--- #-##-#O-#-#-######################-###-#####-###-####-####-#
# 13--- #-X#------#-##W--------------------#-------#---#------#O---#
# 14--- ############################################################