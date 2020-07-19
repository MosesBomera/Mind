# forms.py
# Configures the application forms.

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField
from wtforms.validators import DataRequired, InputRequired, Email, NumberRange, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),
                                            InputRequired()])
    password = PasswordField('Password', validators=[DataRequired(),
                                            InputRequired()])

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),
                                            InputRequired()])
    age = IntegerField('Age', validators=[NumberRange(min=14)])
    email = StringField('Email', validators=[Email()])
    password = PasswordField('Password', validators=[DataRequired(),
                                            InputRequired()])

    message = "The two passwords must be the same."
    repeat_password = PasswordField('Repeat Password', validators=[DataRequired(),
                                                        InputRequired(),
                                                        EqualTo(password, message=message)])
