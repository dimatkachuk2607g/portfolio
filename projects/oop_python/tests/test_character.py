"""Tests for the Character class including fixtures to reduce constant object creation,
constructor testing and edge case testing"""

import pytest
from oop_python.src.character import Character


@pytest.fixture()
def aragon():
    return Character("Aragon", 50, 20, 10, 60)


@pytest.fixture()
def goblin():
    return Character("Goblin", 18, 10, 3, 20)


def test_constructor_aragon(aragon):
    assert aragon.name == "Aragon"
    assert aragon.age == 50
    assert aragon.attack == 20
    assert aragon.defense == 10
    assert aragon.health == 60

def test_constructor_goblin(goblin):
    assert goblin.name == "Goblin"
    assert goblin.age == 18
    assert goblin.attack == 10
    assert goblin.defense == 3
    assert goblin.health == 20


def test_health_get_set(aragon):
    aragon.health = 40
    assert aragon.health == 40

    aragon.health = -10
    assert aragon.health == 0

    with pytest.raises(TypeError):
        aragon.health = "abc"


def test_take_damage(goblin):
    actual_health = goblin.health
    damage = 5
    goblin.take_damage(damage)
    expected_health_after_damage = max(0, actual_health - max(0, damage - goblin.defense))
    assert goblin.health == expected_health_after_damage


def test_attack_target(aragon,goblin):
    actual_health = goblin.health
    actual_damage = aragon.attack
    aragon.attack_target(goblin)
    expected_health_after_damage = max(0, actual_health - max(0, actual_damage - goblin.defense))
    assert goblin.health == expected_health_after_damage


def test_heal(aragon):
    original_health = aragon.health
    heal_amount = 10
    aragon.heal(heal_amount)
    assert aragon.health == original_health + heal_amount

    aragon.health = 0
    aragon.heal(5)
    assert aragon.health == 5


def test_is_alive(aragon, goblin):
    aragon.health = 10
    assert aragon.is_alive() is True

    goblin.health = 0
    assert goblin.is_alive() is False




