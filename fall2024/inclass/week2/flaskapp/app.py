from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index_route():
    return render_template('index.html', posts=posts)

posts = [
    {
        'user': 'chuck',
        'text': 'meow'
    },
    {
        'user': 'nikita',
        'text': 'meow'
    }
]

@app.route('/user/<user>')
def user_route(user):
    user_posts = [post for post in posts if post['user'] == user]
    return render_template('user.html', user=user, user_posts=user_posts)
