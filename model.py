from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer

db=SQLAlchemy()


class User(db.Model):
    """One user"""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    email = db.Column(db.String(50),
                      nullable=False)
    created_date = db.Column(db.DateTime)
    name = db.Column(db.String(100),
                     nullable=False)

    #appointments = list of Appointment objects under this character

    def __repr__(self):
        return f'<User obj id={self.user_id} name={self.name} email={self.email}>'


class Appointment(db.Model):
    """One appointment"""

    __tablename__ = 'appointments'

    appointment_id = db.Column(db.Integer,
                               autoincrement=True,
                               primary_key=True)
    user_id = db.Column(db.Integer,
                        db.ForeignKey("users.user_id"))
    date_time = db.Column(db.DateTime)

    user = db.relationship('User', backref='appointments')
    
    def __repr__(self):
        return f'<Appointment obj id={self.appointment_id} user={self.user_id}>'

def connect_to_db(app, db_name="melon_tasting_db"):
    """Connect to database."""

    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql:///{db_name}"
    app.config["SQLALCHEMY_ECHO"] = True #try turning this off for debugging
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = app
    db.init_app(app)


if __name__ == '__main__':
    from server import app

    connect_to_db(app)