
# ─── LIBRARIES ──────────────────────────────────────────────────────────────────
import requests
from lxml import html
from time import sleep
import pandas as pd

## To solve 'InsecureRequestWarning' -> change request.get(verify=True)
import certifi
import urllib3
http = urllib3.PoolManager(
                            cert_reqs='CERT_REQUIRED', 
                            ca_certs=certifi.where()
                        )


# ─── LOCAL MODULES ──────────────────────────────────────────────────────────────
from tools import read_initial_values, write_csv_file, update_status
from variables import *
from filtering import filter_values



# ─── PROGRAM ────────────────────────────────────────────────────────────────────

## Check if 
def initial_validation():
    print('------SCRAPING URLs------')
    asin_df, repeated_values, repeated_input_values = read_initial_values()

    if len(asin_df) > 0:
        asin_list = asin_df['ASIN'].values.tolist()
        print(asin_list)

        scraping_urls(asin_list)

    if ~(repeated_values.empty and repeated_input_values.empty):
        update_status(repeated_values, repeated_input_values)


def scraping_urls(asin_list):
        extracted_data = []

        for i in asin_list:
            url = 'https://www.amazon.com/dp/' + i
            print("Processing: " + url)
            scraped_data = scrape(url)
            if scraped_data:
                extracted_data.append(scraped_data)

        write_csv_file(output_path, extracted_data)
        print('File Saved. Process Complete!')
        

def scrape(url):
    try:
        for i in range(20): # Retrying for failed requests
            sleep(random_delays)
            response = requests.get(url, headers=headers, verify=True)

            if response.status_code == 200:
                doc = html.fromstring(response.content)

                ## GET DATA FROM XPATHS
                ## Output: Strings
                RAW_NAME = doc.xpath(XPATH_NAME)
                RAW_AUTHOR = doc.xpath(XPATH_AUTHOR)
                RAW_STARS = doc.xpath(XPATH_STARS)
                RAW_ISBN13 = doc.xpath(XPATH_ISBN13)
                RAW_ISBN10 = doc.xpath(XPATH_ISBN10)
                RAW_ASIN = doc.xpath(XPATH_ASIN)
                RAW_SALE_PRICE = doc.xpath(XPATH_SALE_PRICE)
                RAW_CATEGORY = doc.xpath(XPATH_CATEGORY)
                RAW_ORIGINAL_PRICE = doc.xpath(XPATH_ORIGINAL_PRICE)
                RAW_AVAILABILITY = doc.xpath(XPATH_AVAILABILITY)

                ## FILTERING DATA 
                ## Output: It depends on the ID, f -> string, s -> string, l -> list
                ASIN = filter_values(RAW_ASIN, 's')
                NAME = filter_values(RAW_NAME, 'f')
                AUTHOR = filter_values(RAW_AUTHOR, 's')
                STARS = filter_values(RAW_STARS, 's')
                ISBN13 = filter_values(RAW_ISBN13, 'f')
                ISBN10 = filter_values(RAW_ISBN10, 'f')
                SALE_PRICE = filter_values(RAW_SALE_PRICE, 's')
                ORIGINAL_PRICE = filter_values(RAW_ORIGINAL_PRICE, 's')
                CATEGORY = filter_values(RAW_CATEGORY, 'l')
                AVAILABILITY = filter_values(RAW_AVAILABILITY, 's')
                OBSERVATIONS = 'No errors'

                if not STARS:
                    STARS = '---'
                    OBSERVATIONS = 'Stars not found for this item'
                if not ASIN:
                    ASIN = ISBN10
                    OBSERVATIONS = 'ASIN number not found'
                if not ISBN10:
                    ISBN10 = ASIN
                    OBSERVATIONS = 'ISBN10 not found'
                if not ISBN13:
                    ISBN13 = '---'
                    OBSERVATIONS = 'ISBN13 not found'
                if len(ISBN10) > len(ASIN):
                    ISBN10 = ASIN
                    OBSERVATIONS = 'Error in ISBN10'
                if not SALE_PRICE:
                    SALE_PRICE = ORIGINAL_PRICE
                    OBSERVATIONS = 'Sale price not found'
                if not ORIGINAL_PRICE:
                    ORIGINAL_PRICE = SALE_PRICE
                    OBSERVATIONS = 'Original price not found'
                if not NAME: # retrying in case of captcha
                    raise ValueError('captcha')
                if not CATEGORY:
                    CATEGORY = ['Uncategorized', 'Uncategorized', 'Uncategorized']
                    OBSERVATIONS = 'Category not found'
                if len(CATEGORY) == 2:
                    CATEGORY = [CATEGORY[0], CATEGORY[1], '---']
                    OBSERVATIONS = 'No subcategory'

                data = {
                    'ASIN': ASIN,
                    'NAME': NAME,
                    'AUTHOR': AUTHOR,
                    'STARS': STARS[0:3],
                    'ISBN13': ISBN13,
                    'ISBN10': ISBN10,
                    'SALE_PRICE': SALE_PRICE,
                    'ORIGINAL_PRICE': ORIGINAL_PRICE,
                    'ITEM_CATEGORY': CATEGORY[0],
                    'ITEM_SUBCATEGORY': CATEGORY[1],
                    'ITEM_SPECIFIC_CATEGORY': CATEGORY[2],
                    'AVAILABILITY': AVAILABILITY,
                    'URL': url,
                    'STATUS': 1,
                    'OBSERVATIONS': OBSERVATIONS
                }
                
                return data
                
            elif response.status_code == 404:
                break

    except Exception as e:
        print(e)