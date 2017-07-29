import requests, json

#request = "https://www.quandl.com/api/v3/datasets/EOD/AAPL.json?api_key=XCF6zzD6xRn7CfKxgzNa"
class Prices():
	def __init__(self, key):
		self.key = key
		self.data = None
	def getPrice(self, ticker):
		today = "2017-07-28"
		request0 = (
			"https://www.quandl.com/api/v3/datasets/" 
			+ "WIKI/" + ticker + ".json?" +
			"start_date=" + today + 
			"&end_date=" + today
		)
		request = (
			"https://www.quandl.com/api/v3/datasets/WIKI/" + ticker + ".json?start_date=" + today + "&end_date=" + today + "&order=asc&column_index=4&collapse=quarterly&transformation=rdiff"
		)
		self.data = requests.get(request).json()
		return self.data

pricer = Prices("XCF6zzD6xRn7CfKxgzNa")
print(pricer.getPrice("APPL"))