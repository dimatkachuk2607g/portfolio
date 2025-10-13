"""
Tests for pc_builder Project, testing both valid and invalid inputs,
also includes mocking user input for the testing with Patch and main() integration test
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
    """Testing get_build_choice, the first two inputs in the inner list are
    invalid and the last input is valid, user input is mocked with patch"""
    with patch("builtins.input", side_effect=inputs):
        assert pcb.get_build_choice() == expected


@pytest.mark.parametrize("inputs,expected", [
    ([" ", "qwe", "1"], "1"),
    ([" ", "awq", "2"], "2"),
])
def test_get_platform_choice(inputs, expected):
    """Testing get_platform_choice, the first two inputs in the inner list are
    invalid and the last input is valid, user input is mocked with patch"""
    with patch("builtins.input", side_effect=inputs):
        assert pcb.get_platform_choice() == expected


def test_json_load_parts():
    """Testing json_load_parts, if there are any errors opening the file or
     if the actual file is incorrect the test will fail"""
    json_path = Path(__file__).parent.parent / "src" / "part_list.json"
    with open(json_path, "r") as fh:
        expected = json.loads(fh.read())
    actual = pcb.json_load_parts()
    assert actual == expected



def test_main():
    """Test main for integration workflow"""
    with patch("builtins.input", side_effect=["1", "2"]), \
            patch("core_python.src.pc_builder.json_load_parts") as mock_json_load, \
            patch("core_python.src.pc_builder.print_summary") as mock_print_summary:

        mock_json_load.return_value = {
            "1": {
                "2": {
                    "CPU - Intel Core i5-12400F": 150,
                    "CPU Cooler - be quiet! Pure Rock 2": 35,
                    "Motherboard - MSI H610M Mortar": 85,
                    "RAM - G.Skill Ripjaws 16GB DDR4-3200": 50,
                    "Storage - 500GB WD Blue SN570 NVMe": 40,
                    "GPU - NVIDIA RTX 5050": 230,
                    "PSU - EVGA 550W Bronze 80+": 45,
                    "Case - Phanteks P300A": 40
                }
            }
        }

        pcb.main()


        expected_build = {
            "CPU - Intel Core i5-12400F": 150,
            "CPU Cooler - be quiet! Pure Rock 2": 35,
            "Motherboard - MSI H610M Mortar": 85,
            "RAM - G.Skill Ripjaws 16GB DDR4-3200": 50,
            "Storage - 500GB WD Blue SN570 NVMe": 40,
            "GPU - NVIDIA RTX 5050": 230,
            "PSU - EVGA 550W Bronze 80+": 45,
            "Case - Phanteks P300A": 40
        }
        mock_print_summary.assert_called_once_with(expected_build)


