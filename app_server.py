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
    return render_template('techstack.html')

def get_audio_list():
    from google.cloud import storage
    storage_client = storage.Client()
    bucket_name = "seventh-wav-prod-media"
    bucket = storage_client.bucket(bucket_name)
    blobs = bucket.list_blobs(prefix='audios/')

    audio_data = []
    for blob in blobs:
        if blob.name == 'audios/':
            continue
        signed_url = blob.generate_signed_url(version="v4", expiration=300, method="GET")
        filename= blob.name.split('/')[-1]
        audio_data.append({'title':filename, 'signed_url':signed_url})
    return audio_data

@app.route("/techstack/bsroformer")
def techstack_individual():
    audio_data = get_audio_list()
    return render_template('techstack_bsroformer.html', audio_list=audio_data)