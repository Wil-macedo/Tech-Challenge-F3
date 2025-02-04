Link do repositório do Github: https://github.com/Wil-macedo/Tech-Challenge-F3

Link do vídeo explicativo no YouTube: https://www.youtube.com/watch?v=k0QvrCU8xEg


# Execute o comando para instalar as dependências:
    pip install -r requirements.txt


## Visão Geral
O código apresenta uma aplicação Flask que também inicia um aplicativo Streamlit em paralelo. A aplicação permite:
- Executar um servidor web com Flask.
- Iniciar um aplicativo Streamlit.
- Baixar um conjunto de dados do Kaggle.
- Estabelecer conexão com um banco de dados PostgreSQL hospedado na AWS.
- Executar consultas SQL para manipulação de dados.

## 1. Baixe o dataset:
    python downloadDataset.py 


## 2. Flask Web Server (inicialização): 
    python app.py

A aplicação Flask é iniciada com as seguintes rotas:

### Rotas

- `@app.route('/deployed')`: Retorna a data e hora do último deploy.
- `@app.route('/')`: Renderiza uma página HTML (`hello.html`).
- `@app.route('/streamlit')`: Redireciona o usuário para a interface Streamlit.

-------------------------------------------------------------------------------------------------------------------

## 3. Download de Dataset do Kaggle

O script baixa um conjunto de dados do Kaggle (`mlg-ulb/creditcardfraud`) usando a biblioteca `kagglehub` e move os arquivos para a pasta `DATASET`.

Os arquivos são renomeados para `base.csv` e movidos para o diretório de destino.

-------------------------------------------------------------------------------------------------------------------

## 4. Conexão com PostgreSQL

A classe `SQL` gerencia a conexão com um banco de dados PostgreSQL hospedado na AWS.