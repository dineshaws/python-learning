import os
import shutil


f = open('practice1.txt', mode='w+')
f.write('test content')
f.close()


print(os.getcwd())

print(os.listdir())

print(os.listdir('/home/ongraph/python-workspace/'))

try:
    shutil.move('/home/ongraph/python-workspace/python-learning/practice1.txt','/home/ongraph')
except:
    print('File already exist')

print(os.listdir('/home/ongraph'))

os.unlink('practice1.txt')
'''
NOTE: The os module provides 3 methods for deleting files:
    os.unlink(path) which deletes a file at the path your provide
    os.rmdir(path) which deletes a folder (folder must be empty) at the path your provide
    shutil.rmtree(path) this is the most dangerous, as it will remove all files and folders contained in the path. All of these methods can not be reversed! Which means if you make a mistake you won't be able to recover the file. Instead we will use the send2trash module. A safer alternative that sends deleted files to the trash bin instead of permanent removal.

'''

# Walking through a directory

for folder, sub_folders, files in os.walk('/home/ongraph/python-workspace/python-learning'):
    print(f'Current directory is {folder}')
    print('\n')
    for sub_folder in sub_folders:
        print(f'\t sub directory is {sub_folder}')
    print('\n')
    for file in files:
        print(f'\t file is {file}')
    print('\n')

