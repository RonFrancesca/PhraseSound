from flask import Flask, escape, request, render_template, jsonify
import sys
sys.path.append('../')
import main as m

app = Flask(__name__)

#rendering index.html page
@app.route('/')
def my_form():
    return render_template('index_basic.html')

@app.route('/parse', methods=['POST', 'GET'])
#get the sentence and send it to the main script to process 
def my_form_post():
    sentence = request.form['text']
    print("Sentence: ", sentence)
    error = m.setSentence(sentence, 2)
    if error:
        return jsonify("fail")
    else:
        return jsonify("ok")

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response