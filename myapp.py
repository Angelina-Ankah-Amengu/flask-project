from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")


@app.route('/css/<path:path>')
def send_js(path):
    return send_from_directory('css', path)

@app.route('/whereami')
def whereami():
	return "Kdua"

if __name__ == '__main__':
	app.run(host="0.0.0.0")

