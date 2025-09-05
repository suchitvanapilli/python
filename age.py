#Write a program that takes a person's age as input and categorizes them as "Child" (0-12), "Teenager" (13-19), "Adult" (20-59), or "Senior" (60 and above)."""


age = int(input())

if age >= 0 and age <= 12:
    category = "Child"
elif age >= 13 and age <= 19:
    category = "Teenager"
elif age >= 20 and age <= 59:
    category = "Adult"
elif age >= 60:
    category = "Senior"
else:
    category = "Invalid age"

print("Category:", category)

