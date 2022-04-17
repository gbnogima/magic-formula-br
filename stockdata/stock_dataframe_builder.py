from .data_source import DataSource

import pandas as pd

SECTOR_CSV = 'stockdata/csv/sector.csv'

def get_dataframe(strategy):
    df = select_strategy(strategy).build_dataframe()
    df = add_sector(df)
    return df

def select_strategy(strategy):
    for data_source in DataSource.__subclasses__():
        obj = data_source()
        if obj.get_strategy() == strategy:
            print(f"Using data source strategy: {strategy}")
            return obj

    raise Exception("Couldn't found data source strategy.")

def add_sector(df):
    sector = pd.read_csv(SECTOR_CSV, sep=';')
    sector = sector.set_index('code')
    df.insert(1, 'code', [stock[:4] for stock in df['ticker']])
    df = df.set_index('code')
    df = df.join(sector, on=['code'], how='left')
    df = df.reset_index()

    return df
