import pandas as pd
import pytest

@pytest.fixture
def sample_df():
    """Generates a mock dataframe based on the actual head of the data."""
    data = {
        'Unnamed: 0': [0, 1, 2],
        'headline': [
            'Stocks That Hit 52-Week Highs On Friday', 
            'Stocks That Hit 52-Week Highs On Wednesday',
            '71 Biggest Movers From Friday'
        ],
        'url': ['https://test.com/1', 'https://test.com/2', 'https://test.com/3'],
        'publisher': ['Benzinga Insights', 'Benzinga Insights', 'Lisa Levin'],
        'date': ['2020-06-05 10:30:54-04:00', '2020-06-03 10:45:20-04:00', '2020-05-26 04:30:07-04:00'],
        'stock': ['A', 'A', 'A']
    }
    return pd.DataFrame(data)

def test_column_existence(sample_df):
    """Verify all critical columns are present in the dataset."""
    expected_cols = ['headline', 'url', 'publisher', 'date', 'stock']
    for col in expected_cols:
        assert col in sample_df.columns, f"Column {col} is missing!"

def test_headline_content(sample_df):
    """Ensure headlines are non-empty strings."""
    assert isinstance(sample_df['headline'].iloc[0], str)
    assert len(sample_df['headline'].iloc[0]) > 0

def test_stock_ticker_format(sample_df):
    """Check that stock tickers are in the expected uppercase format."""
    # This ensures 'A' is 'A' and not lowercase or a number
    assert sample_df['stock'].iloc[0].isupper()