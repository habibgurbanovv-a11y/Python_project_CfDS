
import pandas as pd

from boxbox.data_loader import load_data
from boxbox.analysis import calculate_tyre_degradation
from boxbox.visualization import plot_tyre_degradation


# Load the Australian GP dataset
df = load_data(
    "data/raw/2026_australian_gp/session_laptimes.json"
)

# Convert lap times to numeric values
df["time"] = pd.to_numeric(df["time"], errors="coerce")

# Remove records with missing lap times
df = df.dropna(subset=["time"])

# Calculate tyre degradation statistics
tyre_results = calculate_tyre_degradation(df)

# Generate and save the tyre degradation chart
plot_tyre_degradation(
    tyre_results,
    "data/processed/tyre_degradation_by_compound.png"
)

print("Tyre analysis completed successfully!")
print(tyre_results.head(10))
