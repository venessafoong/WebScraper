from requests.models import PreparedRequest
from bs4 import BeautifulSoup
from curl_cffi import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Prep URL
def get_url() -> str:
    base_url = "https://www.propertyguru.com.sg/property-for-sale"
    filter_params = {
            "listing_type": 'sale',
            "market": 'residential',
            "maxprice": 400000,
            # "beds[]": 2,
            # "beds[]": 3,
            "search": 'true'
        }
    req = PreparedRequest()
    req.prepare_url(base_url, filter_params)
    return req.url


def scrape_webpage(url) -> dict:
    reponse = requests.get(url = url, impersonate="chrome120")
    soup = BeautifulSoup(reponse.text, features='html.parser')
    
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
    create_table(names, addresses, prices)
    next_page(soup)

def next_page(soup):
    next_button = soup.find('li', class_ = 'pagination-next')
    if next_button:
        next_link = next_button.find('a').get('href')
        url = "https://www.propertyguru.com.sg" + next_link
        print(url)
        scrape_webpage(url)
    else:
        print('There is no next page')

def create_table(names, addresses, prices):
    # for item in data:
        df = pd.DataFrame
        ({'Name': names,
          'Address': addresses,
          'Price': prices
          })
        print(df)

url = get_url()
data = scrape_webpage(url)

# # Selenium
# def go_to_next_page(url):
#     # Keep windows open
#     options = Options()
#     options.add_experimental_option('detach', True)
#     # Open browser
#     driver_manager = ChromeDriverManager().install()
#     driver = webdriver.Chrome(service = Service(driver_manager),
#                               options = options
#                               )
#     driver.get(url)
#     # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     # Search next page button
#     next_page_button = driver.find_element(By.CLASS_NAME, "pagination-next")
#     # next_page_button = pagination.find_element(By.XPATH, "//a[@href]")
#     next_page_button.click()