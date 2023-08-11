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
