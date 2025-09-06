import unittest
import pandas as pd
from gold_price_analysis import GoldPriceAnalyzer
from unittest.mock import patch


class TestGoldPriceAnalyzer(unittest.TestCase):

    def setUp(self):
        """Set up a mock dataset for testing."""
        data = {
            "Date": ["2025-01-01", "2025-01-02", "2025-01-03"],
            "GLD": [1800.0, 1810.0, 1820.0],
            "SLV": [25.0, 25.5, 26.0],
            "SPX": [3700.0, 3750.0, 3800.0],
            "EUR/USD": [1.2, 1.21, 1.22],
            "USO": [40.0, 41.0, 42.0],
        }
        self.mock_df = pd.DataFrame(data)
        self.mock_df["Date"] = pd.to_datetime(self.mock_df["Date"])

        # Patch the load_data method to return the mock dataset
        with patch(
            "gold_price_analysis.GoldPriceAnalyzer.load_data", return_value=self.mock_df
        ):
            self.analyzer = GoldPriceAnalyzer("mock_file.csv")

    def test_load_data(self):
        """Test if data is loaded correctly."""
        self.assertIsNotNone(self.analyzer.df)
        self.assertEqual(len(self.analyzer.df), 3)
        self.assertIn("GLD", self.analyzer.df.columns)

    def test_calculate_returns(self):
        """Test daily returns calculation."""
        returns_df = self.analyzer.calculate_returns()
        self.assertIsNotNone(returns_df)
        self.assertIn("GLD", returns_df.columns)
        self.assertEqual(len(returns_df), 2)  # 3 rows -> 2 rows after pct_change()

    def test_filter_by_time(self):
        """Test filtering by time range."""
        filtered_df = self.analyzer.filter_by_time("2025-01-01", "2025-01-02")
        self.assertEqual(len(filtered_df), 2)
        self.assertTrue((filtered_df["Date"] >= "2025-01-01").all())
        self.assertTrue((filtered_df["Date"] <= "2025-01-02").all())

    def test_get_yearly_mean(self):
        """Test yearly mean calculation."""
        yearly_mean = self.analyzer.get_yearly_mean(["GLD", "SLV"])
        self.assertIsNotNone(yearly_mean)
        self.assertIn(2025, yearly_mean.index)


if __name__ == "__main__":
    unittest.main()
