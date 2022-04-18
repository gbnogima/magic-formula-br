from stockdata.stock_dataframe_builder import get_dataframe
from calculator.calculator import Calculator

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--strategy", help = "Choose strategy, options: [STATUS_INVEST_CSV]", default='STATUS_INVEST_CSV')
parser.add_argument("-t", "--min-trading-volume", help = "Choose min trading volume", default=10000000, type=int)
parser.add_argument("-m", "--min-market-cap", help = "Choose min market cap", default=100000000, type=int)
parser.add_argument("-r", "--result-size", help = "Choose result size", default=20, type=int)

args = parser.parse_args()
print(args)

stock_dataframe = get_dataframe(args.strategy)
calculator = Calculator(stock_dataframe, args.min_trading_volume, args.min_market_cap, args.result_size)
calculator.calculate()
