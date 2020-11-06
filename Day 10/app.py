from flask import Flask, render_template, request, redirect

app = Flask(__name__)
names = []


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        names.append(name)
        return redirect('/')
    return render_template('index.html', names=names)


if __name__ == "__main__":
    app.run()
