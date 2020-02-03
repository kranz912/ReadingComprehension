from flask_wtf import FlaskForm
from wtforms import  StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import  DataRequired, Length, EqualTo

class RegistrationForm(FlaskForm):
    Username = StringField('Username',validators=[DataRequired()])
    Password = PasswordField('Password',validators=[DataRequired(),Length(min=8)])
    Password2 = PasswordField('Confirm Password',validators=[DataRequired(),Length(min=8), EqualTo(Password)])
    FirstName = StringField('First Name',validators=[DataRequired()])
    LastName = StringField('Last Name', validators=[DataRequired()])
    MiddleName = StringField('Middle Name', validators=[DataRequired()])
    submit = SubmitField('Register')
