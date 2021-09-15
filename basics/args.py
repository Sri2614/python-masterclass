
# *args - Parameter that will pack all arguments into a tuple. So that a function can accept varying amount of arguments

def add(*args):
    sum = 0
    args = list(args)
    args[2] = 8
    for i in args:
        sum+= i
    return sum

print(add(1,2,4))