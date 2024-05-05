import os
import pickle
from flask import Flask, render_template, jsonify, request
import vscodecheck

app = Flask(__name__)

with open('A2SLtestfinal.pkl', 'rb') as f:
    con = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_conversion', methods=['POST'])
def start_conversion():

    if 'audio' not in request.files:
        return jsonify(error="No audio file provided")  

    
    audio_file = request.files['audio']
    
    audio_path = 'audio.wav'
    audio_file.save(audio_path)

    result = con.live_audio_to_sign_language(audio_path) 

    os.remove(audio_path)

    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
