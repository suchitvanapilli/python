#upper case

rows = 10
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '*' * (2 * i - 1))
#lower case

rows = 10
for i in range(rows, 0, -1):
    print(' ' * (rows - i) + '*' * (2 * i - 1))