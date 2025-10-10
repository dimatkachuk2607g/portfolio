"""Tests for the Warrior class including fixtures to reduce constant object creation,
constructor testing and method test"""

import pytest
from oop_python.src.warrior import Warrior, Character


@pytest.fixture()
def conan():
    return Warrior("Conan", 60, 50, 15, 500, 100)


@pytest.fixture()
def dragon():
    return Character("Dragon", 800, 200, 100, 1200)


def test_constructor_conan(conan):
    assert conan.name == "Conan"
    assert conan.age == 60
    assert conan.attack == 50
    assert conan.defense == 15
    assert conan.health == 500
    assert conan.rage == 100


def test_constructor_dragon(dragon):
    assert dragon.name == "Dragon"
    assert dragon.age == 800
    assert dragon.attack == 200
    assert dragon.defense == 100
    assert dragon.health == 1200


def test_rage_attack(conan, dragon):
    original_health = dragon.health
    damage = conan.attack + conan.rage
    conan.rage_attack(dragon)
    expected_health_after_damage = max(0, original_health - max(0, damage - dragon.defense))
    assert dragon.health == expected_health_after_damage

