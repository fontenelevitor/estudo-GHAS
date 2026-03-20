# src/web_unsafe.py
from flask import Flask, request
import subprocess, os, yaml

app = Flask(__name__)

@app.get("/run")
def run():
    # Fonte NÃO confiável: parâmetro de query string ?cmd=...
    cmd = request.args.get("cmd", "")
    # SINK 1: shell=True + concatenação -> injeção de comando
    subprocess.run("sh -lc 'ls -la " + cmd + "'", shell=True)
    # SINK 2: comando de SO com concatenação
    os.system("cat " + cmd)
    return "ok"

@app.post("/yaml")
def yml():
    # Fonte NÃO confiável: corpo (por simplicidade, use ?y= no query string)
    data = request.args.get("y", "")
    # SINK 3: desserialização insegura (sem SafeLoader)
    obj = yaml.safe_load(data)
    return str(type(obj))
