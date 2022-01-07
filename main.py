import yfinance as yf
import matplotlib.pyplot as plt
import bs4 as bs
import requests
import pandas as pd

sp500_list = ["AAPL", "MSFT", "TSLA", "GME", "ETH-USD", "DOGE-USD"]


def get_sp500_stocks():
    resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})
    industries_dict = {}
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text[:-1]
        industry = row.findAll('td')[3].text
        if industry not in industries_dict:
            industries_dict[industry] = []
        industries_dict[industry].append(ticker)
    return industries_dict


def load_data(ticker_list):
    data = yf.download(
        tickers=ticker_list,
        period="10y",  # Get data over past month
        interval="1d",  # Data per day
        group_by="ticker"  # Allows for access via symbol (ex. data["MSFT"])
    )
    return data


def get_closing_info(sector, ticker):
    sp500 = get_sp500_stocks()
    # sp500 = sp500_list
    closing_info = {}
    data = load_data(sp500[sector])
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
    plt.title(f'Close Price History of {ticker}', fontsize=18)
    plt.plot(dates, closing_prices)
    plt.xlabel('Date', fontsize=18)
    plt.ylabel('Close Price USD ($)', fontsize=18)
    plt.show()


def main():
    sp500 = get_sp500_stocks()
    # sp500 = sp500_list
    sector = input('Enter the sector of the stock you would like to plot.\n')
    ticker = input('Enter a ticker of the stock you would like to plot.\n')
    load_data(sp500[sector])
    print(get_closing_info(sector, ticker))
    plot_closing_prices(ticker, get_closing_info(sector, ticker)['closing prices'], get_closing_info(sector, ticker)['dates'])


if __name__ == '__main__':
    main()
