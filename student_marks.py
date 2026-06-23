# Student Marks Analysis

students = {
    "Arun": 85,
    "Priya": 92,
    "Kaviya": 88,
    "Rahul": 76,
    "Meena": 95
}

total = sum(students.values())
average = total / len(students)

highest = max(students, key=students.get)
lowest = min(students, key=students.get)

print("Student Marks Analysis")
print("----------------------")
print("Average Marks:", average)
print("Highest Scorer:", highest, "-", students[highest])
print("Lowest Scorer:", lowest, "-", students[lowest])
