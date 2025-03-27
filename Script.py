import requests
import bs4
import json

base_url = 'https://docs.oracle.com/en/java/javase/17/docs/api/'
all_packages_url = base_url + 'allpackages-index.html'

res = requests.get(all_packages_url)
res.raise_for_status()  # Raise an exception for bad status codes
sp = bs4.BeautifulSoup(res.text, 'html.parser')

data = {}

for package_link_tag in sp.select('.col-first.even-row-color a, .col-first.odd-row-color a'):
    package_name = package_link_tag.text
    package_url = base_url + package_link_tag['href']

    req1 = requests.get(package_url)
    req1.raise_for_status()
    sp1 = bs4.BeautifulSoup(req1.text, 'html.parser')

    classes = [class_link.text for class_link in sp1.select('.col-first.even-row-color a, .col-first.odd-row-color a')]
    data[package_name] = classes

with open('document.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Data saved to document.json")