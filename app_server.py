from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/devlog")
def devlog():
    return render_template('devlog.html')

@app.route("/techstack")
def techstack():
    return render_template('techstack.html')

@app.route("/techstack/bsroformer")
def techstack_individual():
    return render_template('techstack_bsroformer.html')