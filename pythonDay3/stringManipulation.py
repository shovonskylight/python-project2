inputString = input (("Enter your full name: "))
indexOfSpace = int(inputString.index(" "))
firstName = inputString[0:indexOfSpace:1]
lastName = inputString[indexOfSpace+1: :1]
print(lastName,firstName)