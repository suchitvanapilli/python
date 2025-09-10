a = input("enter a maths marks: ")
b = input("enter a science marks: ")
c = input("enter a english marks: ")

total = int(a) + int(b) + int(c)
print("Total Marks: ",total)
avg = total/300 *100
print("Average Marks: ",avg)

if avg >= 80:
    print("grade : A")
elif avg >= 50:
    print("grade : B")
elif avg >= 30:
    print("grade : C")
else:
    print("fail")

