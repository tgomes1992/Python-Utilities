import os

def changedir():
    path = input("Digite o diretório que deseja criar o projeto: ")
    os.chdir(path)

def makefolders():
    os.mkdir('css')
    os.mkdir('js')

def createjs():
    path = os.getcwd()
    open(path+"\css\style.css","w")

def createcss():
    path = os.getcwd()
    open(path+"\js\script.js","w")

def createindex():
    open("index.html","w")


def main():
    changedir()
    createindex()
    makefolders()
    createcss()
    createjs()

if __name__=='__main__':
    main()

