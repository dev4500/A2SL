from flask import Flask, render_template, jsonify
from vscodecheck import SignLanguageConverter

app = Flask(__name__)
converter = SignLanguageConverter()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_conversion')
def start_conversion():
    # Call live_audio_to_sign_language function to get sign language images
    sign_language_images = converter.live_audio_to_sign_language()

    # Here you can convert the images to base64 format or save them temporarily and return their paths
    # For simplicity, let's assume we're just returning the paths
    image_paths = [image_path for image_path in sign_language_images]

    # Return the paths of the sign language images as JSON response
    return jsonify(result=image_paths)

if __name__ == "__main__":
    app.run(debug=True)
