from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Required, Email, Length


class LoginForm(Form):
    email = StringField(
        'Enter email ', validators=[Email(),
                                    Required(),
                                    Length(4, 30)])
    password = PasswordField('Enter password', validators=[Required()])
    remember_me = BooleanField('Remember me? ')
    submit = SubmitField('Login')
