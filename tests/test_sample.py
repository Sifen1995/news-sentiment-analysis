# def test_sample_addition():
#     assert 1 + 1 == 2




import pandas as pd
import pytest
import os

# This helper function mimics your data loading logic
def load_data():
    # Adjust path to match your structure
    file_path = os.path.join('data', 'raw', 'newsData','raw_analyst_ratings.csv') # ensure this name is correct
    if not os.path.exists(file_path):
        return None
    return pd.read_csv(file_path)

def test_data_loading():
    """Check if the data file exists and can be loaded."""
    df = load_data()
    assert df is not None, "Data file could not be found"
    assert isinstance(df, pd.DataFrame)

def test_expected_columns():
    """Ensure the dataset has the columns we need for analysis."""
    df = load_data()
    expected_columns = ['Unnamed', 'headline', 'url', 'publisher', 'date', 'stock']
    for col in expected_columns:
        assert col in df.columns, f"Missing required column: {col}"

def test_headline_is_string():
    """Check that headlines are stored as strings (not numbers or empty)."""
    df = load_data()
    # Check the first few rows to ensure data types are correct
    assert df['headline'].dtype == 'O', "Headline column should be of object (string) type"





