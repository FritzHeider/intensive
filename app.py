from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import os
from bson.objectid import ObjectId
from datetime import datetime

host = os.environ.get('MONGODB_URI', 'mongodb://heroku_j31466sd:74ishojt4v09mjpreg0qkhgnf4@ds237308.mlab.com:37308/heroku_j31466sd')
#host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/home')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()
#db = client.TinyHomeMe
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



# app.py
if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
