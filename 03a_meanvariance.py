numbers = list(map(float, input("Enter numbers separated by space: ").split()))

mean = sum(numbers) / len(numbers)

variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)

std_dev = variance ** 0.5

print("Mean =", mean)
print("Variance =", variance)
print("Standard Deviation =", std_dev)
