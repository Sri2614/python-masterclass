#  lambda function - function written in 1 line using lambda keyword
# accepts any number of arguments, but only has one expression

# lambda parameters:expression

double = lambda x: x * 2
multiply = lambda x,y: x * y
add = lambda x,y,z: x+y+z
full_name = lambda first_name, last_name: first_name + " "+last_name
age_check = lambda age: True if age >= 18 else False
  
print(full_name("sri","balaji"))
print(add(3,5,6))
print(double(4))
print(multiply(5,6))
print(age_check(22))