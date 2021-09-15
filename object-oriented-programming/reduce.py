# reduce() - apply a function to an iterable and reduce it to a single cumulative value

# Performs function on first two elements and repeats process until 1 value remains

#  reduce(function, iterable)

import functools
# letters = ["S","R","I","B","A","L","A","J","I"]

# word = functools.reduce(lambda x, y: x+y,letters)

factorial = [5,4,3,2,1,12]

result = functools.reduce(lambda x,y: x*y,factorial)

print(result)

