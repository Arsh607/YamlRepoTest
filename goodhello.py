"""This module prints greetings using simple functions."""

def hello():
    """Prints a simple greeting."""
    print("Hello, DevOps learner!")

def bye():
    """Prints a simple farewell."""
    print("Goodbye!")

def greet():
    """Prints happy weekend"""
    print("Happy Weekend")

if __name__ == "__main__":
    hello()
    bye()

def test_hello_prints_expected_text(capsys):
    hello()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, DevOps learner!"

def test_bye_prints_expected_text(capsys):
    bye()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Goodbye!"