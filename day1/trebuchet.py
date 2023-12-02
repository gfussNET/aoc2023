count = 0

inputFile = open( 'input.txt', 'r')

lines = inputFile.readlines()


for line in lines:
    numbers = []
    #this is gross, but for part 2, find 'words' that are numbers and replace them.  Words truncated as input has overlap potential e.g. twooneight
    line = line.replace('one','o1e').replace('two','t2o').replace('thr','3').replace('four','4').replace('fiv','5').replace('six','6').replace('seven','7').replace('igh','8').replace('nin','9')
    
    for char in line:
        if char.isdigit():
            numbers.append(char)
    
    if len( numbers ) != 1:
        twoDigitNum = int(numbers[0] + numbers[-1])
        count += twoDigitNum
    else: #single entry so double it
        twoDigitNum = int(numbers[0] + numbers[0])
        count += twoDigitNum

print(f'Count is: ', count)

    

