student = ("Sri", 23, "male")

print(student.count("Sri"))
print(student.index("male"))

for x in student:
    print(x, end=" ")

if "Sri" in student:
    print("Sri is here!!")