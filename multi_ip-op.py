#example4: taking multiple inputs in a single line 
#question: expected input: 10 20 30
#          expected output: "sum of inputs:60"

a = input("enter multiple numbers :")
x,y,z=a.split(" ")
sum = int(x)+int(y)+int(z)

print("sum of inputs:",sum,sep="")