import os
from pathlib import Path

def name_changer(name, direc_name):
    direc_name = Path(direc_name)
    dir_files = os.listdir(direc_name)

    for i in range(len(dir_files)):
        new_name = name
        file = dir_files[i]
        src_file = os.path.join(direc_name, file)
        _, ext = file.split(".")

        new_name = new_name + str(i) + "."
        filename = new_name + ext

        dst_file = os.path.join(direc_name, filename)
   
        os.rename(src_file, dst_file)

def directory_files_comparer():
    direc_name1 = Path(str(input("Enter directory1: ")))
    direc_name2 = Path(str(input("Enter directory2: ")))

    dir1_files = os.listdir(direc_name1)
    dir2_files = os.listdir(direc_name2)
    dir1_filenames = []
    dir2_filenames = []

    for i in dir1_files:
        name, _ = i.split(".")
        dir1_filenames.append(name)

    for i in dir2_files:
        name, _ = i.split(".")
        dir2_filenames.append(name)

    absent_files = []

    for i in dir2_filenames:
        if i not in dir1_filenames:
            absent_files.append(i)
    
    return absent_files