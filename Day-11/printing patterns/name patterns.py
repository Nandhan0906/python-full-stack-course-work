def draw_letter(char, n):
    for row in range(n):
        for col in range(n):
            mid = n // 2
            
            if char == 'P':
                if col == 0 or (row == 0 or row == mid) and col < n-1 or (col == n-1 and row < mid):
                    print('*', end=' ')
                else: print(' ', end=' ')
            

            elif char == 'R':
                if col == 0 or (row == 0 or row == mid) and col < n-1 or (col == n-1 and row < mid) or (row == col and row > mid):
                    print('*', end=' ')
                else: print(' ', end=' ')

            elif char == 'U':
                if (col == 0 or col == n-1) and row < n-1 or (row == n-1 and col > 0 and col < n-1):
                    print('*', end=' ')
                else: print(' ', end=' ')

            elif char == 'D':
                if col == 0 or (row == 0 or row == n-1) and col < n-1 or (col == n-1 and row > 0 and row < n-1):
                    print('*', end=' ')
                else: print(' ', end=' ')

            elif char == 'H':
                if col == 0 or col == n-1 or row == mid:
                    print('*', end=' ')
                else: print(' ', end=' ')

            elif char == 'V':
                if (row == col // 2 and col < n // 2) or (row == (n - 1 - col) // 2 and col >= n // 2):
                    print('*', end=' ')
                elif col == row or col == n - 1 - row: 
                     print('*', end=' ')
                else: print(' ', end=' ')

            elif char == 'I':
                if row == 0 or row == n-1 or col == mid:
                    print('*', end=' ')
                else: print(' ', end=' ')

            elif char == ' ':
                print(' ', end=' ')
            
            else:
                if row == 0 or row == n-1 or col == 0 or col == n-1:
                    print('?', end=' ')
                else: print(' ', end=' ')
        print() 
user_input = input("Enter your name: ").upper()
size = 7 
for letter in user_input:
    print(f"\n--- {letter} ---")
    draw_letter(letter, size)