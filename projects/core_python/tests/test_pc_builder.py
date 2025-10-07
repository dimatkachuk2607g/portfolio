"""
Tests for pc_builder Project, testing both valid and invalid inputs,
also includes mocking user input for the testing
"""

import core_python.src.pc_builder as pcb
import pytest
import json
from pathlib import Path
from unittest.mock import patch

@pytest.mark.parametrize("inputs,expected", [
    ([" ", "abc", "2"], "2"),
    (["", "olp", "2"], "2"),
    ([" ", "abc", "3"], "3"),
])
def test_get_build_choice(inputs, expected):
    with patch("builtins.input", side_effect=inputs):
        assert pcb.get_build_choice() == expected


@pytest.mark.parametrize("inputs,expected", [
    ([" ", "qwe", "1"], "1"),
    ([" ", "awq", "2"], "2"),
])
def test_get_platform_choice(inputs, expected):
    with patch("builtins.input", side_effect=inputs):
        assert pcb.get_platform_choice() == expected


def test_json_load_parts():
    json_path = Path(__file__).parent.parent / "src" / "part_list.json"
    with open(json_path, "r") as fh:
        expected = json.loads(fh.read())
    actual = pcb.json_load_parts()
    assert actual == expected



