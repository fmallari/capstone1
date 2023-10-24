from flask import Flask, render_template, redirect, session, flash
# from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db, User, Workout
from forms import UserForm, WorkoutForm

app = Flask(__name__)
app.app_context().push()


app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///fitness_frenzy"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "fitness"
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
# toolbar = DebugToolbarExtension(app)

connect_db(app)

##############################################################################
# Register/Login/Logout 

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/profile', methods=["GET", "POST"])
def show_profile():
    if "user_id" not in session:
        flash("Login required")
        return redirect('/login')
    form = WorkoutForm()

    return render_template('profile.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register_user():
    form = UserForm()
    if form.validate_on_submit():
        name = form.username.data
        pwd = form.password.data
        new_user = User.register(name, pwd)

        db.session.add(new_user)
        db.session.commit()
        session['user_id'] = new_user.id

        flash("Welcome! You Have Successfully Created Your Account!")
        return redirect('/profile')

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET','POST'])
def login_user():
    form = UserForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        user = User.authenticate(username, password)
        if user:
            flash(f"Welcome Back, {user.username}!")
            session['user_id'] = user.id
            return redirect('/profile')
        else:
            form.username.errors = ['Invalid username/password']

    return render_template('/login.html', form=form)

@app.route('/logout')
def logout_user():
    session.pop('user_id')
    flash("Successfully logged out")
    return redirect('/')