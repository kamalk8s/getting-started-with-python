from flask import Flask, render_template

app = Flask(__name__)  # We are inititating a app variable from Flask class (Flask class if part of flask module)

@app.route('/')  # Here we can define the Routes of out web server
def home():
  return render_template('index.html')

@app.route('/<string:username>')
def hello(username):
  return "<h1>Hello, " + username + "</h1>"


# This is a common way to say launch application only if application name matched with main -
if __name__ == '__main__':
  app.run(debug=True) # Debug True allow us to make changes in running server and debug as well. Debug False is recommended for Production.