from model import User, Appointment, connect_to_db, db
from datetime import datetime


def create_user(name, email, date=datetime.now()):
    """Create and return a User object"""

    return User(name=name, email=email, created_date=date)

def create_appointment(user_id, date_time):
    """Create and return an Appointment object"""

    return Appointment(user_id=user_id, date_time=date_time)

def get_user_by_email(email):
    """Gets user obj by given email address"""

    return User.query.filter(User.email == email).first()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)