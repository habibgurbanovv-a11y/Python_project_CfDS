
import pandas as pd

from boxbox.data_loader import load_data
from boxbox.analysis import calculate_tyre_degradation


def test_tyre_degradation():
    """
    Test tyre degradation analysis using the real Australian GP dataset.
    """

    # Load the real Australian GP dataset
    df = load_data(
        "data/raw/2026_australian_gp/session_laptimes.json"
    )

    # Convert lap times to numeric and remove missing values
    df["time"] = pd.to_numeric(df["time"], errors="coerce")
    df = df.dropna(subset=["time"])

    # Calculate tyre degradation statistics
    results = calculate_tyre_degradation(df)

    # Check that results are not empty
    assert not results.empty

    # Check that every tyre age has at least 8 observations
    assert (results["count"] >= 8).all()

    # Check that all average lap times are below 100 seconds
    assert (results["mean"] < 100).all()

    print("Tyre degradation test passed!")
    print(results.head(10))


if __name__ == "__main__":
    test_tyre_degradation()
