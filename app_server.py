from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('page_layouts/home.html')

@app.route("/devlog")
def devlog():
    return render_template('page_layouts/devlog.html')

@app.route("/techstack")
def techstack():
    return render_template('page_layouts/techstack.html')

@app.route("/techstack/bsroformer")
def techstack_individual():
    return render_template('page_layouts/techstack_bsroformer.html')

@app.route("/ref_layout")
def ref_layout():
    return render_template('reference_layout.html')