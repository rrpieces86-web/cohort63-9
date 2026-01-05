student = {
    "name": "reece",
    "age": 39,
    "school": "oregon state",
    "degree": "computer science"
}
print(student)
print(student["age"])
student["graduation_year"] = 2028
print(student)
student.pop("graduation_year")
print(student)
student["age"] = 21
print(student)