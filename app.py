from flask import Flask, render_template

app = Flask(__name__)

# Agora a rota principal (/) vai para sobre.html
@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

# A segunda página será index.html
@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)