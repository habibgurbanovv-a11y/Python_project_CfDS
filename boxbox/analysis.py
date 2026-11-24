def calculate_average_lap_time(df):
    """
    Calculate the average lap time for each driver

    """

    average_times = df.groupby("driver")["lap_time_seconds"].mean()

    return average_times


def calculate_fastest_driver(df):
    fastest_driver = df.groupby("driver")["lap_time_seconds"].mean().idxmin()
    return fastest_driver


def calculate_driver_ranking(df):
    """
    Calculate and rank drivers by average lap time.
    """

    # 1. Group drivers and calculate average lap times

    # 2. Convert the result into a DataFrame

    # 3. Sort by average lap time
    ranking = df.groupby("driver")["lap_time_seconds"].mean().reset_index().sort_values(by="lap_time_seconds", ascending=True).reset_index(drop=True)

    return ranking


import pandas as pd 

def calculate_driver_consistency(df):
    """
    Calculate lap time standard deviation

    """

    consistency = df.groupby("driver")["lap_time_seconds"].std()
    return consistency


def calculate_driver_statistics(df):
    """
    Calculate average, standard deviation, minimum and maximum lap times.
    """
    statistics = df.groupby("driver")["lap_time_seconds"].agg(["mean","std", "min", "max"])
    return statistics