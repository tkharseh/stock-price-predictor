import yfinance as yf

ticker_list = ["AAPL", "MSFT", "TSLA"]

data = yf.download(
    tickers=ticker_list,
    period="1mo",  # Get data over past month
    interval="1d",  # Data per day
    group_by="ticker"  # Allows for access via symbol (ex. data["MSFT"])
)

print(data["AAPL"])
