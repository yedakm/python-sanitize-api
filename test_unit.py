from app.main import replace_chars

def test_simple_replace():
    repl = {"a":"4","e":"3","i":"1","o":"0","s":"5"}
    assert replace_chars("aku suka nasi", repl) == "4ku 5uk4 n451"
