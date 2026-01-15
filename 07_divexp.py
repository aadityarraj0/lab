def DivExp(a, b):
    assert a > 0, "a must be greater than 0"
    if b == 0:
        raise Exception("b cannot be zero")
    else:
        c = a / b
    return c

a = float(input("Enter a: "))
b = float(input("Enter b: "))

c = DivExp(a, b)
print("Result =", c)
