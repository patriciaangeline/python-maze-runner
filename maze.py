# Patricia Angeline G. Tan
# 226189
# October 11, 2022

# I have not discussed the Python language code in my program
# with anyone other than my instructor or the teaching assistants
# assigned to this course.

# I have not used Python language code obtained from another student,
# or any other unauthorized source, either modified or unmodified.

# If any Python language code or documentation used in my program
# was obtained from another source, such as a textbook or website,
# that has been clearly noted with a proper citation in the comments
# of my program.

# --------------------
# Function Definitions
# --------------------

# Use functions to produce the appropriate maze depending on the level
def firstLevel(): # Level 1 (Easy): 3x3 grid
    global easyList # Source: https://www.w3schools.com/python/python_variables_global.asp
    easyList = []

    # 1 List = 0
    easyMaze0 = ["Available Directions: South", None, None, 4, None] # Source: http://programarcadegames.com/index.php?chapter=lab_adventure
    easyList.append(easyMaze0)

    # 2 List = 1
    easyMaze1 = ["Available Directions: East South", None, 3, 5, None]
    easyList.append(easyMaze1)

    # 3 List = 2
    easyMaze2 = ["Available Directions: West", None, None, None, 2]
    easyList.append(easyMaze2)

    # 4 List = 3
    easyMaze3 = ["Available Directions: North East South", 1, 5, 7, None]
    easyList.append(easyMaze3)

    # 5 List = 4
    easyMaze4 = ["Available Directions: North East South West", 2, 6, 8, 4]
    easyList.append(easyMaze4)

    # 6 List = 5
    easyMaze5 = ["Available Directions: West", None, None, None, 5]
    easyList.append(easyMaze5)

    # 7 List = 6
    easyMaze6 = ["Available Directions: North", 4, None, None, None]
    easyList.append(easyMaze6)

    # 8 List = 7
    easyMaze7 = ["Available Directions: North East", 5, 9, None, None]
    easyList.append(easyMaze7)

    # 9 List = 8
    easyMaze8 = ["Available Directions: West", None, None, None, 8]
    easyList.append(easyMaze8)

    return easyList[currentLocation][0]


def secondLevel(): # Level 2 (Average) : 4 by 4 grid
    global mediumList
    mediumList = []

    # 1 List = 0
    mediumMaze0 = ["Available Directions: East South", None, 2, 5, None]
    mediumList.append(mediumMaze0)

    # 2 List = 1
    mediumMaze1 = ["Available Directions: East West", None, 3, None, 1]
    mediumList.append(mediumMaze1)

    # 3 List = 2
    mediumMaze2 = ["Available Directions: East West", None, 4, None, 2]
    mediumList.append(mediumMaze2)

    # 4 List = 3
    mediumMaze3 = ["Available Directions: South West", None, None, 8, 3]
    mediumList.append(mediumMaze3)

    # 5 List = 4
    mediumMaze4 = ["Available Directions: North East South", 1, 6, 9, None]
    mediumList.append(mediumMaze4)

    # 6 List = 5
    mediumMaze5 = ["Available Directions: East West", None, 7, None, 5]
    mediumList.append(mediumMaze5)

    # 7 List = 6
    mediumMaze6 = ["Available Directions: South West", None, None, 11, 6]
    mediumList.append(mediumMaze6)

    # 8 List = 7
    mediumMaze7 = ["Available Directions: North", 4, None, None, None]
    mediumList.append(mediumMaze7)

    # 9 List = 8
    mediumMaze8 = ["Available Directions: North South", 5, None, 15, None]
    mediumList.append(mediumMaze8)

    # 10 List = 9
    mediumMaze9 = ["Available Directions: South", None, None, 14, None]
    mediumList.append(mediumMaze9)

    # 11 List = 10
    mediumMaze10 = ["Available Directions: North East South", 7, 12, 15, None]
    mediumList.append(mediumMaze10)

    # 12 List = 11
    mediumMaze11 = ["Available Directions: South West", None, None, 16, 11]
    mediumList.append(mediumMaze11)

    # 13 List = 12
    mediumMaze12 = ["Available Directions: North East", 9, 14, None, None]
    mediumList.append(mediumMaze12)

    # 14 List = 13
    mediumMaze13 = ["Available Directions: North West", 10, None, None, 13]
    mediumList.append(mediumMaze13)

    # 15 List = 14
    mediumMaze14 = ["Available Directions: North", 11, None, None, None]
    mediumList.append(mediumMaze14)

    # 16 List = 15
    mediumMaze15 = ["Available Directions: North", 12, None, None, None]
    mediumList.append(mediumMaze15)

    return mediumList[currentLocation][0]


