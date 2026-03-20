import os
import subprocess

def run_untrusted():
    # Fonte de input não confiável
    user_input = input("Digite algo: ")

    # SINK inseguro: concatenação + shell=True
    subprocess.run("ls -la " + user_input, shell=True)

    # Alternativa insegura detectada pelo CodeQL
    os.system("cat " + user_input)

if __name__ == "__main__":
    run_untrusted()
