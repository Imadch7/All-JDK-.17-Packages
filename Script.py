import requests
import bs4 
import pandas as pd
import json

res = requests.get('https://docs.oracle.com/en/java/javase/17/docs/api/allpackages-index.html')
sp = bs4.BeautifulSoup(res.text, 'html.parser') 
for i in sp.select('.col-first.even-row-color, .col-first.odd-row-color'):
    req1 = requests.get('https://docs.oracle.com/en/java/javase/17/docs/api/'+i.a['href'])
    sp1 = bs4.BeautifulSoup(req1.text, 'html.parser')
    with open('document.json', 'a') as file:
        json.dump({i.text: [i.text for i in sp1.select('.col-first.even-row-color, .col-first.odd-row-color')]}, file)
