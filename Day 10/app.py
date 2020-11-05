from flask import Flask, render_template, request, redirect

app = Flask(__name__)
names = []


@app.route('/')
def home():
    if len(names) >= 1:
        highlight = names[0]
        other = names.copy()
        other.pop(0)
        return render_template('base.html', names=other, first=highlight, name=True)
    else:
        return render_template('base.html', names=names)


@app.route('/add', methods=['POST'])
def add():
    name = request.form.get('name')
    names.append(name)
    return redirect('/')


if __name__ == "__main__":
    app.run()
