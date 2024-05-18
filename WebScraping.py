from enum import Enum
from requests.models import PreparedRequest
from bs4 import BeautifulSoup
from curl_cffi import requests
import pandas as pd
import user_filter

# Global variables
names = []
addresses = []
prices = []

# Filter parameters
class ListingType(Enum):
    sale = 'buy'
    rent = 'rent'

class Filters:
    listing_type = ""
    min_price = 0
    max_price = 0
    rooms = []

    def __init__(self, listing_type, min_price, max_price):
        self.min_price = min_price
        self.max_price = max_price
        if listing_type == ListingType.sale.value:
            self.listing_type = ListingType.sale.name
        else:
            self.listing_type = listing_type

# Prep URL
def get_url(filter) -> str:
    base_url = "https://www.propertyguru.com.sg/property-for-sale"
    filter_params = {
            "listing_type": filter.listing_type,
            "maxprice": filter.max_price,
            # "beds[]": 2,
            # "beds[]": 3,
            "market": 'residential',
            "search": 'true'
        }
    req = PreparedRequest()
    req.prepare_url(base_url, filter_params)
    return req.url

def scrape_webpage(url):
    reponse = requests.get(url = url, impersonate="chrome120")
    soup = BeautifulSoup(reponse.text, features='html.parser')
    listings = soup.find_all('div', class_ = 'listing-card')
    for listing in listings:
        name = listing.find('a', class_ = 'nav-link')
        names.append(name.text)
        address = listing.find('p', class_ = 'listing-location')
        addresses.append(address.text)
        price = listing.find('li', class_ = 'list-price')
        prices.append(price.text)
    next_page(soup)

def next_page(soup):
    disabled_next_button = soup.find_all(class_=["pagination-next", "disabled"])
    if disabled_next_button:  # Check for next page
        print("There is no more next page")
    else:
        next_button = soup.find('li', class_ = 'pagination-next')
        next_link = next_button.find('a').get('href')
        url = "https://www.propertyguru.com.sg" + next_link
        print(url)
        scrape_webpage(url)

def create_table():
    df = pd.DataFrame({'Name': names,
                       'Address': addresses,
                       'Price': prices})
    df.to_excel('properties.xlsx', index=False)
    print("DataFrame is written to Excel File successfully.")

filters = Filters(listing_type=user_filter.listing,
                  min_price=user_filter.min_price,
                  max_price=user_filter.max_price)
url = get_url(filters)
scrape_webpage(url)
create_table()

# # Selenium
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
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