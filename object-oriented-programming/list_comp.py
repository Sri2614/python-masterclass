# List comprehension - It is a way to create a new list with less syntax
# It can mimic lambda functions, easier to read
# list = [expression for item in iterable]
# list = [expression for item in iterable if conditions]
# list = [expression if/else for item in iterable]


sqares = []

for i in range(1,11):
    sqares.append(i * i)
print(sqares)

sqares = [i*i for i in range(1,11)]
print(sqares)


students = [100,90,80,70,60,40,20,10,0]

passed_students = list(filter(lambda x: x >=60, students ))

print(passed_students)

# pass_students = [i for i in students if i>=60]

pass_students = [i if i>=60 else "FAILED" for i in students ]
print(pass_students)