# install packages
import pandas as pd
import matplotlib.pyplot as plt


from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error


class GoldPriceAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = self.load_data()
        self.returns_df = self.calculate_returns()

    def load_data(self):
        """Loads the CSV file into a pandas DataFrame."""
        try:
            df = pd.read_csv(self.file_path)
            df["Date"] = pd.to_datetime(df["Date"])
            print("Data loaded successfully.")
            return df
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {self.file_path}")

    def calculate_returns(self):
        """Calculates daily returns for all financial instruments."""
        if self.df is None:
            return None

        # Select all numerical columns except 'Date'
        numerical_cols = self.df.select_dtypes(include=["float64"]).columns.tolist()

        # Calculate percentage change for these columns
        returns_df = self.df[numerical_cols].pct_change().dropna()
        print("\nDaily returns calculated successfully.")
        return returns_df

    def inspect_data(self):
        """Displays key information about the dataset."""
        if self.df is None:
            return

        print("\n--- first 5 rows of the data ---")
        print(self.df.head())

        print("\n--- data basic info ---")
        self.df.info()

        print("\n--- descriptive statistics ---")
        print(self.df.describe())

        print("\n--- missing values per column ---")
        print(self.df.isnull().sum())

        print("\n--- total duplicate rows ---")
        print(self.df.duplicated().sum())

    def filter_by_time(self, start_date, end_date):
        """Filters the DataFrame to include data from a specific year onwards."""
        if self.df is None:
            return None

        filtered_df = self.df[
            (self.df["Date"] >= start_date) & (self.df["Date"] <= end_date)
        ].copy()
        return filtered_df

    def get_yearly_mean(self, column_name):
        """Calculates the mean of a column, grouped by year."""
        if self.df is None:
            return None

        self.df["Year"] = self.df["Date"].dt.year
        yearly_mean = self.df.groupby("Year")[column_name].mean()
        # yearly_std = self.df.groupby('Year')[column_name].std()
        print(f"\nAverage {column_name} price by year: {yearly_mean}")
        return yearly_mean

    def explore_ml_model(self, features, target):
        """Trains a Linear Regression model using daily returns."""
        if self.returns_df is None:
            return

        # We will use the returns_df for modeling
        X = self.returns_df[features]
        y = self.returns_df[target]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        model = LinearRegression()
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)

        # Evaluate the model's performance
        r2 = r2_score(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)

        print("\n--- Linear Regression Model Results on Returns ---")
        print("Model Coefficients:")
        for i, feature in enumerate(features):
            print(f"- {feature} Return: {model.coef_[i]:.4f}")
        print(f"Intercept: {model.intercept_:.4f}")
        print("\n--- Model Evaluation on Test Data ---")
        print(f"R-squared (R²): {r2:.4f}")
        print(f"Mean Squared Error (MSE): {mse:.4f}")

        return model

    def create_cumulative_return_plot(self, columns, title):
        """
        Plots the cumulative returns of selected instruments.
        This method remains the same as it already works with returns.
        """
        if self.df is None:
            return

        plt.figure(figsize=(12, 8))

        # Use the stored returns_df for calculation
        df_returns = self.returns_df[columns]

        for col in columns:
            cumulative_returns = (1 + df_returns[col]).cumprod()
            plt.plot(
                self.df["Date"].iloc[1:], cumulative_returns, label=col
            )  # Match date to returns_df

        plt.title(title)
        plt.xlabel("Date")
        plt.ylabel("Cumulative Return")
        plt.legend(title="Financial Instruments")
        plt.grid(True)
        plt.show()


if __name__ == "__main__":
    file_path = "./gold_data_2015_25.csv"
    analyzer = GoldPriceAnalyzer(file_path)

    if analyzer.df is not None:
        # Step 2: Inspect the Data
        analyzer.inspect_data()

        # Step 3: Basic Filtering and Grouping
        df_2025 = analyzer.filter_by_time("2025-01-01", "2025-08-01")

        yearly_means = analyzer.get_yearly_mean(["GLD", "SLV"])
        print(yearly_means)

        # Step 4: Explore a Machine Learning Algorithm
        features = ["SPX", "EUR/USD", "SLV"]
        target = "GLD"
        model = analyzer.explore_ml_model(features, target)

        # Step 5: Visualization
        analyzer.create_cumulative_return_plot(
            columns=["SPX", "GLD", "USO", "SLV", "EUR/USD"],
            title="Cumulative Returns Over Time",
        )
