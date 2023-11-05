from python_application.hello_world import get_greeting

def test_get_greeting():
    assert get_greeting() == 'Hello World!'

def test_get_greeting_intentional_fail():
    assert get_greeting() == 'abc123'