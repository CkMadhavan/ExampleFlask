from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['GET', 'POST'])
def process():
    if request.method == "POST":
        name = request.form['storyText']
        return render_template('welcome_user.html',  username = name)
    else:
        return 'Method Not Allowed'

@app.route('/y9')
def y9():
    return '<h1>Greatest tutor group of all time!</h1>'

if __name__ == '__main__':
    app.run()