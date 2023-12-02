
inputFile = open( 'input.txt', 'r')

lines = inputFile.readlines()

#tracking summation of valid game IDs
validGames = 0

for line in lines:
    
    # Each game has several sets
    gameID = line.split(": ")[0].split(" ")[-1]

    gameResults = line.split(": ")[1].split("; ")

    for cubes in gameResults:

        colors = cubes.split(", ")
        
        cubeCountGreen = 0
        cubeCountRed = 0
        cubeCountBlue = 0
        
        validGame = 1

        greenValid = 1
        redValid = 1
        blueValid = 1
        

        for color in colors:
            cubeQuantity, cubeColor = color.split(" ")

            cubeColor = cubeColor.strip()
            #add up sum of thse cubes drawn
            if( cubeColor == "green" and int(cubeQuantity) > 13):
                #cubeCountGreen += int(cubeQuantity)
                greenValid = 0
            if( cubeColor == "red" and int(cubeQuantity) > 12):
                #cubeCountRed += int(cubeQuantity)
                redValid = 0
            if( cubeColor == "blue" and int(cubeQuantity) > 14):
                #cubeCountBlue += int(cubeQuantity)
                blueValid = 0
        
        if( blueValid == 0 or greenValid == 0 or redValid == 0):
            validGame = 0
            break #this draw violated restrictions so even if other draws in same game do not, next to move to next game and test again

        print(f'Cubes drawn: {cubes} - {validGame}')    
         
    
    #Part 1 - which games would have been possible if bag only had 12 red, 13 green and 14 blue
    if( validGame == 1 ):
        print(f'Counting Game ID: {gameID}')
        validGames += int(gameID)
   
    #print(f'GameID: {gameID} - Valid Game?: {validGame} - GameID Count: {validGames}')
    #wait = input("checking.....")
                
print( validGames )
    