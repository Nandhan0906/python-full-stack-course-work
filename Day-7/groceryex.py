# Product and Price data
products = [
    "Rice", "Wheat Flour", "Sugar", "Milk", "Eggs (12 pcs)", 
    "Cooking Oil", "Tea Powder", "Salt", "Bread", "Soap"
]
prices = [60, 45, 40, 25, 70, 130, 90, 20, 30, 25]

# 1. Display Welcome Message
print("------- Welcome to Grocery Store -------")
print("Here are the available products:\n")

# 2. Display the Product Menu
print(f"{'Index':<8} {'Product':<25} {'Price (Rs.)'}")
for i in range(len(products)):
    print(f"{i+1:<8} {products[i]:<25} {prices[i]}")

print("-" * 40)

# 3. Get User Input
print("\nEnter the product indexes you want to buy (you can repeat indexes)")
user_input = input("Enter indexes: ")

# Convert input string into a list of integers
# We subtract 1 from each index because Python lists start at 0
selected_indexes = [int(x) - 1 for x in user_input.split()]
print(f"[{', '.join(map(str, [x+1 for x in selected_indexes]))}]")

# 4. Generate the Bill
print("\n------- Your Bill -------")
print(f"{'Product':<20} {'Qty':<8} {'Price':<10} {'Total'}")

total_bill = 0
# Use set() to get unique items so we don't print the same product multiple times
unique_selection = []
for idx in selected_indexes:
    if idx not in unique_selection:
        unique_selection.append(idx)

for idx in unique_selection:
    name = products[idx]
    unit_price = prices[idx]
    qty = selected_indexes.count(idx)
    item_total = unit_price * qty
    total_bill += item_total
    
    print(f"{name:<20} {qty:<8} {unit_price:<10} {item_total}")

# 5. Display Final Total
print(f"\nTotal Amount to Pay: Rs. {total_bill}")
print("Thank you for shopping with us!")
