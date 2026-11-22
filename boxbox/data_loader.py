import pandas as pd 
def load_data(file_path):
    """ 
    Load data from a  CSV file
    """

    data = pd.read_csv(file_path)

    return data

