#the program will sort files in a particular folder based on their extension
import os 
import shutil
# the directory path which should be sorted
path = 'C:/Users/amos/Downloads'
# create  a well organized list for the folder
content = os.listdir(path)
#loop through all elements within the list
for files in content:
    name, ext = os.path.splitext(files)
    #get the extension type 
    ext = ext[1:]
    if ext == '':
        continue 
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+files, path+'/'+ext+'/'+files)
    #make a directory if there is no existing directory
    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+files, path+'/'+ext+'/'+files)