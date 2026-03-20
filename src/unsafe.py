# DEMO — código inseguro proposital para alertas do CodeQL
# src/unsafe.py
import os
import subprocess
import yaml

def run_system_command(user_input: str):
    # ESTE CÓDIGO É INSEGURO DE PROPÓSITO PARA DEMONSTRAR O CODEQL
    cmd = f"ls -la {user_input}"
    subprocess.check_output(cmd, shell=True)  # shell=True + interpolação → Command Injection

def parse_yaml_untrusted(data: str):
    # Carregar YAML inseguro → deserialização perigosa
    obj = yaml.load(data, Loader=yaml.Loader)  # intencionalmente inseguro
    return obj

if __name__ == "__main__":
    run_system_command("; echo POC")
    parse_yaml_untrusted("!!python/object/apply:os.system ['echo POC']")
