import os 
import shutil

def get_files():
    folder = os.getcwd()
    list = os.listdir(folder)
    file = []
    for i in list:
        if os.path.isfile(i):
            file.append(i)
    return file

def get_filetypes(list):
    filetypes = []
    for i in list:
        if i.split(".")[-1] not in filetypes:
            filetypes.append(i.split(".")[-1])
    return filetypes

def create_folders():
    folders = get_filetypes(get_files())
    for i in folders:
        if os.path.exists(i):
            pass
        else:
            os.mkdir(i)
    return folders

def movefiles():
    files = get_files()
    for i in files:
        if os.path.exists(i.split(".")[-1]):
            if os.path.exists(os.path.join(i.split(".")[-1],i)):
                pass
            shutil.move(i,i.split(".")[-1])
    return "files moved"

def main():
    create_folders()
    movefiles()

    return "DONE"




if __name__ == "__main__":
    main()
    
