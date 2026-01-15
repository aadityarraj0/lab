marks = []
for i in range(6):
    value = int(input(f"Enter marks for subject {i+1}:"))
    marks.append(value)
swapped = True
n = len(marks)
swapped = False
for i in range(n-1):
    for j in range(n-i-1):
        if marks[j] < marks[j+1]:
            marks[j], marks[j+1] = marks[j+1], marks[j]
            swapped = True
    if not swapped:
        break


print("\nMarks from highest to lowest: ")
for k in marks:
    print(k)