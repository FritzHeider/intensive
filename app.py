from flask import Flask, render_template
from pymongo import MongoClient

client = MongoClient()
db = client.TinyHomeMe
users = db.users


app = Flask(__name__)

users = [
    { 'title': 'Cat Videos', 'description': 'Cats acting weird' },
    { 'title': '80\'s Music', 'description': 'Don\'t stop believing!' }
]
@app.route('/')
def users_index():
    """Show all users."""
    return render_template('users_index.html', users=users.find())

@app.route('/')
def home():
    """Show all users."""
    return render_template('home.html', msg='Flask is Cool!!' )




if __name__ == '__main__':
    app.run(debug=True)
