# ─── LIBRARIES ──────────────────────────────────────────────────────────────────
import csv
import pandas as pd
import xlrd
import re



# ─── LOCAL MODULES ──────────────────────────────────────────────────────────────
from variables import url_file_path, number_of_books



# ─── VARIABLES ──────────────────────────────────────────────────────────────────
excel_file_path = './sources/url_grabber.xlsm'

regex = re.compile(r"(amazon.|amzn.)(com|co\.uk|ca|de|fr|es|it|cn|co\.jp).*\/(asin|dp|gp|product|exec\/obidos|gp\/offer-listing|product\-reviews|gp\/aw\/d)\/([A-Z0-9]{10,13})")


# ─── PROGRAM ────────────────────────────────────────────────────────────────────
## Reads original excel file and saves it to csv.
def generate_url_file():
    excel_file = pd.read_excel(excel_file_path)
    df = pd.DataFrame(excel_file)
    df.to_csv(url_file_path)

# generate_url_file()
    
## Reads new csv file, grabs the URL column, grabs a certain number of rows, and returns a list. 
def read_url_file(url_file_path, number_of_books):
    url_file = pd.read_csv(url_file_path)
    df = pd.DataFrame(url_file)
    # books_list = df['url'].values.tolist()
    books_list = df['url'].loc[:number_of_books-1].values.tolist() # Test
    return books_list


## Reads list from read_url_file(), filters ASIN from it, and returns a list of ASIN.
## batch is a list of amazon urls, e.g. ['www.amazon.com/dp/XW2X2X/','',...]
def filter_url_batch(batch):
    data = []

    for url in batch:
        try:
            asin = regex.search(url).group(4)
            data.append(asin)

        except Exception as e:
            print('------')
            print('Exception occurred while filtering URL: ', e)
            print('Problem with: ', url)

    return data