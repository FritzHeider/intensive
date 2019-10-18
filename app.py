from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import os
from bson.objectid import ObjectId
from datetime import datetime


client = MongoClient()
db = client.TinyHomeMe
users = db.users


app = Flask(__name__)

# users = [
#     { 'title': 'Cat phone', 'email': 'Cats acting weird' },
#     { 'title': '80\'s Music', 'email': 'Don\'t stop believing!' }
# ]

@app.route('/admin')
def users_index():
    """Show all users."""
    return render_template('users_index.html', users=users.find())



@app.route('/info')
def info():
    """Show all users."""
    return render_template('home.html')


@app.route('/users/new')
def users_new():
    """Show all users."""
    return render_template('users_new.html')

@app.route('/users', methods=['POST'])
def users_submit():
    """Submit a new user."""
    user = {
        'title': request.form.get('title'),
        'description': request.form.get('description'),
        'phone': request.form.get('phone')
    }
    users.insert_one(user)
    return redirect(url_for('users_index'))
