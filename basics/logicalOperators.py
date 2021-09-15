# LOGICAL OPERATORS - AND, OR, NOT


temp = int(input("What's the temperature outside?: "))

if not(temp >= 0 and temp <= 30):
    print("The temperature is currently: " + str(temp) + " today.")
    print("You can go out today!!")
elif not(temp < 0 or temp > 30):
    print("The temperature is bad today!!")