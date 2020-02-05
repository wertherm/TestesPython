import urllib.request as ur
import simplejson

response = ur.urlopen("https://api.coinmarketcap.com/v1/global/")

sl = simplejson.load(response)

print("Marketcap Global: " + str(sl["total_market_cap_usd"]))
