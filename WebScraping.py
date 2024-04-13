from bs4 import BeautifulSoup
from curl_cffi import requests
import pandas as pd

url = "https://www.propertyguru.com.sg/property-for-sale"

page = requests.get(url, impersonate="chrome120")
soup = BeautifulSoup(page.text, features='html.parser')

listings = soup.find_all('div', class_ = 'listing-card')
names = []
addresses = []
prices = []
for listing in listings:
    name = listing.find('a', class_ = 'nav-link')
    names.append(name.text)
    address = listing.find('p', class_ = 'listing-location')
    addresses.append(address.text)
    price = listing.find('li', class_ = 'list-price')
    prices.append(price.text)

df = pd.DataFrame({'Name': names,
                   'Address': addresses,
                   'Price': prices})
print(df)