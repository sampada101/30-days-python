from flask import Flask, render_template, redirect, url_for, request, session, g
import pymongo
from datetime import timedelta


class Db:

    def __init__(self, client_code, dbname, collection):
        self.client = pymongo.MongoClient(client_code)
        self.db = self.client[dbname]
        self.collection = self.db[collection]

    def insert(self, fname, lname, email, password):
        self.get()
        if len(self.ids) >= 1:
            user_id = self.ids[-1] + 1
        else:
            user_id = 1
        user = {'id': user_id, 'first': fname, 'last': lname, 'email': email, 'pass':password}
        self.collection.insert_one(user)

    def get(self):
        users = self.collection.find({})
        self.ids = []
        self.fnames = []
        self.lnames = []
        self.emails = []
        self.passwords = []
        for i in users:
            self.ids.append(i['id'])
            self.lnames.append(i['last'])
            self.fnames.append(i['first'])
            self.emails.append(i['email'])
            self.passwords.append(i['pass'])

    def delete(self, user_id):
        self.collection.delete_one({"id": user_id})
        self.manage()

    def update(self, user_id, fname, lname, email):
        self.collection.update_one({'id': user_id}, {"$set": {'first': fname, 'last': lname, 'email': email}})

    def manage(self):
        user_id = 1
        for user in self.collection.find({}):
            self.collection.update_one(user, {'$set': {'id': user_id}})
            user_id += 1


app = Flask(__name__)
app.permanent_session_lifetime = timedelta(days=5)
app.secret_key = YOURSECRETKEY
db = Db(CLUSTERCODE, DBNAME, COLLECTIONNAME)


@app.before_request
def before():
    if 'user_id' in session:
        g.user = session['user_id']


@app.route('/', methods=['GET', 'POST'])
def index():
    db.get()
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        if email in db.emails:
            if password == db.passwords[db.emails.index(email)]:
                session.permanent = True
                session['user_id'] = db.ids[db.emails.index(email)]
                return redirect(url_for('profile'))
            else:
                return """<html>
            <body>

            <script>
              alert("Invalid Email or Password");
              location.replace("/")
            </script>

            </body>
            </html>"""
        else:
            return """<html>
    <body>

    <script>
      alert("Invalid Email or Password");
      location.replace("/")
    </script>

    </body>
    </html>"""
    if 'user_id' in session:
        return redirect(url_for('profile'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    if 'user_id' in session:
        session.pop('user_id')
    return redirect(url_for('index'))


@app.route('/profile')
def profile():
    try:
        if 'user_id' in session:
            db.get()
            return render_template('profile.html', fname=db.fnames[db.ids.index(g.user)])
        return redirect(url_for('index'))
    except:
        return redirect(url_for('add'))


@app.route('/admin')
def admin():
    db.get()
    return render_template('index.html', lnames=db.lnames, fnames=db.fnames, ids=db.ids, emails=db.emails)


@app.route('/signup', methods=['POST', 'GET'])
def add():
    if 'user_id' in session:
        return redirect(url_for('profile'))
    db.get()
    if request.method == "POST":
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        password = request.form.get('password')
        if email in db.emails:
            return """<html>
    <body>

    <script>
      alert("Email already registered");
      location.replace("/")
    </script>

    </body>
    </html>"""
        db.insert(fname, lname, email, password)
        return redirect(url_for('index'))

    return render_template('add.html')


@app.route('/delete', methods=['POST'])
def delete():
    user_id = int(request.form.get('id'))
    db.delete(user_id)
    return redirect(url_for('index'))


@app.route('/update', methods=['POST'])
def update():
    user_index = db.ids.index(int(request.form.get('id')))
    return render_template('update.html', fname=db.fnames[user_index], lname=db.lnames[user_index],
                           id=int(request.form.get('id')), email=db.emails[user_index])


@app.route('/updatevalue', methods=['POST'])
def updatevalue():
    user_id = int(request.form.get('id'))
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')
    db.update(user_id, fname, lname, email)
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run()
