import os


path = os.getcwd()

files = os.listdir(path)

with open("files.csv","w") as csv:
    csv.write("filenames" + "\n")
    for i in files:    
        csv.writelines(i+"\n")





