#!/usr/bin/env python3

from fruit_app import random_fruit


def test_random_fruit():
    assert "apple" or "cherry" or "orange" in random_fruit()
