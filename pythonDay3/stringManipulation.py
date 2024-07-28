inputString = input (("Enter your full name: "))
indexOfSpace = int(inputString.index(" "))
firstName = inputString[0:indexOfSpace:1]
lastName = inputString[indexOfSpace+1: :1]
print(lastName,firstName)
print("total no of character: ", len(inputString))
initial = firstName[0] + lastName[0]
print("initial: ", initial.upper())