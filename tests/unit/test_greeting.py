"""Unit tests for oranod.hello_nora."""


import pytest

from plugins.module_utils.helper import create_greeting


class TestGreeting:
    # test that module works with string inputs
    def test_greeting(self):
        result = create_greeting("Hello", "Nora")
        assert result == "Hello, Nora!"

        result = create_greeting("Howdy", "Jinx")
        assert result == "Howdy, Jinx!"

    # test that module fails if two args not provided
    def test_greeting_missing_arg(self):
        with pytest.raises(TypeError):
            create_greeting()

        with pytest.raises(TypeError):
           create_greeting("Hello")
