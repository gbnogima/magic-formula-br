import pandas as pd

class Calculator:

    def __init__(self, df, min_trading_volume, min_market_cap, result_size):
        self.df = df
        self.min_trading_volume = min_trading_volume
        self.min_market_cap = min_market_cap
        self.result_size = result_size

    def calculate(self):
        self.filter_roic_and_ebit()
        self.filter_by_trading_volume()
        self.filter_by_market_cap()
        self.rank_by_ROIC()
        self.rank_by_EVEBIT()
        self.add_score()
        self.sort_result()
        self.print_results()

    def filter_roic_and_ebit(self):
        self.df = self.df[self.df['ev_ebit'] > 0]
        self.df = self.df[self.df['roic'] > 0]

    def filter_by_trading_volume(self):
        self.df = self.df[self.df['trading_volume'] > self.min_trading_volume]

    def filter_by_market_cap(self):
        self.df = self.df[self.df['market_cap'] > self.min_market_cap]

    def rank_by_ROIC(self):
        self.df['roic_rank'] = self.df['roic'].rank(ascending=False)

    def rank_by_EVEBIT(self):
        self.df['evebit_rank'] = self.df['ev_ebit'].rank(ascending=True)

    def add_score(self):
        self.df['magic_score'] = self.df['roic_rank'] + self.df['evebit_rank']

    def sort_result(self):
        self.df = self.df.sort_values(by=['magic_score']).head(self.result_size)

    def print_results(self):
        result = self.df.reset_index()
        print(result[['ticker', 'name', 'sector', 'segment', 'ev_ebit', 'roic']])
