# src/unsafe.py
import os
import subprocess
import yaml  # pip install pyyaml (adicione no requirements.txt para o teste)

def run_system_command(user_input: str):
    # Exemplo didático: NÃO faça isso em produção.
    # Risco: Command Injection se user_input vier de fonte não confiável.
    cmd = f"ls -la {user_input}"
    # shell=True + string format -> padrão perigoso
    subprocess.check_output(cmd, shell=True)  # CodeQL deve sinalizar

def parse_yaml_untrusted(data: str):
    # yaml.load sem Loader seguro -> padrão perigoso (execução arbitrária)
    obj = yaml.load(data, Loader=yaml.Loader)  # intencionalmente inseguro
    return obj

if __name__ == "__main__":
    # Simulação de entradas
    run_system_command("; echo POC")
    parse_yaml_untrusted("!!python/object/apply:os.system ['echo POC']")
