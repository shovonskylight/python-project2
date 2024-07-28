tshirtPrice = float(input("enter the price of a Tshirt "))
tshirtQuantity = int(input("enter the quantity of tshirt "))
sareePrice = float(input("enter the price of a saree "))
sareeQuantity = int(input("enter the quantity of saree "))

total = tshirtPrice*tshirtQuantity+sareePrice*sareeQuantity
print("the total price = ", round(total,2))