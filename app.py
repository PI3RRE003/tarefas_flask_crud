from flask import Flask

#__name__ = '__main__'
app = Flask(__name__)

@app.route("/")
def hello_word():
    return 'Olá Mundo!'

@app.route("/about")
def about():
    return"Página Sobre"

#APENAS PARA DESENVOLVIMENTO LOCAL
if __name__ == '__main__': 
    app.run(debug=True)
