students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    students[name] = marks

print("\nStudent Details:")
for name, marks in students.items():
    print(name, ":", marks)

total_marks = sum(students.values())
average = total_marks / n

topper = max(students, key=students.get)
top_marks = students[topper]

print("\nSummary Report")
print("Average Marks:", average)
print("Topper:", topper)
print("Highest Marks:", top_marks)
