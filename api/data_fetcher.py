"""
This script is meant to be used to load the data for the project.
"""

from typing import List, Iterable

from pandas import DataFrame, read_csv
import yfinance as yf


class StockDataRequest:
    """A data class for YFinance Stock information requests."""
    tickers: List[str]
    _period: str
    _data_interval: str

    def __init__(self, period: str, interval: str):
        self.tickers = []
        self._period = period
        self._data_interval = interval

    def add_tickers(self, tickers: Iterable[str]) -> None:
        self.tickers.extend(tickers)

    def get_period(self) -> str:
        return self._period

    def get_interval(self) -> str:
        return self._data_interval


def update_stock_data(filename: str, request: StockDataRequest) -> DataFrame:
    """Downloads the requested stock data and saves it as a CSV into file
    <filename>."""
    downloaded_data = yf.download(
        tickers=request.tickers,
        period=request.get_period(),
        interval=request.get_interval(),
        group_by="ticker"
    )

    # The downloaded data must be stored in a Pandas dataframe
    assert type(downloaded_data) == DataFrame
    downloaded_data.to_csv(filename)

    return downloaded_data


def load_stock_data(filename: str, up_to_date=False, request=None) -> DataFrame:
    """Loads the stock price data onto a Pandas dataframe. If up_to_date is True
    the latest data is fetched.

    Precondition: request is None iff not up_to_date
    """
    if up_to_date is True:
        return update_stock_data(filename, request)

    return read_csv(filename)


if __name__ == "__main__":
    request = StockDataRequest("10y", "1d")
    request.add_tickers(["MSFT"])

    data = load_stock_data("./data/stock_price_data.csv", up_to_date=True, request=request)
    print(data.head(5))

    data = load_stock_data("./data/stock_price_data.csv")
    print(data.head(5))


