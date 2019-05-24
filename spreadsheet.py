import pandas as pd
from config import CSV


def get_spreadsheet():
    spreadsheet = pd.read_csv(CSV)

    print("test:", spreadsheet.loc[1, 0])
    print("test:", spreadsheet.loc[1, 4])

    return

