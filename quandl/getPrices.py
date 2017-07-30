import quandl

class Client():
	def __init__(self):
		self.data = None
		quandl.ApiConfig.api_key = "XCF6zzD6xRn7CfKxgzNa"
	def getPrice(self, ticker):
		self.data = quandl.get("FRED/GDP", trim_start="2017-07-27", trim_end="2017-07-28")

		return self.data
getter = Client()
print(getter.getPrice("AAPL"))
