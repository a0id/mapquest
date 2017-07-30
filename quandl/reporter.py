import requests, json

#request = "https://www.quandl.com/api/v3/datasets/EOD/AAPL.json?api_key=XCF6zzD6xRn7CfKxgzNa"
class Prices():
	def __init__(self, key):
		self.key = key
		self.data = None
	def getPrice(self, ticker):
		request = (
			"https://www.quandl.com/api/v3/datasets/EOD/AB.json?rows=5&order=desc&column_index=4&api_key=XCF6zzD6xRn7CfKxgzNa"
		)
		self.data = requests.get(request).json()
		return self.data["dataset"]["data"][0][1]

pricer = Prices("XCF6zzD6xRn7CfKxgzNa")
print(pricer.getPrice("AAPL"))
