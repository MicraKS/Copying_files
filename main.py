import os
import shutil


path = 'D:/thisTest/'
path2 = 'D:/test2/'
os.chdir(path)
for i in os.listdir(path):
    os.chdir(path)
    if os.path.isfile(i):
        shutil.copy2(i, path2)
    elif os.path.isdir(i):
        folder = os.path.basename(r'D:/thisTest/' + i)
        os.chdir(path2)
        os.mkdir(folder)
        for i in os.listdir(path + folder):
            os.chdir(path + folder)
            z = path2 + folder
            shutil.copy2(i, z)

