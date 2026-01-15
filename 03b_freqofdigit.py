num = input("Enter a multi-digit number: ")

uniq_digit = set(num)

for elem in uniq_digit:
    print("Digit", elem, "occurs", num.count(elem), "time(s)")

