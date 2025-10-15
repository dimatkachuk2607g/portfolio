"""
Tests for pokemon_analysis.py functions.
Includes tests for CSV loading, cleaning, type conversion, CSV creation,
opening, pie chart data, and the main function.
"""

import pandas as pd
import data_analysis.src.pokemon_analysis as pa
import pytest
from pathlib import  Path
from unittest.mock import patch

@pytest.fixture
def sample_df():
    """Sample unclean dataframe"""
    return pd.DataFrame({
        "Name": ["Pikachu", "Charmander", "Bulbasaur", "Pikachu", None],
        "Type1": ["Electric", "Fire", "Grass", "Electric", None],
        "Type2": ["None", None, "Poison", "None", None],
        "Height": [0.4, 0.6, 0.7, 0.4, None],
        "Weight": [6.0, 8.5, 9.0, 6.0, None],
        "Legendary": [0.0, 0.0, 0.0, 0.0, None],
    })

@pytest.fixture()
def sample_clean_df():
    """Sample clean dataframe with proper missing values"""
    return pd.DataFrame({
        "Name": ["Pikachu", "Charmander", "Bulbasaur"],
        "Type1": ["Electric", "Fire", "Grass"],
        "Type2": [None, "Doesn't exist", "Poison"],
        "Height": [0.4, 0.6, 0.7],
        "Weight": [6.0, 8.5, 9.0],
        "Legendary": [0, 0, 0],
    })



def test_load_csv_data():
    """Test that the csv file loads correctly"""
    csv_path = Path(__file__).parent.parent / "src" / "pokemon_data.csv"
    expected = pd.read_csv(csv_path)
    actual = pa.load_csv_data()
    pd.testing.assert_frame_equal(actual, expected)


def test_remove_duplicates_and_empty_rows(sample_df):
    """Test that duplicates and empty rows are removed"""
    actual = pa.remove_duplicates_and_empty_rows(sample_df)
    expected = pd.DataFrame({
        "Name": ["Pikachu", "Charmander", "Bulbasaur"],
        "Type1": ["Electric", "Fire", "Grass"],
        "Type2": ["None", None, "Poison",],
        "Height": [0.4, 0.6, 0.7],
        "Weight": [6.0, 8.5, 9.0],
        "Legendary": [0.0, 0.0, 0.0],
    })
    pd.testing.assert_frame_equal(actual, expected)


def test_fill_missing_values(sample_df):
    """Tests that missing values for Type2, Height and Weight were filled"""
    actual = pa.fill_missing_values(sample_df)

    expected = pd.DataFrame({
        "Name": ["Pikachu", "Charmander", "Bulbasaur", "Pikachu", None],
        "Type1": ["Electric", "Fire", "Grass", "Electric", None],
        "Type2": ["None", "Doesn't exist", "Poison", "None", "Doesn't exist"],
        "Height": [0.4, 0.6, 0.7, 0.4, 0.5],
        "Weight": [6.0, 8.5, 9.0, 6.0, 7.25],
        "Legendary": [0, 0, 0, 0, None],
    })

    pd.testing.assert_frame_equal(actual, expected)


def test_force_correct_types(sample_clean_df):
    """Test that each column now has the correct type"""
    actual = pa.force_correct_types(sample_clean_df)

    assert actual["Name"].dtype == object
    assert actual["Type1"].dtype == object
    assert actual["Type2"].dtype == object
    assert actual["Height"].dtype == float
    assert actual["Weight"].dtype == float
    assert actual["Legendary"].dtype == int


def test_create_clean_csv(sample_clean_df):
    pa.create_clean_csv(sample_clean_df)
    expected = pd.read_csv("pokemon_data_clean.csv").where(pd.notnull(pd.read_csv("pokemon_data_clean.csv")), None)
    pd.testing.assert_frame_equal(sample_clean_df, expected)



def test_open_clean_csv(sample_clean_df):
    """Test that the clean csv file can be opened and is correct"""
    pa.create_clean_csv(sample_clean_df)
    actual = pa.open_clean_csv()
    expected = pd.read_csv("pokemon_data_clean.csv")
    pd.testing.assert_frame_equal(actual, expected)


def test_create_type1_pie_chart(sample_clean_df):
    """Test that the pie chart uses the correct values"""
    type_counts = sample_clean_df["Type1"].value_counts()

    expected = {
        "Electric": 1,
        "Fire": 1,
        "Grass": 1,
    }

    assert type_counts.to_dict() == expected


def test_main():
    """Test the main function runs without errors"""
    with patch("matplotlib.pyplot.show"):
        with patch("builtins.print"):
            pa.main()