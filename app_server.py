from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/devlog")
def devlog():
    return render_template('devlog.html')


@app.route("/techstack")
def techstack():
    return render_template('techstack_bsroformer.html')