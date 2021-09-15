import time

# print(time.ctime(1000000)) # convert a time expressed in seconds since epoch to a readable string
# epoch - When your computer thinks time began(reference point)

# print(time.ctime(time.time()))

# time_object = time.localtime()
# print(time_object)


# local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
# print(local_time)


time_tuple = (2021, 9, 15, 12, 7, 0, 0, 0, 0)
time_string = time.asctime(time_tuple)
print(time_string)

time_tuple = (2021, 9, 15, 12, 7, 0, 0, 0, 0)
time_string = time.mktime(time_tuple)
print(time_string)

