from flask import Flask, render_template, redirect, session, flash
# from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db, User
from forms import UserForm

app = Flask(__name__)
app.app_context().push()


app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///fitness_frenzy"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "fitness"
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
# toolbar = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def home_page():
    return render_template('index.html')