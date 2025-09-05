#example5: specifying separator in output
#specifying separator in output

#question: expected input: "john",25
#          expected output: "name:john,age:25"

name,age = input("enter name and age: ").split(",")
print("Name:",name,",Age:",age,sep="")