import os
os.system('pip3 install bs4 pandas')
import time
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import pandas as pd
everyThing = {"brand":[],"year":[],"model":[],"car":[]}
url = 'https://www.rockauto.com/en/catalog/'
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
page_soup = soup(webpage, 'html.parser')
res = page_soup.find_all('a',{"class": "navlabellink"})
brands = []
for r in res:
  brands.append(r.contents[0])
while len(brands)!=0
  try:
      br = brands[0]
      brands = brands[1:]
      print("Getting data for "+ br)
      br = br.replace(" ", "+")
      time.sleep(30)
      req = Request(url+br, headers={'User-Agent': 'Mozilla/5.0'})
      webpage = urlopen(req).read()
      page_soup = soup(webpage, 'html.parser')
      resY = page_soup.find_all('a',{"class": "navlabellink"})
      years = []
      resY = resY[1:]
      for r in resY:
        r = str(r)
        years.append(r[r.find('>')+1:r.find('</')])

      for y in years:
        time.sleep(30)
        req = Request(url+br+","+y, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        page_soup = soup(webpage, 'html.parser')
        resM = page_soup.find_all('a',{"class": "navlabellink"})
        resM = resM[2:]
        models = []
        for r in resM:
          r = str(r)
          models.append(r[r.find('>')+1:r.find('</')])
        for m in models:
          time.sleep(30)
          req = Request(url+br+","+y+","+m, headers={'User-Agent': 'Mozilla/5.0'})
          webpage = urlopen(req).read()
          page_soup = soup(webpage, 'html.parser')
          resC = page_soup.find_all('a',{"class": "navlabellink"})
          r = str(resC[-1])
          car = r[r.find('>')+1:r.find('</')]
          everyThing["brand"].append(br)
          everyThing["year"].append(y)
          everyThing["model"].append(m)
          everyThing["car"].append(car)
      df = pd.DataFrame.from_dict(everyThing)
      df.to_csv(br+'.csv')
      everyThing = {"brand":[],"year":[],"model":[],"car":[]}
      print("Writing data for "+ br + " check "+br+".csv")
  except Exception as e:
    print("Error Occured Didn't got response from the website server")
    print("Waiting for a bit now")
    time.sleep(60*5)
