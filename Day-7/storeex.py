products = [
    "Rice", "Wheat Flour", "Sugar", "Milk", "Eggs (12 pcs)", 
    "Cooking Oil", "Tea Powder", "Salt", "Bread", "Soap"
]
prices = [60, 45, 40, 25, 70, 130, 90, 20, 30, 25]

print("------- Welcome to Grocery Store -------")
print("Here are the available products:\n")

print('Index'.ljust(6,' '),'Products'.ljust(15,' '),'Price'.ljust(6,' '))
for i in range(10):
    print(str(i+1).ljust(6,' '),products[i].ljust(15,' '),str(prices[i]).ljust(6,' '))

items=list(map(int,input("Enter the indexes: ").split()))

print("Selected Items: ")
total_amount=0
for item in items:
    print(products[item-1],prices[item-1])
    total_amount+= prices[item-1]


print("Total Amount to Pay: ")
print("Thank you for shopping with us!: ")
