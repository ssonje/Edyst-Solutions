# cook your dish here

# list of base values
listBase = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        
# function to convert the number to roman
def NumToRoman(n):

    # logic
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbol = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman_number = ''
    i = 0
    while  n > 0:
        for _ in range(n // values[i]):
            roman_number = roman_number + symbol[i]
            n -= values[i]
        i += 1
    return roman_number

# function the roman letter with max base
def findMaxBase(roman):

    # logic
    max = 0
    for i in range(len(roman)):
        for j in range(len(listBase)):
            if listBase[j]==roman[i] and max<j:
                max = j

    return max

# function to find base index
def findIndex(roman_i):
    for j in range(len(listBase)):
        if listBase[j]==roman_i:
            index = j

    return index

# function to calculate new n
def findNewN(roman,base):

    # calculate the number values from roman
    i = 0
    n = 0
    length = len(roman)
    while length>0:
        n += findIndex(roman[i]) * pow(base,length-1)
        i += 1
        length -= 1

    return n

# function for task
def calculate(n):

    while True:
        if n>=1 and n<=3999:
            roman = NumToRoman(n)

            if len(roman)==1:
                base = findIndex(roman)
            else:
                base = findMaxBase(roman)+1
            
            n_new = findNewN(roman,base)

            n = n_new           
        else:
            break

    return n
    
# take the input from user
n = int(input())

# claculate the o/p
print(calculate(n))
