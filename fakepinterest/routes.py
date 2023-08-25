# Criar as rotas do nosso site (os links)

from flask import render_template, url_for
from fakepinterest import app, database, bcrypt
from fakepinterest.models import Usuario, Foto
from flask_login import login_required
from fakepinterest.forms import FormLogin, FormCriarConta


@app.route("/", methods=["GET", "POST"])
def homepage():
    formlogin = FormLogin()
    return render_template("homepage.html", form=formlogin)

@app.route("/criarconta", methods=["GET", "POST"])
def criarconta():
    form_criarconta = FormCriarConta()
    if form_criarconta.validate_on_submit():
        senha = bcrypt.generate_password_hash(form_criarconta.senha.data)
        bcrypt.check_password_hash()
        usuario = Usuario(username=form_criarconta.username.data,
                          email=form_criarconta.email.data, senha=senha)
        database.session.add(usuario)
        database.session.commit()
    return render_template("criarconta.html", form=form_criarconta)

@app.route("/perfil/<usuario>")
@login_required
def perfil(usuario):
    return render_template("perfil.html", usuario=usuario)
