
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


def calculate_tyre_degradation(df,max_lap_time = 100, min_observations = 8):
 # Exclude laps of 100 seconds or more to reduce the influence of unusually slow laps
    
    tyre_df = df[df["time"] < max_lap_time].copy()

    tyre_analysis = (
        tyre_df.groupby(["compound", "life"])["time"].agg(["mean", "count"]).reset_index()
    )
        # Keep only tyre ages with at least 8 observations to reduces the influence of very few laps.
    reliable_tyre_ages = tyre_analysis[
        tyre_analysis["count"] >= min_observations
    ].copy()

    return reliable_tyre_ages
