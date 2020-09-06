from __future__ import division, print_function
import os
import shutil

import zipfile
import glob


from flask import Flask, send_file, url_for, request, render_template
from werkzeug.utils import secure_filename

# Define a flask app
app = Flask(__name__)


# Necessary
# print('Model loaded. Start serving...')

# You can also use pretrained model from Keras
# Check https://keras.io/applications/
#from keras.applications.resnet50 import ResNet50
#model = ResNet50(weights='imagenet')
#model.save('')
print('Model loaded. Check http://127.0.0.1:5000/')


@app.route('/')
def home():
    # Main page
    return render_template('index.html')
@app.route('/Submission.html')
def submit():
    return render_template('Submission.html')
@app.route('/index.html')
def index():
    return render_template('index.html')
@app.route('/Download.html')
def Download():
    return render_template('Download.html')
@app.route('/Results.html')
def results():
    return render_template('Results.html')
@app.route('/Help.html')
def Help():
    return render_template('Help.html')
@app.route('/Department.html')
def departemnt():
    return render_template('Department.html')
@app.route('/predict', methods=['GET', 'POST'])
def predict():

    if request.method == 'POST':

        # Get the file from post request
        
        print(
            'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz')
        


if __name__ == '__main__':
    app.run(debug=True)

