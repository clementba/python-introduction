from src import score

def test_score():
    assert score("XXXXXXXXXXXX") == 300
    assert score("9-9-9-9-9-9-9-9-9-9-") == 90
    assert score("5/5/5/5/5/5/5/5/5/5/5") == 150
    assert score("------------------------------") == 0