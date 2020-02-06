from flask import  render_template, flash, redirect
from app import app
from app.forms import RegistrationForm
from app import models

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

# @app.route('/login', methods=['GET','POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
#         return redirect('/index')
#     return render_template('login.html',title='Sign In',form=form)



@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        context = models.User(
        Username=form.Username.data,
        Password=form.Password.data,
        FirstName = form.FirstName.data,
        LastName = form.LastName.data,
        MiddleName =form.MiddleName.data
        )
        context.save()
        return redirect('/index')
    return render_template('auth/register.html',form=form,page='register')
