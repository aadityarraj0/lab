01a.	Develop a python program to read 2 numbers from the keyboard and perform the basic arithmetic operations based on the choice. (1-Add, 2-Subtract, 3-Multiply, 4-Divide).

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

choice = int(input("Enter choice (1 - Add, 2 - Sub, 3 - Multiply, 4 - Divide): "))

if choice == 1:
    print("Result: ", a+b)
elif choice == 2:
    print("Result: ", a-b)
elif choice == 3:
    print ("Result: ", a*b)
elif choice == 4:
    if b != 0:
        print("Result: ", a/b)
    else:
        print("Division by zero is not allowed.")
else:

    print("Invalid Choice")
