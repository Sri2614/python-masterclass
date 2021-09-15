import os

location = "C:\\Users\\sribalaji.b\\Desktop\\AWS"

if os.path.exists(location):
    print("This location exists!!!")
    if os.path.isfile(location):
        print("That is a file")
    elif os.path.isdir(location):
        print("That is a directory!!")
else:
    print("The location doesn't exist")