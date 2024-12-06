from flask import Flask, redirect, render_template
import subprocess


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('hello.html')


@app.route('/streamlit')
def streamlit_app():
    # Redireciona para a aplicação Streamlit executando em outra porta
    return redirect("http://localhost:8501")


def start_streamlit():
    # Inicie o Streamlit como um subprocesso
    print("*** INICIANDO SUBPROCESS STREAMLIT ***")
    subprocess.Popen(['streamlit', 'run', 'dashboard.py'])


if __name__ == '__main__':
    # Inicie o Streamlit e o Flask
    start_streamlit()
    app.run(port=5000)