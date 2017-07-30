import requests, json, time, mailClient

class Prices():
	def __init__(self, key):
		self.key = key
		self.data = []
		self.tempData = None
		self.date = ""
		self.time = ""
		self.getTime()
	def getTime(self):
		hr = time.strftime("%H")
		week = time.strftime("%a")
		day = int(time.strftime("%d"))
		if int(hr) < 10:
			hr = "10"
		elif int(hr) > 16:
			hr = "16"
		else:
			hr = hr + ":00:00"
		if week == "Sun":
			day = day-2
		elif week == "Sat":
			day = day-1
		self.time = time.strftime("%Y-%m-" + str(day) + " " + hr)
		self.date = time.strftime("%Y-%m-" + str(day))
	def getOldPrice(self, ticker):
		request = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=" + ticker + "&interval=60min&apikey=" + self.key
		self.tempData = requests.get(request).json()
		self.data.append("Price one hour ago: " + self.tempData["Time Series (60min)"][self.time]["4. close"])
	def getPrices(self, ticker):
		self.tempData = None
		self.data = []
		request = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + ticker + "&apikey=" + self.key
		self.tempData = requests.get(request).json()
		self.data.append("Current price: " + self.tempData["Time Series (Daily)"][self.date]["4. close"])
		self.data.append("Opening price: " + self.tempData["Time Series (Daily)"][self.date]["1. open"])
		self.getOldPrice(ticker)
		return self.data
pricer = Prices("GDJIXVNNXQGHSD7A")



AAPL = "AAPL"
XOM = "XOM"
GOOG = "GOOG"
def format(stock):
	newStock = stock + ": "
	items = pricer.getPrices(stock)
	for x in range(len(items)):
		newStock = newStock + items[x] + ". "
	return newStock
body = []
body.append(format(AAPL))
body.append(format(XOM))
body.append(format(GOOG))

sendBody = ""
for item in body:
	sendBody = sendBody + "\n\n" + item
email = mailClient.Mail()
email.send("Stock Prices By Matt Nappo", sendBody)
