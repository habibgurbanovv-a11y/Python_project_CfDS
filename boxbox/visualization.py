import matplotlib.pyplot as plt
def plot_tyre_degradation(tyre_results,output_path):
        """
    Plot average lap time against tyre age for each compound.
        tyre_results: DataFrame containing compound, life, mean and count.
        output_path: Location where the chart will be saved.
    """

        plt.figure(figsize = (12,6))

        for compound in tyre_results["compound"].unique():
            compound_data = tyre_results[
                  tyre_results["compound"] == compound
            ]

            plt.plot(
                  compound_data["life"],
                  compound_data["mean"],
                  marker = "o",
                  label = compound
            )
        plt.xlabel("Tyre Age(Laps)")
        plt.ylabel("Average Lap Time (Seconds)")
        plt.title("2026 Australian GP - Tyre Degradation Analysis")
        plt.legend(title = "TYre Compound")
        plt.grid(True,alpha = 0.3)

        plt.tight_layout()
        plt.savefig(output_path,dpi = 300)
        plt.close()