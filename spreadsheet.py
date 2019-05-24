import pandas as pd
from config import CSV


def get_spreadsheet():
    spreadsheet = pd.read_csv(CSV)
    result = (
        spreadsheet.loc[0, 'Unnamed: 1'],
        spreadsheet.loc[1, 'Unnamed: 1'],
        spreadsheet.loc[2, 'Unnamed: 1'],
        spreadsheet.loc[0, 'Unnamed: 4'],
        spreadsheet.loc[1, 'Unnamed: 4'],
        spreadsheet.loc[2, 'Unnamed: 4'],
    )
    return result
