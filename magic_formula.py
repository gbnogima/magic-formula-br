from stockdata.stock_dataframe_builder import get_dataframe
from calculator import Calculator

STRATEGY = 'STATUS_INVEST_CSV'
MIN_TRADING_VOLUME = 10000000
MIN_MARKET_CAP = 100000000
RESULT_SIZE = 20

stock_dataframe = get_dataframe(STRATEGY)
calculator = Calculator(stock_dataframe, MIN_TRADING_VOLUME, MIN_MARKET_CAP, RESULT_SIZE)
calculator.calculate()
