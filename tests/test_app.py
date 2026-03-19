
rom src.app import main

def test_main_runs(capsys):
    main()
    captured = capsys.readouterr()
    assert "Matriz 3x3:" in captured.out
    assert "Status GitHub API:" in captured.out

