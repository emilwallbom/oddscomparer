import requests
import json
import pandas as pd

url = "https://ero.betfair.se/www/sports/exchange/readonly/v1/bymarket?_ak=nzIFcwyWhrlwYMrh&alt=json&currencyCode=SEK&locale=sv&marketIds=1.202362469,1.202366611,1.202366731,1.202734110,1.202686847,1.201751569,1.201751638&rollupLimit=100&rollupModel=STAKE&types=RUNNER_STATE"
urls="https://api.betfair.com/exchange/betting/json-rpc/v1"
jsonrpc_req='{"jsonrpc": "2.0", "method": "SportsAPING/v1.0/listEventTypes", "params": {"filter":{}}, "id": 1}'

payload={}
headers = {
  'authority': 'ero.betfair.se',
  'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
  'accept': 'application/json, text/plain, */*',
  'sec-ch-ua-mobile': '?0',
  'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
  'origin': 'https://www.betfair.se',
  'sec-fetch-site': 'same-site',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://www.betfair.se/',
  'accept-language': 'en-US,en;q=0.9',
  'cookie': 'wsid=8fe890b1-294c-11ed-bc98-fa163efe4205; vid=df1fe530-fa92-4d73-bde6-8688c44d1bdc; language=sv; betexPtk=betexLocale%3Dsv%7EbetexRegion%3DGBR; bfsd=ts=1661964432937|st=p; storageSSC=lsSSC%3D1; BETEX_ESD=accountservices; PI=4546; StickyTags=rfr=4546; TrackingTags=rfr=4546; rfr=4546; _gcl_au=1.1.479595070.1661964433; OptanonAlertBoxClosed=2022-08-31T16:47:19.845Z; exp=ex; __cf_bm=_dg1ANepdc9M2i8CYrP7KywARNXe_.Ip69Gh85.Bh_o-1662028690-0-AZdnB+uo/HspF8TJB2Yo779+7owj9WvJlivnQzsWB3cVHpYH/m44sF4cNHdNZtJG9Y3/pMTPhx5ut+1LDO2VSJE=; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Sep+01+2022+12%3A38%3A45+GMT%2B0200+(centraleuropeisk+sommartid)&version=6.18.0&isIABGlobal=false&hosts=&consentId=3e73ee9e-058a-4bf0-ae20-f4d1e3ccd562&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A0%2CC0002%3A0%2CC0004%3A0&AwaitingReconsent=false&geolocation=%3B'
}

r = requests.request("GET", url, headers=headers, data=jsonrpc_req)
response = requests.post(url, data=payload, headers=headers)
data = r.json()

print(json.dumps(data, indent=4))
#print(json.dumps(json.loads(r.text), indent=3))

eventlen = len(data['eventTypes'][0]['eventNodes'])
marketlen = len(data['eventTypes'][0]['eventNodes'][0]['marketNodes'][0]['runners'])
print(eventlen)
print(marketlen)
odds = []
i = 0
while i != eventlen:
    j = 0
    while j != marketlen:
        odds.append(data['eventTypes'][0]['eventNodes'][i]['marketNodes'][0]['runners'][j])
        j = j + 1
    print(odds[i])
    i = i + 1

df = pd.json_normalize(odds)

print(df.head())

df.to_csv('data.csv', index=False)
