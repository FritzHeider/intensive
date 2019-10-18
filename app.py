from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import os
from bson.objectid import ObjectId
from datetime import datetime


client = MongoClient()
db = client.TinyHomeMe
users = db.users


app = Flask(__name__)




@app.route('/')
def home():
    """Show all users."""
    return render_template('home.html', msg='Tine Home me!' )


@app.route('/users', methods=['POST'])
def users_submit():
    """Submit a new user."""
    user = {
        'title': request.form.get('title'),
        'description': request.form.get('description'),
        'videos': request.form.get('videos').split()
    }
    users.insert_one(user)
    return redirect(url_for('users_index'))


@app.route('/users/new')
def users_new():
    """Create a new user."""
    return render_template('users_new.html')


if __name__ == '__main__':
    app.run(debug=True)
