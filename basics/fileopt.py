# Read a file

try:
    with open("D:\\Python\\PythonMasterclass\\test.txt") as file:
        print(file.read())

except FileNotFoundError as e:
    print(e)

#  Write a file

text = "Learning to write in a file using Python\n Bro Code Kudos to you man!!!"

# with open("D:\\Python\\PythonMasterclass\\test.txt", 'w') as file:
#     file.write(text)

# with open("D:\\Python\\PythonMasterclass\\test.txt", 'a') as file:
#     file.write(text)


