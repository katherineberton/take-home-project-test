from flask import Flask, render_template, request, flash, session, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy

from model import connect_to_db, db
import crud

app = Flask(__name__)
app.secret_key = "test-key"



@app.route('/')
def show_homepage():
    """Shows homepage that prompts for login creds"""

    #if user's already logged in, go to landing page
    if 'user_id' in session:
        return redirect('/landing')
    
    return render_template('homepage.html')



@app.route('/login', methods=["POST"])
def log_user_in():
    """Handles login attempts."""

    login_email = request.form.get("email")

    user = crud.get_user_by_email(login_email)

    if user:
        session['user_id'] = user.user_id
        flash(f'Let\'s eat, {user.name}!')
        return redirect('/landing')
    else:
        flash('You have not yet registered.')
        return render_template('homepage.html')



@app.route('/logout')
def log_user_out():
    """Logs user out"""

    session.pop('user_id')
    flash('Have fun at your tasting!')

    return render_template('homepage.html')



@app.route('/landing')
def show_landing():
    """Shows landing page"""

    return render_template('landing.html')



if __name__ == '__main__':
    connect_to_db(app)

    app.run(debug=True, host='0.0.0.0')