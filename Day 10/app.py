from flask import Flask, render_template, request, redirect

app = Flask(__name__)
names = []


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        names.append(name)
        return redirect('/')
    if len(names) >= 1:
        highlight = names[0]
        other = names.copy()
        other.pop(0)
        return render_template('base.html', names=other, first=highlight)
    else:
        return render_template('base.html', names=names)


if __name__ == "__main__":
    app.run()
