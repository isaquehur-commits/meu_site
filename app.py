from flask import Flask, render_template
import pandas as pd
import json

app = Flask(__name__)

# --- Página Sobre (página inicial) ---
@app.route('/')
def sobre():
    return render_template('sobre.html')


# --- Página Index (com dados do Excel) ---
@app.route('/index')
def index():
    # Lê o Excel
    df = pd.read_excel("data/banco.xlsx")

    # Converte a coluna de data (installationDate) para datetime
    # e força o formato ISO (YYYY-MM-DD) para o JavaScript
    if 'installationDate' in df.columns:
        df['installationDate'] = pd.to_datetime(
            df['installationDate'],
            errors='coerce'
        ).dt.strftime('%Y-%m-%d')

    # Converte o DataFrame em uma lista de dicionários
    registros = df.to_dict(orient="records")

    # Converte para JSON e envia ao HTML
    components_json = json.dumps(registros, ensure_ascii=False)

    return render_template("index.html", components_json=components_json)



# --- Nova página Shopping Center Beta ---
@app.route('/shopping-center-beta')
def shopping_center_beta():

 # Lê o Excel
    df = pd.read_excel("data/banco.xlsx", sheet_name="ELV-042")

# Converte a coluna de data (installationDate) para datetime
    # e força o formato ISO (YYYY-MM-DD) para o JavaScript
    if 'installationDate' in df.columns:
        df['installationDate'] = pd.to_datetime(
            df['installationDate'],
            errors='coerce'
        ).dt.strftime('%Y-%m-%d')

# Converte o DataFrame em uma lista de dicionários
    registros = df.to_dict(orient="records")

# Converte para JSON e envia ao HTML
    elv_data_json = json.dumps(registros, ensure_ascii=False)

    return render_template("shopping_center_beta.html", elv_data_json=elv_data_json)

# --- Execução local ---
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

