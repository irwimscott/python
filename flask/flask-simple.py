from flask import Flask, render_template
import os

# initialize Flask
app = Flask(__name__)
@app.route('/<valora>')
def index():
    return render_template('index.html', results=[+ valora])
	
if __name__ == '__main__':
    app.run(debug=True)