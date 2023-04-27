import os
import shutil
import pathlib

path = 'D:/thisTest/'
path2 = 'D:/test2/'

def copy_files(path,path2):
    os.chdir(path)
    for i in os.listdir(path):
        if os.path.isfile(i):
            shutil.copy2(i, path2)
def copy_folder(path, path2, files):
    for i in files:
        os.chdir(path2)
        os.mkdir(i)
def search_dir(path):
    example_dir = 'D:/thisTest/'
    dir = pathlib.Path(example_dir)
    files = [file.name for file in dir.iterdir() if file.is_dir()]
    return files

copy_folder(path, path2, search_dir(path))
