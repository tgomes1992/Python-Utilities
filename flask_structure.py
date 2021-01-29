import os

#arquivo para criar projetos  básicos em flask 

def changedir():
    path = input("Digite o diretório que deseja criar o projeto: ")
    os.chdir(path)


def makefolders():
    os.mkdir('static')
    os.mkdir('templates')


def create_app():
    app = open("app.py","w")
    line = ["import os\n","from flask import Flask,",
            "render_template,request,redirect,url_for,jsonify\n",
            "from flask_sqlalchemy import SQLAlchemy\n",
            "import sys\n","app = Flask(__name__)\n",
            "#create the app config, including the database data\n",
            "#templates folder for html, static for css an js files\n",
            "migrate = Migrate(app, db)\n"]
    for lines in line:
        app.write(lines)

def main():
   changedir()
   makefolders()
   create_app()


if __name__ == "__main__":
    main()

