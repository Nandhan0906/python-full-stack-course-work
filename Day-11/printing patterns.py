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

'''
n = int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        print(col, end=' ')
    print()
'''
'''
n = int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        if (row + col) % 2 == 0:
            print('0', end='')
        else:
            print('1', end='')
    print() 
''''''
n = int(input("Enter the size: "))
for row in range(n):
    for col in range(row+1):
        print('*', end=' ')
    print()
'''
'''
n = int(input("Enter the size: "))
for row in range(n):
    for col in range(n-row):
        print('*', end=' ')
    print()
'''
'''
n = int(input("Enter the size: "))
for row in range(n):
    for spc in range(n-row-1):
        print(' ', end=' ')
    for col in range(row+1):
        print('*', end=' ')
    print()
'''
'''
n = int(input("Enter the size: "))
for row in range(n):
    for spc in range(row):
        print(' ', end=' ')
    for col in range(n - row):
        print('*', end=' ')
        
    print()
'''
'''
n = int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        if row == 0 or row == n - 1 or col == 0 or col == n - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
'''
'''
n = int(input("Enter the size: "))
mid = n // 2  
for row in range(n):
    for col in range(n):
        if row == 0 or row == n - 1 or col == 0 or col == n - 1:
            print('*', end=' ')
        elif row == mid and col > 0 and col < n - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
'''
'''
n = int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        if row == 0 or row == n - 1 or col == 0 or col == n - 1 or row==n//2 or col==n//2:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
'''
'''
n = int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        if row == 0 or row == n - 1 or (row + col == n - 1):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
'''
'''
n = int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        if row == col or row + col == n - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
'''
