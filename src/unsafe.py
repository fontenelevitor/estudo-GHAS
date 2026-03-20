# src/unsafe.py (versão para forçar alertas no PR)
import os, subprocess, yaml

def run_system_command(user_input: str):
    os.system("ls -la " + user_input)  # concatenação direta → injeção de comando
    subprocess.run("cat " + user_input, shell=True)  # shell=True + input → risco

def parse_yaml_untrusted(data: str):
    return yaml.load(data)  # sem Loader seguro → deserialização insegura
