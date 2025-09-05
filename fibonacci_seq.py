N = int(input("enter the value"))
a, b = 0, 1
seq = []
for _ in range(N) :
    seq.append(a)
    a, b = b, a + b
    print(seq)