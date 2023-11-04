from python_application.hello_world import get_greeting

def test_main():
    assert get_greeting() == 'Hello World!'