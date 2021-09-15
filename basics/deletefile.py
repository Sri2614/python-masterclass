import os 
import shutil

path = "D:\\Python\\Python_cache"

try:
    # os.remove(path) - Deletes files
    # os.rmdir(path) - Deletes folder which are empty
    shutil.rmtree(path)
except FileNotFoundError:
    print("The file is not Found")
except PermissionError:
    print("You don't have permission to delete this")
except OSError:
    print("You can't delete a folder with files")
else:
    print("The folder is removed")