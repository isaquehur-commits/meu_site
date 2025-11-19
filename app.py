from flask import Flask, render_template
import pandas as pd
import json

app = Flask(__name__)

@app.route('/')
def sobre():
    return render_template('sobre.html')

@app.route('/index')
def index():
    # Lê o Excel
    df = pd.read_excel("data/banco.xlsx")

    # Converte a coluna de data (installationDate) para datetime
    # e força o formato ISO (YYYY-MM-DD)
    if 'installationDate' in df.columns:
        df['installationDate'] = pd.to_datetime(
            df['installationDate'], 
            errors='coerce'
        ).dt.strftime('%Y-%m-%d')  # <-- FORMATO CORRETO PARA O JS

    # Converte o DataFrame em uma lista de dicionários
    registros = df.to_dict(orient="records")

    # Converte para JSON e envia ao HTML
    components_json = json.dumps(registros, ensure_ascii=False)

    return render_template("index.html", components_json=components_json)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
