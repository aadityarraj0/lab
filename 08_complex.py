class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {-self.imag}i"


def add_complex(c1, c2):
    new_real = c1.real + c2.real
    new_imag = c1.imag + c2.imag
    return Complex(new_real, new_imag)


N = int(input("Enter how many complex numbers you want to add (N >= 2): "))

if N < 2:
    print("Number of complex numbers must be at least 2.")
else:
    print("\nEnter the complex numbers:")

    real = float(input("Enter real part of number 1: "))
    imag = float(input("Enter imaginary part of number 1: "))
    total = Complex(real, imag)

    for i in range(2, N + 1):
        real = float(input(f"Enter real part of number {i}: "))
        imag = float(input(f"Enter imaginary part of number {i}: "))
        current = Complex(real, imag)
        total = add_complex(total, current)

    print("\nThe sum of all complex numbers is:", total)
