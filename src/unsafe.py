import os
import subprocess
import yaml

def run_system_command(user_input: str):
    # Vulnerabilidade clara de Command Injection
    os.system("ls -la " + user_input)

    # Outra forma insegura proposital
    subprocess.run("cat " + user_input, shell=True)

def parse_yaml_untrusted(data: str):
    # Vulnerabilidade de deserialização insegura
    return yaml.load(data)  # intencionalmente sem Loader seguro

if __name__ == "__main__":
    run_system_command("; echo POC")
    parse_yaml_untrusted("!!python/object/apply:os.system ['echo POC']")
