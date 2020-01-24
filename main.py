from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  return "<a href='/home'>HI!</a>"

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/contact')
def contact():
  return render_template('contact.html')

@app.route('/home')
def home():
  return render_template('home.html')  

if __name__ == '__main__':
  app.run(host="0.0.0.0", port = 5222, threaded = True, debug = True)