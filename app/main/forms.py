from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required, Email


class NameForm(Form):
    name = StringField('Enter username', validators=[Required()])
    email = StringField('Enter email', validators=[Required(), Email()])
    password = PasswordField('Enter password', validators=[Required()])
    submit = SubmitField('Submit')
