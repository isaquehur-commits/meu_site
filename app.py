from flask import Flask, render_template
import pandas as pd
import json
from pathlib import Path

app = Flask(__name__)

# --- Página Sobre (página inicial) ---
@app.route('/')
def sobre():
    return render_template('sobre.html')


# --- Página Index (com dados do Excel) ---
@app.route('/index')
def index():
    # Lê o Excel
    df = pd.read_excel("data/banco.xlsx", sheet_name="ELV-001")

    # 🚨 PASSO CRÍTICO: RENOMEIA A COLUNA 'link' PARA 'imageUrl' 🚨
    # Isso garante que o frontend encontre a URL de imagem.
    df = df.rename(columns={'link': 'imageUrl'})

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

    # 🚨 PASSO CRÍTICO: RENOMEIA A COLUNA 'link' PARA 'imageUrl' 🚨
    df = df.rename(columns={'link': 'imageUrl'})

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

# --- Nova página hospital Gama ---
@app.route('/hospital-gama')
def hospital_gama():

    # Lê o Excel
    df = pd.read_excel("data/banco.xlsx", sheet_name="ELV-128")

    # 🚨 PASSO CRÍTICO: RENOMEIA A COLUNA 'link' PARA 'imageUrl' 🚨
    df = df.rename(columns={'link': 'imageUrl'})

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

    return render_template("hospital_gama.html", elv_data_json=elv_data_json)

# --- Nova página Residencial Delta ---
@app.route('/residencial-delta')
def residencial_delta():

    # Lê o Excel
    df = pd.read_excel("data/banco.xlsx", sheet_name="ELV-089")
    
    # 🚨 PASSO CRÍTICO: RENOMEIA A COLUNA 'link' PARA 'imageUrl' 🚨
    df = df.rename(columns={'link': 'imageUrl'})
    
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

    return render_template("residencial_delta.html", elv_data_json=elv_data_json)

# --- Execução local ---
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)