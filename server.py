from flask import Flask, render_template, request, flash, session, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy

from model import connect_to_db, db
#import crud

app = Flask(__name__)
app.secret_key = "test-key"



@app.route('/')
def show_homepage():
    """Shows homepage that prompts for login creds"""

    #if user's already logged in, go to landing page
    if 'user_id' in session:
        return redirect('/landing')
    
    return "<p>Hello</p>"


if __name__ == '__main__':
    connect_to_db(app)

    app.run(debug=True, host='0.0.0.0')