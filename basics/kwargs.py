# **kwargs - Parameter that will pack all arguments into a dictionary. Function can accept varying amount of keyword arguments

def hello(**kwargs):
    # print("Hello "+ kwargs['first'] + " "+ kwargs['last'] + " " + kwargs['middle'])
    print("Hello", end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")

hello(title="Mr.",first="Sri",middle="B.B", last="Balaji",nick="Cloud")