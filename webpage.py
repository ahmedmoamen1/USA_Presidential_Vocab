from flask import Flask, render_template, request
import presidentialVocab as pv
import president_helper as ph
import GatherData as GD

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',  options = list(GD.presidents.values()))

@app.route('/Search1', methods=['GET', 'POST'])
def Search1():
    selected_options = request.form.getlist("options")
    word = request.form.get('Similar')
    max = request.form.get('max')
    speech = ph.get_presidents_sentences(selected_options)
    try:
        similar = pv.findMostSimilar(speech, word, max)
    except Exception as e:
        similar = "NONE"
    print(similar)
    frequent = ph.most_frequent_words(speech)
    result = [list(x) for x in zip(similar, frequent)]
    return render_template('index.html', options = list(GD.presidents.values()),results= result)