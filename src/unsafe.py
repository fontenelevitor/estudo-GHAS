# src/unsafe.py — PR DELTA COM DATAFLOW EXPLÍCITO
import os
import subprocess

def run_untrusted():
    # Fonte não confiável: input() (controlado pelo usuário)
    user_input = input("Digite algo: ")

    # SINK #1: shell=True + concatenação -> padrão clássico de injeção
    subprocess.run("sh -lc 'ls -la " + user_input + "'", shell=True)

    # SINK #2: comando de SO com concatenação
    os.system("echo start && cat " + user_input)

if __name__ == "__main__":
    run_untrusted()
