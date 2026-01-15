name = input("Enter your name: ")
year = int(input("Enter your year of birth: "))

current_year = 2025
age = current_year - year

print("Name:", name)
print("Age:", age)

if age >= 60:
    print("You are a Senior Citizen")
else:
    print("You are not a Senior Citizen")
