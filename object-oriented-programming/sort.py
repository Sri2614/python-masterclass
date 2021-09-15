# sort() method - used with lists
# sort() function - used with iterables

# student = ["Sri","Vid","Anish","Soni","Gnana"]

# student.sort(reverse=True)

# student = ("Sri","Vid","Anish","Soni","Gnana")

# sorted_students = sorted(student,reverse=True)

# for i in sorted_students:
#     print(i)

# students = [("Sri","M",23),
#             ("Vid","A",22),
#             ("Anish","K",25),
#             ("Gnana","F",23)]


# grade = lambda grades:grades[1]
# ages = lambda ages:ages[2]
# students.sort(key=ages,reverse=True)

students = (("Sri","M",23),
            ("Vid","A",22),
            ("Anish","K",25),
            ("Gnana","F",23))


ages = lambda ages:ages[2]
sorted_students = sorted(students,key=ages)

for i in sorted_students:
    print(i)













