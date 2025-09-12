candies = 10
for i in range(0,candies):
    print("given to frnd")

# exampele 1
message = "Hello, World!"
for i in message:
    print(i)

# example 2
message = "Hello, World!"
length = len(message)
for i in range(length):
    print(i)

# example 3
for i in range(5):
    print(i)

# example 4 
total = 0
for i in range (1,5) :
    total += i 
print(total)

# example 5

words = ["apple", "banana", "cherry"]
for i, word in enumerate(words):
    print(i, word)