import os


#variáveis

html_tag = """<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="css/style.css" rel="stylesheet">
  <title>Document</title>
</head>

<body>


</body>
<script src="js/script.js"></script>

</html>"""

#funções

def changedir():
    path = input("Digite o diretório que deseja criar o projeto: ")
    os.chdir(path)

def makefolders():
    os.mkdir('css')
    os.mkdir('js')

def createstatic():
    path = os.getcwd()
    with open(path+"\js\script.js","w") as js:
        js.write('alert("File has been linked")')
    open(path+"\css\style.css","w")

def create_html():
    with open("index.html","w") as index:
        index.write(html_tag)
    print ("INDEX HAS BEEN CREATED")
  
def web_projects():
    changedir()
    makefolders()
    create_html()
    createstatic()


# funcao principal

def main():
    web_projects()


if __name__=='__main__':
    main()

