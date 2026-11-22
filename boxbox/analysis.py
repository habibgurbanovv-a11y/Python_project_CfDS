def calculate_average_lap_time(df):
    """
    Calculate the average lap time for each driver

    """

    average_times = df.groupby("driver")["lap_time_seconds"].mean()

    return average_times


def calculate_fastest_driver(df):
    fastest_driver = df.groupby("driver")["lap_time_seconds"].mean().idxmin()
    return fastest_driver