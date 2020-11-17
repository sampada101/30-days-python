from flask import Flask, render_template, request, redirect, abort

app = Flask(__name__)


def getblogs():
    global blogs
    blogs = {}
    with open('blogs.csv', 'r') as f:
        lines = f.readlines()
        for i in lines:
            try:
                name, rating, desc, price, filename = i.strip('\n').split(',')
                blogs[name] = {'desc': desc, 'rating': int(rating), 'file': filename, 'price': price}
            except:
                break


def addblog(name, desc, rating, filename, price):
    getblogs()
    blogs[name] = {'desc': desc, 'rating': int(rating), 'file': filename, 'price': price}
    with open('blogs.csv', 'w') as f:
        for i in blogs:
            f.write(f"{i},{blogs[i]['rating']},{blogs[i]['desc']},{blogs[i]['price']},{blogs[i]['file']}\n")
    getblogs()


@app.route('/')
def home():
    getblogs()
    return render_template('index.html', blogs=[blogs[i]['file'] for i in blogs], names=[i for i in blogs])


@app.route('/blogs/<blogname>')
def blog(blogname):
    getblogs()
    try:
        return render_template('bloginfo.html', name=blogname, rating=blogs[blogname]['rating'],
                               desc=blogs[blogname]['desc'], file=blogs[blogname]['file'],
                               price=blogs[blogname]['price'])
    except:
        return abort(404)


@app.route('/add', methods=['GET', 'POST'])
def add():
    getblogs()
    if request.method == "GET":
        return render_template('addblog.html')
    name = request.form.get('name')
    if name not in blogs:
        desc = request.form.get('desc')
        rating = request.form.get('rating')
        price = request.form.get('price')
        pic = request.files['pic']
        pic.filename = name + '.' + pic.filename.split('.')[1]
        addblog(name, desc, rating, pic.filename, price)
        pic.save('static/img/' + pic.filename)
        return redirect(request.url)
    return f"""
<html>
<body>

<script>
  alert("This name already exists! Please Try Again");
  location.replace("{request.url}")
</script>

</body>
</html>

    """


if __name__ == "__main__":
    app.run()
