from flask import Flask
app = Flask(__name__)
@app.route('/')

def index():
	return 'Web app using python flask'
app.run(debug=True , host='0.0.0.0', port=5000)
