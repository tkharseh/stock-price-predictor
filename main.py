import yfinance as yf
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

sp500 = ["AAPL", "MSFT", "TSLA", "GME", "ETH-USD", "DOGE-USD"]


def load_data(ticker_list):
    data = yf.download(
        tickers=ticker_list,
        period="10y",  # Get data over past month
        interval="1d",  # Data per day
        group_by="ticker"  # Allows for access via symbol (ex. data["MSFT"])
    )
    return data


def get_closing_info(ticker):
    closing_info = {}
    data = load_data(sp500)
    closing_prices = []
    dates = []
    for i in range(len(data[(ticker, 'Close')])):
        closing_price = data[(ticker, 'Close')][i]
        date = data[(ticker, 'Close')].keys()[i]
        closing_prices.append(closing_price)
        dates.append(date)
    closing_info['closing prices'] = closing_prices
    closing_info['dates'] = dates
    return closing_info


def plot_closing_prices(ticker, closing_prices, dates):
    print(len(closing_prices))
    plt.title(f'Close Price History of {ticker}', fontsize=18)
    plt.plot(dates, closing_prices)
    plt.xlabel('Date', fontsize=18)
    plt.ylabel('Close Price USD ($)', fontsize=18)
    plt.show()


def main():
    ticker = input('Enter a ticker of the stock you would like to plot.\n')
    load_data(sp500)
    print(get_closing_info(ticker))
    plot_closing_prices(ticker, get_closing_info(ticker)['closing prices'], get_closing_info(ticker)['dates'])


if __name__ == '__main__':
    main()