def thirdLevel(): # Level 3 (Difficult) : 5 by 5 grid
    global difficultList
    difficultList = []

    # 1 List = 0
    difficultMaze0 = ["Available Directions: East South", None, 2, 6, None]
    difficultList.append(difficultMaze0)

    # 2 List = 1
    difficultMaze1 = ["Available Directions: West East", None, 3, None, 1]
    difficultList.append(difficultMaze1)

    # 3 List = 2
    difficultMaze2 = ["Available Directions: West East South", None, 4, 8, 2]
    difficultList.append(difficultMaze2)

    # 4 List = 3
    difficultMaze3 = ["Available Directions: West South", None, None, 9, 3]
    difficultList.append(difficultMaze3)

    # 5 List = 4
    difficultMaze4 = ["Available Directions: South", None, None, 10, None]
    difficultList.append(difficultMaze4)

    # 6 List = 5
    difficultMaze5 = ["Available Directions: North East", 1, 7, None, None]
    difficultList.append(difficultMaze5)

    # 7 List = 6
    difficultMaze6 = ["Available Directions: West South", None, None, 12, 6]
    difficultList.append(difficultMaze6)

    # 8 List = 7
    difficultMaze7 = ["Available Directions: North South", 3, None, 13, None]
    difficultList.append(difficultMaze7)

    # 9 List = 8
    difficultMaze8 = ["Available Directions: North East South", 4, 10, 14, None]
    difficultList.append(difficultMaze8)

    # 10 List = 9
    difficultMaze9 = ["Available Directions: North West", 5, None, None, 9]
    difficultList.append(difficultMaze9)

    # 11 List = 10
    difficultMaze10 = ["Available Directions: East South", None, 12, 16, None]
    difficultList.append(difficultMaze10)

    # 12 List = 11
    difficultMaze11 = ["Available Directions: North East West South", 7, 13, 17, 11]
    difficultList.append(difficultMaze11)

    # 13 List = 12
    difficultMaze12 = ["Available Directions: North West", 8, None, None, 12]
    difficultList.append(difficultMaze12)

    # 14 List = 13
    difficultMaze13 = ["Available Directions: North East", 9, 15, None, None]
    difficultList.append(difficultMaze13)

    # 15 List = 14
    difficultMaze14 = ["Available Directions: West South", None, None, 20, 14]
    difficultList.append(difficultMaze14)

    # 16 List = 15
    difficultMaze15 = ["Available Directions: North South", 11, None, 21, None]
    difficultList.append(difficultMaze15)

    # 17 List = 16
    difficultMaze16 = ["Available Directions: North East", 12, 18, None, None]
    difficultList.append(difficultMaze16)

    # 18 List = 17
    difficultMaze17 = ["Available Directions: West South", None, None, 23, 17]
    difficultList.append(difficultMaze17)

    # 19 List = 18
    difficultMaze18 = ["Available Directions: South", None, None, 24, None]
    difficultList.append(difficultMaze18)

    # 20 List = 19
    difficultMaze19 = ["Available Directions: North South", 15, None, 25, None]
    difficultList.append(difficultMaze19)

    # 21 List = 20
    difficultMaze20 = ["Available Directions: North East", 16, 22, None, None]
    difficultList.append(difficultMaze20)

    # 22 List = 21
    difficultMaze21 = ["Available Directions: West", None, None, None, 21]
    difficultList.append(difficultMaze21)

    # 23 List = 22
    difficultMaze22 = ["Available Directions: North", 18, None, None, None]
    difficultList.append(difficultMaze22)

    # 24 List = 23
    difficultMaze23 = ["Available Directions: North East", 19, 25, None, None]
    difficultList.append(difficultMaze23)

    # 25 List = 24
    difficultMaze24 = ["Available Directions: West North", 20, None, None, 24]
    difficultList.append(difficultMaze24)

    return difficultList[currentLocation][0]

# Initialization of variables
gridInterval = 0
directionInput = ""
validList = ["NORTH", "SOUTH", "EAST", "WEST", "QUIT"]

# Use functions to determine the available directions per space in the maze
def inputDirection():
    global directionInput

    directionInput = input("Which direction will you take? \n").upper()
    return directionInput


