inputString = input("Enter a your full name: ")
lastNameFirstLetterIndex = int(inputString.index(" ")+1)
initial = inputString[0] + inputString[lastNameFirstLetterIndex]
print(initial.upper())