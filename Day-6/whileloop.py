'''
ini
while condi:
    upd
    #stmts

i=20
while i<=30:
    if i==25:
        continue
    print(i)
    i+=1


bullets = 15
while bullets > 0:
    print(f"{bullets} bullets are left, you can shoot!!")
    bullets -= 1
else:
    print("Game Over")


moves = 30
winning_point = 24
while moves > 0:
    if moves == winning_point:
        print("You win the game!!")
        break
    print(f"{moves} moves are left, you can play!!")
    moves -= 1
else:
    print("Game Over")
'''

data={}
n=int(input("Enter the number of students: "))
for i in range(n):
    name=input("Enter the name: ")
    data[name]=False

for name in data:
    print(name)
    status = int(input(f"Enter the {name} status(0-Absent,1-Present): "))
    data[name] = bool(status)
print(data)
