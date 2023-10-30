from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()

bcrypt = Bcrypt()


def connect_db(app):
    db.app = app
    db.init_app(app)

class Workout(db.Model):
    __tablename__ = "workout"
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    text = db.Column(db.Text, 
                     nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', backref="workouts")


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    username = db.Column(db.Text,
                         nullable=False,
                         unique=True)

    password = db.Column(db.Text,
                         nullable=False)
    
    # email = db.Column(db.Text,
    #                    nullable=False,
    #                    unique=True,

    @classmethod
    def register(cls, username, password):
        """Register user with hashed pwd and return user"""

        hashed = bcrypt.generate_password_hash(password)

        # turn bytestring into normal unicode utf8 string
        hashed_utf8 = hashed.decode("utf8")

        # return instance of user with username and hashed pwd
        return cls(username=username, password=hashed_utf8)

    @classmethod
    def authenticate(cls, username, password):
        """Validate that user exists and password is correct
        
        Return user if valid; else return False
        """

        u = User.query.filter_by(username=username).first()

        if u and bcrypt.check_password_hash(u.password, password):
            # return user instance

            return u
        else:
            return False