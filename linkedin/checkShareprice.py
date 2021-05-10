from nsetools import Nse
from pprint import pprint
nse = Nse()
q = nse.get_quote('infy')
print(type(q))
print('Sym',q['symbol'],'LTP',q['lastPrice'])
# print(q['symbol'],q['lastPrice'])

