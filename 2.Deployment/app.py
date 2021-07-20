import os
from flask import Flask, render_template, request
from predict import *

app = Flask(__name__, static_url_path='/static')
app.secret_key = "pren"

UPLOAD_FOLDER = './static/images/'
ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg']

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def recognize():
    prediction = ""
    
    if 'uploaded-img' not in request.files:
        prediction = "INIT"
    else:
        uploaded_image = request.files['uploaded-img']
        
        if('.' in uploaded_image. filename):
            file_extension = uploaded_image.filename.split('.')[-1]
        else:
            file_extension = 'INVALID'

        if(file_extension in ALLOWED_EXTENSIONS):
            path = os.path.join(app.config['UPLOAD_FOLDER'], 'upload.jpg')
            uploaded_image.save(path)
            prediction = predict_label(path)
        else:
            prediction = "INVALID IMAGE"

    return render_template('index.html', prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True, port=8000)