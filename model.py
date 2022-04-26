from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer

db=SQLAlchemy()




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