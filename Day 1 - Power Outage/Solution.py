# cook your dish here

# getting input
rr1 = float(input())
batsmanStriker, batsmanNonStriker = map(int, input().split())
listScores = list(map(str,input().split()))
rr2 = float(input())

# TASK TWO :- Calculate the BALLS(b) and RUNS(r)
for i in range(len(listScores)):
    if listScores[i]=='W':
        listScores[i] = '-2'

# converting the string to int values
listScores = list(map(int,listScores))

# calculate the sum
sumScore = 0
for i in listScores:
    if i != -2:
        sumScore += i 

# calculate the balls and runs
balls = (rr2 * len(listScores) - 6 * sumScore) / (rr1 - rr2)
runs = rr1 * balls / 6

# TASK THREE :- Calculating the TOTAL SCORE
totalScore = int(runs + sumScore)

# TASK FOUR :- Calculate the each BATSMAN score
checkBatsman1 = True
checkBatsman2 = False
checkOver = int(balls % 6)

# logic
for i in range(len(listScores)):

    if checkBatsman1 is True:
        if listScores[i] == -2:
            batsmanStriker = 0
        else:
            batsmanStriker += listScores[i]

    if checkBatsman2 is True:
        if listScores[i] == -2:
            batsmanNonStriker = 0
        else:
            batsmanNonStriker += listScores[i]

    checkOver += 1

    if listScores[i]%2 != 0:
        if checkBatsman1 is True:
            checkBatsman1 = False
            checkBatsman2 = True
        else:
            checkBatsman1 = True
            checkBatsman2 = False

    if checkOver==6:
        if checkBatsman1 is True:
            checkBatsman1 = False
            checkBatsman2 = True

        else:
            checkBatsman1 = True
            checkBatsman2 = False
        
        checkOver = 0

# printing the final output
print(totalScore,end=" ")

if checkBatsman1 is True:
    print(batsmanStriker,end=" ")
    print(batsmanNonStriker)
else:
    print(batsmanNonStriker,end=" ")
    print(batsmanStriker)
