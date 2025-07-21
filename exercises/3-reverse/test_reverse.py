from reverse import reverse_string

def test_reverse_string():
    assert reverse_string("python") == "nohtyp"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"
