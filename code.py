import os
os.system('sudo apt-get install openvpn')
os.system('pip3 install bs4 pandas')
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import pandas as pd
os.system("python2 ./vpn.py Japan")
try:
  everyThing = {"brand":[],"year":[],"model":[],"car":[]}
  url = 'https://www.rockauto.com/en/catalog/'
  req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
  webpage = urlopen(req).read()
  page_soup = soup(webpage, 'html.parser')
  res = page_soup.find_all('a',{"class": "navlabellink"})
  brands = []
  for r in res:
    brands.append(r.contents[0])
  for br in brands:
    os.system("python2 ./vpn.py Japan")
    print("Getting data for "+ br)
    br = br.replace(" ", "+")
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
  print("Rerun this script after some time")