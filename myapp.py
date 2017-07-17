from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html", to="Sam Moorhouse")


@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('img', path)

@app.route('/whereami')
def whereami():
	return "Kdua"

@app.route('/hello/<name>')
def foo(name):
    return render_template('index.html', to=name)

port = int(os.environ.get('PORT', 33507))

if __name__ == '__main__':
	app.run(port=port)

