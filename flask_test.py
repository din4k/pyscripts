from flask import Flask
app = Flask(__name__)

@app.route('/sayhello/<n>')
def hellow(n):
	return "Hello "+ n +" work"

if __name__ == '__main__':
	app.run("localhost","5001",debug=True)
