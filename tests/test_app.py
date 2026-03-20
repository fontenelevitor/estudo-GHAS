
# tests/test_app.py
from src.app import main

def test_main_runs(capsys):
    # Executa a função principal
    main()

    # Captura a saída do console
    captured = capsys.readouterr()

    # Verifica se as mensagens esperadas foram impressas
    assert "Matriz 3x3:" in captured.out
    assert "Status GitHub API:" in captured.out
