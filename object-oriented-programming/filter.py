# filter() - It creates a collection of elements from an iterable for which a function returns True

# filter(function, iterable)


friends = [("Sri",13),
            ("Vid",12),
            ("Anish",25),
            ("Gnana",23)]

age = lambda data: (data[1] <= 18)

teenage = list(filter(age, friends))

for i in teenage:
    print(i)