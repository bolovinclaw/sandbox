from hello import greet


def test_greet_named():
    assert greet("world") == "hello, world"


def test_greet_sandbox():
    assert greet("sandbox") == "hello, sandbox"
