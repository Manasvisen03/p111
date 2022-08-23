import os
import shutil

list_of_files = os.listdir()
print(list_of_files)
for fileName in list_of_files:
    name,extention=os.path.splitext(fileName)
    print(name)
    print(extention)