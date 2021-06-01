import shutil
import os

input_file = 'unzip_me_for_instructions.zip'
output_dir = 'output_dir'
shutil.unpack_archive(input_file, output_dir, 'zip')
for folder, sub_folders, files in os.walk(os.getcwd()+'/'+output_dir):
    for file in files:
        f = open(f'{folder}/{file}', 'r')
        content = f.read()
        f.close()