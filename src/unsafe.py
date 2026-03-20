# src/unsafe.py — versão para forçar alerta no PR
import os
import subprocess

def run_untrusted():
    # Fonte de dados não confiável (user-controlled)
    user_input = input("Digite algo: ")

    # SINK 1: uso inseguro de shell + concatenação
    subprocess.run("ls -la " + user_input, shell=True)

    # SINK 2: comando do SO com entrada não sanitizada
    os.system("cat " + user_input)

if __name__ == "__main__":
    run_untrusted()
