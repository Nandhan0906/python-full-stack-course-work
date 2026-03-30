'''
n=int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        print('000000',end=' ')
    print()

'''
'''
n = int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        print(str(row) * 5, end=' ')
    print()
'''
n = int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        print(col, end=' ')
    print()
