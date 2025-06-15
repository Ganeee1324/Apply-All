from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact')
def home():
    return render_template('contact.html')

@app.route('/privacy')
def home():
    return render_template('privacy.html')

@app.route('/terms')
def home():
    return render_template('terms.html')

if __name__ == '__main__':
    app.run(debug=True)