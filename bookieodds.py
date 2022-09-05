import requests
import json
import pandas as pd


url = "https://eu-offering.kambicdn.org/offering/v2018/ubse/betoffer/group/1000094985,1000095057,1000095049,1000095001,1000094994,1000094991,1000094981,1000176408,2000069140,1000093381,2000077426,2000130521,2000113672,2000130522,1000095052,1000094986,1000093393,1000093399,2000051466,1000094569,1000094984,1000095050,1000094998,2000065880,1000093570,1000095059,1000094993,1000095063,1000094995,1000094990,1000094992,1000094980,1000094965,2000050561,1000094971,1000094978,1000095010,1000095062,1000095061,1000094744,1000094745,1000123032,2000065674,2000105692.json?lang=sv_SE&market=SE&onlyMain=true&ncid=1662031539"

payload={}
headers = {
  'Connection': 'keep-alive',
  'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
  'sec-ch-ua-mobile': '?0',
  'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
  'Accept': '*/*',
  'Origin': 'https://www.unibet.se',
  'Sec-Fetch-Site': 'cross-site',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Dest': 'empty',
  'Referer': 'https://www.unibet.se/',
  'Accept-Language': 'en-US,en;q=0.9'
}

r = requests.request("GET", url, headers=headers, data=payload)

data = r.json()

print(json.dumps(data, indent=4))

df = pd.json_normalize(odds)

print(df.head())

df.to_csv('data.csv', index=False)
