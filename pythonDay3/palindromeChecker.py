inputString = input("Enter a string: ")
reverse = inputString[ : :-1]
if(inputString==reverse):
    print("palindrome")
else:
    print("not palindrome")