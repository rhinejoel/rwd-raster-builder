import os
import pandas as pd


def get_maxmonth(c_csv: str) -> None:
    """
    Creates a column 'maxmonth' with the max value in the header in the row"

    Parameters:
    c_csv: str, required
        Path to input water pixel count csv file

    Returns:
    None
    """
    parent = os.path.dirname(c_csv)
    file_name = os.path.splitext(os.path.basename(c_csv))[0]
    c_pd = pd.read_csv(c_csv)

    max_month = pd.concat([c_pd, c_pd.idxmax(axis=1)], axis=1)
    max_month = max_month.rename(columns={0: "maxmonth"})

    max_month.to_csv(os.path.join(parent, "{}_maxmonth.csv".format(file_name)))