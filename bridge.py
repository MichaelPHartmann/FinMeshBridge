from FinMesh.iex import stock
import csv
import json

class company(object):

    def fetch_prices(self, range):
        prices = stock.historical_price(self.ticker, range=range)
        with open(f"{self.ticker}_prices.csv", 'w+') as f:
            writer = csv.writer(f, delimiter=',')
            h = prices[0]
            writer.writerow(h)
            for entry in prices:
                v = entry.values()
                writer.writerow(v)

    def fetch_balance_sheet(self, period='Quarterly', last=1):
        bs = stock.balance_sheet(self.ticker, period=period, last=last)
        with open(f"{self.ticker}_balance_sheet.csv", 'w+') as f:
            writer = csv.writer(f, delimiter=',')
            years = bs['balancesheet']
            h = bs['balancesheet'][0].keys()
            writer.writerow(h)
            for entry in years:
                values = entry.values()
                writer.writerow(values)

    def fetch_income_statement(self, period='Quarterly', last=1):
        bs = stock.income_statement(self.ticker, period=period, last=last)
        with open(f"{self.ticker}_income_statement.csv", 'w+') as f:
            writer = csv.writer(f, delimiter=',')
            years = bs['income']
            h = bs['income'][0].keys()
            writer.writerow(h)
            for entry in years:
                values = entry.values()
                writer.writerow(values)

    def fetch_cash_flow(self, period='Quarterly', last=1):
        bs = stock.cash_flow(self.ticker, period=last, last=last)
        with open(f"{self.ticker}_cash_flow.csv", 'w+') as f:
            writer = csv.writer(f, delimiter=',')
            years = bs['cashflow']
            h = bs['cashflow'][0].keys()
            writer.writerow(h)
            for entry in years:
                values = entry.values()
                writer.writerow(values)

    def fetch_all_financials(ticker):
        fetch_cash_flow(self.ticker)
        fetch_balance_sheet(self.ticker)
        fetch_income_statement(self.ticker)

    def __init__(self,ticker):
        self.ticker = ticker
