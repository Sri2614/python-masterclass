#  Loop Control Statements - Change a loop's execution from its normal sequence

# break - Used to terminate the loop entirely

# continue - skips to the next iteration of the loop

# pass - Does nothing, just acts as a placeholder

while True:
    name = input("Enter your name: ")
    if name != "":
        break 


phone_number = "324-123-4553"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="")


for i in range(1,21):
    if i == 15:
        pass
    else:
        print(i,end="")