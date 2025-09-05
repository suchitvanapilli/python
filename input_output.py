# input statements

name = input()
print(name)

# input with string

name = input("enter your name :")
print("your name is :",name)

# input with datatype

number = int(input("enter a number :"))
print(type(number))


# example

name = input("enter your name :")
age = int(input("enter your age :"))
print("hellow, " + name + "! your are", age , "years old. ")


#multiple inputs

inputs = input("Enter multiple values: ").split()
print(inputs)


# example for string to float conversion 

user_input = input("Enter a number: ")  # Prompt user to enter a number
number = float(user_input)              # Convert the input string to a float
print("The number you entered is:", number)



# output statements

a = int(input("enter a value : "))
b = int(input("enter a value : "))

print(a,b,a,b,sep = "-",end = "ended")

#example

x = 5
y = "apple"
print("i have",x,y)

#example
print("One",end=" ")
print("Two",end=" ")
print("three")