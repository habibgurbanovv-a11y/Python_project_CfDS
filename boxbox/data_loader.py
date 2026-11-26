import pandas as pd


def load_data(file_path):
    """
    Load data from a CSV or JSON file.
    """

    if file_path.endswith(".csv"):
        data = pd.read_csv(file_path)

    elif file_path.endswith(".json"):
        data = pd.read_json(file_path)

    else:
        raise ValueError("Unsupported file format")

    return data