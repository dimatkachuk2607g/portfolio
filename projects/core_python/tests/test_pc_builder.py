import core_python.src.pc_builder as pcb
import pytest
import json
from pathlib import Path
from unittest.mock import patch

def test_get_build_choice_valid_and_invalid_1():
    inputs = [" ", "abc", "2"]
    with patch("builtins.input", side_effect=inputs):
        choice = pcb.get_build_choice()
        assert choice == "2"

def test_get_build_choice_valid_and_invalid_2():
    inputs = ["", "olp", "2"]
    with patch("builtins.input", side_effect=inputs):
        choice = pcb.get_build_choice()
        assert choice == "2"

def test_get_build_choice_valid_and_invalid_3():
    inputs = [" ", "abc", "3"]
    with patch("builtins.input", side_effect=inputs):
        choice = pcb.get_build_choice()
        assert choice == "3"


def test_get_platform_choice_valid_and_invalid_1():
    inputs = [" ", "qwe", "1"]
    with patch("builtins.input", side_effect=inputs):
        choice = pcb.get_platform_choice()
        assert choice == "1"

def test_get_platform_choice_valid_and_invalid_2():
    inputs = [" ", "awq", "2"]
    with patch("builtins.input", side_effect=inputs):
        choice = pcb.get_platform_choice()
        assert choice == "2"


def test_json_load_parts():
    json_path = Path(__file__).parent.parent / "src" / "part_list.json"
    with open(json_path, "r") as fh:
        expected = json.loads(fh.read())
    actual = pcb.json_load_parts()
    assert actual == expected



