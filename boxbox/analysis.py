
import pandas as pd 


def calculate_average_lap_time(df):
    """
    Calculate the average lap time for each driver.
    """
    average_times = (
        df.groupby("drv")["time"]
        .mean()
        .sort_values(ascending=True)
    )
    return average_times


def calculate_fastest_driver(df):
    fastest_driver = df.groupby("drv")["time"].mean().idxmin()
    return fastest_driver


def calculate_driver_ranking(df):
    """
    Calculate and rank drivers by average lap time.
    """

    # 1. Group drivers and calculate average lap times

    # 2. Convert the result into a DataFrame

    # 3. Sort by average lap time
    ranking = df.groupby("drv")["time"].mean().reset_index().sort_values(by="time", ascending=True).reset_index(drop=True)

    return ranking



def calculate_driver_consistency(df):
    """
    Calculate lap time standard deviation

    """

    consistency = df.groupby("drv")["time"].std()
    return consistency


def calculate_driver_statistics(df):
    """
    Calculate average, standard deviation, minimum and maximum lap times.
    """
    statistics = df.groupby("drv")["time"].agg(["mean","std", "min", "max"])
    return statistics


