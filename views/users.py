from flask import Flask, render_template, request, Blueprint, session, url_for, redirect
from models.user import User, UserErrors


item_blueprint = Blueprint('users', __name__)


@item_blueprint.route('/register', methods =['GET', 'POST'])
def new_item():
    if request.method == 'POST':
        email = request.form['email']
        passw = request.form['password']
        try:
            User.register_user(email, passw)
            session['email'] = email # save session
        except UserErrors.UserError as e:
            return e.mssage

    return render_template('users/register.html')