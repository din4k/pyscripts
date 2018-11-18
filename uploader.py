from flask import Flask, redirect, url_for, render_template, request
from werkzeug import secure_filename

app = Flask(__name__)


@app.route('/upload')
def upload_file():
	return render_template('upload.html')

@app.route('/success/<name>')
def success(name):
	return "File "+ name +" uploaded successfully."

@app.route('/uploader', methods = ['POST','GET'])
def uploader():
	if request.method == 'POST':
		f = request.files['file']
		f.save(secure_filename(f.filename))
		return redirect(url_for('success',name=f.filename))


if __name__ == '__main__':
	app.run(debug = True)
