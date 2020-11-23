from flask import Flask, render_template, request
from twitter import Twitter

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    name = request.form.get('name')
    password = request.form.get('pass')
    twitter = Twitter(name, password)
    logged_in = twitter.login()
    if not logged_in:
        return """<html>
    <body>

    <script>
      alert("Invalid Username or Password");
      location.replace("/")
    </script>

    </body>
    </html>"""
    return render_template('twitter.html', followers=twitter.followers, name=twitter.name, following=twitter.following, tweet=twitter.tweet, link=twitter.url)


if __name__ == "__main__":
    app.run()
