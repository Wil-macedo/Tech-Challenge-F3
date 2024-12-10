from flask import Flask, redirect, render_template
import subprocess
import sys
import os


app = Flask(__name__)


@app.route('/deployed')
def deployed():
    return "07-12-2024 22:04"


@app.route('/')
def index():
    return render_template('hello.html')


@app.route('/streamlit')
def streamlit_app():
    try:
        # Apontar para o localhost em um container docker causa conflito entre o container e o host.
        return redirect(f"http://localhost:8070")
    except Exception as ex:
        print("streamlit_app", str(ex))


def start_streamlit():
    try:
        possiblePaths = ["dashboard.py", 
                         os.path.join(os.path.abspath(os.path.curdir), "code","dashboard.py"), 
                         os.path.join(os.path.abspath(os.path.curdir), "dashboard.py")
                        ]
        
        for pathFile in possiblePaths:
        
            if os.path.exists(pathFile):  # Docker image estará no diretório raiz.
                break
                
        print("*** INICIANDO SUBPROCESS STREAMLIT ***")
        subprocess.Popen([sys.executable, "-m", "streamlit", "run", pathFile, "--server.address", "0.0.0.0", "--server.port", "8070", "--server.headless=true"])
    
    except Exception as ex:
        print("start_streamlit", str(ex))
        
        
if __name__ == '__main__':
    # Inicie o Streamlit e o Flask
    start_streamlit()
    app.run(port=8000)

app.run()

    # para construir container docker:
    #docker build -t webserverf3 .
    
    # Para executar com docker:
    # docker run -p 8060:8060 -p 8070:8070 webserverf3