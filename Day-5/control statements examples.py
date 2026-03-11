'''
#syntax for forloop

for var in seq:
    #Statements

#seq: list,tuple,set,dict,str,range

Real time examples/codes

products = ['bread','butter','milk','sugar','salt']
for item in products:
    print(item)

products = {'bread':30,'butter':50,'milk':20,'sugar':45,'salt':60}
for item in products:
    print("Product name:",item)
    print("Product Price:",products[item])
    print("Buy Now | Add to cart")
    print("Add to fav")
    print("--------------------")

s='python programming'
for ch in s:
    print(ch)

Syntax of range

range(start,stop+1,step) = (0,step+1,1)


for i in range(1,11):
    print(i)


printing a table

n=int(input("Enter the number: "))
for i in range(1,21):
      print(f"{n}*{i}={n*i}")


breaking  a statement

for i in range(10):
    if i == 5:
        break
    print(i)


contiue a statement

for i in range(10):
    if i ==5:
        continue
    print(i)


for i in range(10):
    if i ==15:
        continue
    print(i)
else:
    print("Enter of the numbers")
'''

pin=1234
for i in range(5):
    user_pin=int(input("Enter the pin: "))
    if user_pin == pin:
        print("Login successful")
        break
    else:
        print("Invalid password, Try again")
else:
    print("You have reached the max attempts, try again after 5 mins")
