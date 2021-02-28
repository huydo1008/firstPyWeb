from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")

def main():
    return render_template('index.html')

#def hello():
 #   return "Hello HUY DO!"
