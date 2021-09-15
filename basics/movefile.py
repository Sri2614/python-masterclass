import os 

source = "D:\\Python\\PythonMasterclass\\test.txt"

dest = "D:\\Python\\mv.txt"


try:
    if os.path.exists(dest):
        if os.path.isfile(dest):
            print("The file exists already")
        elif os.path.isdir(dest):
            print("The folder exists already")
    else: 
        os.replace(source,dest)
        print("File is moved to the destination")
except FileNotFoundError:
    print(source+ " was not found")