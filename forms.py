from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import InputRequired, DataRequired

class AddUserForm(FlaskForm):
    """New User Form"""
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])

class UserForm(FlaskForm):
    """Existing User"""

    # firstname = StringField("First Name", validators=[InputRequired()])
    # namename = StringField("Last Name", validators=[InputRequired()])
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])

class WorkoutForm(FlaskForm):
    """Workout Post to li"""
    text = StringField("Workout Post", validators=[InputRequired()])

class MessageForm(FlaskForm):
    """Form for sharing post"""

    text = TextAreaField('text', validators=[DataRequired()])