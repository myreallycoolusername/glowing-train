from flask import Flask, redirect, url_for
from wonderwords import RandomWord
from pyttsx3 import init
import os

app = Flask(__name__)
engine = init()
r = RandomWord()

@app.route('/tts/<text>', methods=['GET'])
def text_to_speech(text):
    # Generate a random word for the filename
    filename = r.word() + '.ogg'
    filepath = os.path.join('static', filename)

    # Convert text to speech
    engine.save_to_file(text, filepath)
    engine.runAndWait()

    # Redirect to the audio file's URL
    return redirect(url_for('static', filename=filename))

if __name__ == '__main__':
    app.run(debug=True)
