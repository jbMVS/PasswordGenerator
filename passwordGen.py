import random
import string

# create variable for each kind of character
charsLower = string.ascii_lowercase
charsUpper = string.ascii_uppercase
charsNums = string.digits
charsPunct = """~`!@#$%^&*()_-+={[}]|\:;"'<,>.?/""" # parentheses order: """ " '' " """ , if you need to include single and double quotes in a string

# create a list of all possibilities, to pick from randomly
possiblilities = [charsLower, charsUpper, charsNums, charsPunct]

# get input, check if it's a number, and that it's greater than 8
inputMatch = False
while inputMatch == False:
    count = input('How long do you want your password? (must be 8 chars or greater)\n')
    if not count.isdigit(): # isdigit() returns a boolean based on if a string variable is a number, i.e. True or False
        print("You must enter a number")
    elif int(count) < 8:
        # would error if user entered a non-integer, but the 'elif' makes sure this only occurs if the first 'if' fails
        # (count is actually a string here, so we compare the int() type instead)
        print("You must enter 8 or higher")
    else:
        # occurs if neither of the first if statements apply
        inputMatch = True

# generate password the length of input number, with at least 1 each of lowercase, uppercase, numbers, and punctuation
needsMet = False
while needsMet == False:
    
    hasLower = False
    hasUpper = False
    hasNums = False
    hasPunct = False
    
    output = ""

    # iterate through the amount entered in user input (count)
    for char in range(int(count)):
        charPick = possiblilities[random.randint(0, 3)] # selects a random character type from possibilities variable
        output = output + charPick[random.randint(0, (int(len(charPick)) - 1))] # adds a random possibility from the selected character type to output

    # iterate through the output, checking if each type of character exists
    for char in output: 
        if char in charsLower:
            hasLower = True
        if char in charsUpper:
            hasUpper = True
        if char in charsNums:
            hasNums = True
        if char in charsPunct:
            hasPunct = True
    
    # if every 'has' char boolean has been set to True, set needsMet to True, which exits the while loop
    # if NOT every char boolean has been set to True, the while loop will continue, generating a new password until all needs are met
    if (hasLower == True) and (hasNums == True) and (hasPunct == True) and (hasUpper == True):
        needsMet = True

# print the generated password
print("Generated password: " + output)