import os 
import shutil



folder = os.getcwd()

file = os.listdir(folder)

filetypes = []

files = []

for i in file:
    if os.path.isfile(folder + "/"+i):
        files.append(i)    

for i in files:
    if i.split('.')[-1]  not in filetypes:
        filetypes.append(i.split('.')[-1])

for i in filetypes:
    os.mkdir(i)

for i in files:
    shutil.move(folder + "/" + i , folder + "/" + i.split(".")[-1] )






