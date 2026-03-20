# src/app.py
import numpy as np
import requests

def main():
    arr = np.arange(1, 10).reshape(3, 3)
    print("Matriz 3x3:")
    print(arr)
    r = requests.get("https://api.github.com", timeout=10)
    print("Status GitHub API:", r.status_code)
