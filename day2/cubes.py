
inputFile = open( 'input.txt', 'r')

lines = inputFile.readlines()

#tracking summation of valid game IDs
validGames = 0
cubePowerSum = 0

for line in lines:
    
    # Each game has several sets
    gameID = line.split(": ")[0].split(" ")[-1]

    gameResults = line.split(": ")[1].split("; ")
    blueQty = []
    redQty = []
    greenQty = []
    for cubes in gameResults:

        colors = cubes.split(", ")
        
        validGame = 1

        greenValid = 1
        redValid = 1
        blueValid = 1
        


        for color in colors:
            cubeQuantity, cubeColor = color.split(" ")
       
            cubeColor = cubeColor.strip()
            #check if any violations
            if( cubeColor == "green" and int(cubeQuantity) > 13):
                greenValid = 0
            if( cubeColor == "red" and int(cubeQuantity) > 12):
                redValid = 0
            if( cubeColor == "blue" and int(cubeQuantity) > 14):
                blueValid = 0
            
            #part 2 - building lists and then finding max
            if( cubeColor == "blue" ):
                blueQty.append(int(cubeQuantity))
            if( cubeColor == "red" ):
                redQty.append(int(cubeQuantity))
            if( cubeColor == "green" ):
                greenQty.append(int(cubeQuantity))

        
        if( blueValid == 0 or greenValid == 0 or redValid == 0):
            validGame = 0
            #removing break for Part2
            #break #this draw violated restrictions so even if other draws in same game do not, next to move to next game and test again

        #print(f'Cubes drawn: {cubes} - {validGame}')    
        
    
    #Part 1 - which games would have been possible if bag only had 12 red, 13 green and 14 blue
    if( validGame == 1 ):
        #print(f'Counting Game ID: {gameID}')
        validGames += int(gameID)
    print(f'Colors for GameID {gameID}: blue{blueQty}, red{redQty}, green{greenQty}') 
    cubePower = max(blueQty) * max(redQty) * max(greenQty)
    print(f'Cube Power for Game ID {gameID} is {cubePower}')
    cubePowerSum += cubePower
    #print(f'GameID: {gameID} - Valid Game?: {validGame} - GameID Count: {validGames}')
    #wait = input("checking.....")
                
#print(f'Part 1 - summation of valid game Game IDs: {validGames}' )
print(f'Part 2 - summation of cube powers: {cubePowerSum}')
    