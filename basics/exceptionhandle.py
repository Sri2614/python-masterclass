
try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by Zero!!!")
except ValueError as e:
    print(e)
    print("Enter only numbers please!!!")
except Exception:
    print("Something went Wrong!!")

else:
    print("The result is: {}".format(result))

finally:
    print("Finally Code Worked!!!")