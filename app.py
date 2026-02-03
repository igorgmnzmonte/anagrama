from flask import Flask, render_template, request
from model import anagrama

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        palavra = request.form['palavra']
        resposta = anagrama(palavra)
        return render_template('index.html', resposta=resposta, palavra=palavra)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)