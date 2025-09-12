# print 1 to n odd numbers

n = int(input("enter n value : "))
i = 1
while  i <= n:
    if not(i%2 == 1):
        i += 1 
        continue
    print(i)
    i += 1