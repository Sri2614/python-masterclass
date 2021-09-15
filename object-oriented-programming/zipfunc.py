# zip(*iterables) - Aggregate elements from two or more iterables (list,tuples,sets,etc..) 
# Creates a "zip" object with paired elements stored in tuples for each element

usernames = ["Sri", "Balaji", "Virat"]
passwords = ("p@sswoRd", "abc@123", "cricket")

users = dict(zip(usernames,passwords))

for i,y in users.items():
    print(i+' : '+y)

print(type(users))