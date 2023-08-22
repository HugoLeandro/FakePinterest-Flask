from flask import Flask


app = Flask(__name__)

@app.route("/")
def homepage():
    return "Pinterest"

@app.route("/perfil")
def perfil():
    return "Perfil"

if __name__ == "__main__":
    app.run(debug=True)