def askDirection(gridInterval):
    global currentLocation

    if  == 3:
        for element in easyList:
            if directionInput == "NORTH":
                if easyList[currentLocation][1] == None: #Add-on 2: Handle incorrect input = Unavailable directions
                    print("Please choose an available direction.")
                    print()
                    break
                else:
                    currentLocation -= gridInterval
                break

            if directionInput == "EAST":
                if easyList[currentLocation][2] == None:
                    print("Please choose an available direction.")
                    print()
                    break
                else:
                    currentLocation += 1
                break

            if directionInput == "SOUTH":
                if easyList[currentLocation][3] == None:
                    print("Please choose an available direction.")
                    print()
                    break
                else:
                    currentLocation += gridInterval
                break

            if directionInput == "WEST":
                if easyList[currentLocation][4] == None:
                    print("Please choose an available direction.")
                    print()
                    break
                else:
                    currentLocation -= 1
                break

    if gridInterval == 4:
        for element in mediumList:
            if directionInput == "NORTH":
                if mediumList[currentLocation][1] == None:
                    print("Please choose an available direction.")
                    print()
                    break
                else:
                    currentLocation -= gridInterval
                break

            if directionInput == "EAST":
                if mediumList[currentLocation][2] == None:
                    print("Please choose an available direction.")
                    print()
                    break
                else:
                    currentLocation += 1
                break

            if directionInput == "SOUTH":
                if mediumList[currentLocation][3] == None:
                    print("Please choose an available direction.")
                    print()
                    break
                else:
                    currentLocation += gridInterval
                break

            if directionInput == "WEST":
                if mediumList[currentLocation][4] == None:
                    print("Please choose an available direction.")
                    print()
                    break
                else:
                    currentLocation -= 1
                break

    if gridInterval == 5:
        for element in difficultList:
            if directionInput == "NORTH":
                if difficultList[currentLocation][1] == None:
                    print("Please choose an available direction.")
                    print()
                    break
                else:
                    currentLocation -= gridInterval
                break

            if directionInput == "EAST":
                if difficultList[currentLocation][2] == None:
                    print("Please choose an available direction.")
                    print()
                    break
                else:
                    currentLocation += 1
                break

            if directionInput == "SOUTH":
                if difficultList[currentLocation][3] == None:
                    print("Please choose an available direction.")
                    print()
                    break
                else:
                    currentLocation += gridInterval
                break

            if directionInput == "WEST":
                if difficultList[currentLocation][4] == None:
                    print("Please choose an available direction.")
                    print()
                    break
                else:
                    currentLocation -= 1
                break

# -----------------
# Program Execution
# -----------------

# Greet the player
print("Welcome to the Maze!")

# Ask the player to select a level
levelInput = int(input("Select a level: 1, 2, or 3 \n"))

# Conditionals to determine gridInterval which will affect askDirection(gridInterval)
if levelInput == 1:
    gridInterval += 3
elif levelInput == 2:
    gridInterval += 4
if levelInput == 3:
    gridInterval += 5

# Keep track of the player's current location in the maze
    # Numbered grid starting from 0 - If user input is 1, it refers to 0th element in the list (n-1)
currentLocation = int(input("Starting point: ")) #Add-on 1: Start Elsewhere
currentLocation -= 1

# Keep track of the player's inputted exit location in the maze
    # By default, the exit is the last space, the lower-right corner
exitLocation = int(input("Exit location: ")) # Add-On 3: Start Elsewhere, Exit Elsewhere
exitLocation -= 1
print()

# Repeatedly ask the player for moves, depending on whether the player has made it to the exit or the player has given up
whileCounter = 0
while whileCounter == 0:

    if gridInterval == 3:
        print(firstLevel())
        inputDirection() # Ask for the player's move
        print()

        if directionInput == "QUIT": # When the player gives up, produce the appropriate output
            print("Try again next time.")
            break

        if directionInput not in validList: # Add-On 2: Handle Incorrect Input = Invalid commands
            print("Please choose an available direction.")
            print()

        else:
            askDirection(3) # Determine the change in the player's location within the maze

            if currentLocation == exitLocation: # When the player has reached the exit, produce the appropriate output
                print("Found the exit!")
                break

    if gridInterval == 4:
        print(secondLevel())
        inputDirection()
        print()

        if directionInput == "QUIT":
            print("Try again next time.")
            break

        if directionInput not in validList:
            print("Please choose an available direction.")
            print()

        else:
            askDirection(4)

            if currentLocation == exitLocation:
                print("Found the exit!")
                break

    if gridInterval == 5:
        print(thirdLevel())
        inputDirection()
        print()

        if directionInput == "QUIT":
            print("Try again next time.")
            break

        if directionInput not in validList:
            print("Please choose an available direction.")
            print()

        else:
            askDirection(5)

            if currentLocation == exitLocation:
                print("Found the exit!")
                break

# Before terminating the program, say goodbye.
print("Goodbye.")