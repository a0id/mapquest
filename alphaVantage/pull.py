import requests, json

class Prices():
	def __init__(self, key):
		self.key = key
		self.data = []
        self.tempData = None
    def getOldPrice(self):
        request = (

        )
        self.tempData = requests.get(request).json()
        self.data.append(self.tempData[])
        return self.data
	def getPrices(self, ticker):
        request = (
			"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + ticker + "&apikey=" + self.key
		)
		self.tempData = requests.get(request).json()
        self.data.append(self.tempData["Time Series (Daily)"]["2017-07-28"])
        self.getOldPrice()
pricer = Prices("GDJIXVNNXQGHSD7A")
print(pricer.getPrices("AAPL"))
