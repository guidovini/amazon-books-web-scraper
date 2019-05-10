# ─── LIBRARIES ──────────────────────────────────────────────────────────────────
from random import randint
random_delays = randint(1, 20)


# ─── PROGRAM VARIABLES ──────────────────────────────────────────────────────────
headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'
          }

input_path = './data/input.csv'
output_path = './data/output.csv'
books_to_scrape = 35


# ─── XPATH VARIABLES ────────────────────────────────────────────────────────────
XPATH_NAME = '//h1[@id="title"]//text()'

XPATH_SALE_PRICE = '//span[contains(@id,"ourprice") or                                                                                  contains(@id,"saleprice")]/text() |                                                                   /*[@id="buyNewSection"]/h5/div/div[2]/div/span[2]/text() |                                                   //*[@id="buyNewSection"]/a/h5/div/div[2]/div/span[2]/text() |                                                //*[@id="priceblock_ourprice"]/text() |                                                                      //*[@id="newOfferAccordionRow"]/div/div[1]/a/h5/div/div[2]/span[2]/text()'

XPATH_ORIGINAL_PRICE = '//td[contains(text(),"List Price") or                                                                             contains(text(),"M.R.P") or                                                                                  contains(text(),"Price")]/following-sibling::span/text() |                                              //*[@id="price"]/table/tbody/tr[1]/td[2]/span[1]//text() |                                                   //*[@id="buyBoxInner"]/div/div[1]/ul/li[1]/span/span[2]/text() |                                             //*[@id="outOfStock"]/div/div[1]/span/text() |                                                               //*[@id="buyNew_noncbb"]/span/text() |                                                                       //*[@id="addToCart"]/div[1]/span[1]/span[2]/text() |                                                         //*[@id="usedBuySection"]/h5/div/div[2]/div/span[2]/text()' 

XPATH_AUTHOR = '//*[@id="bylineInfo"]/span/span[1]/a[1]/text() |                                                             //*[@id="bylineInfo"]/span/a/text()'

XPATH_STARS = '//*[@id="acrPopover"]/span[1]/a/i[1]/span/text()'

XPATH_ISBN13 = '//*[@id="isbn_feature_div"]/div/div[1]/span[2]/text() |                                                      //b[contains(text(), "ISBN-13")]/../text()'

XPATH_ISBN10 = '//*[@id="isbn_feature_div"]/div/div[2]/span[2]/text() |                                                      //b[contains(text(), "ISBN-10")]/../text()'

XPATH_ASIN = '//b[contains(text(), "ASIN")]/../text()'

XPATH_CATEGORY = '//a[@class="a-link-normal a-color-tertiary"]//text()'

XPATH_AVAILABILITY = '//div[@id="availability"]//text()'

fieldnames = [
                'NAME',
                'AUTHOR',
                'STARS',
                'ISBN13',
                'ISBN10',
                'SALE_PRICE',
                'ORIGINAL_PRICE',                                                                           
                'ITEM_SUBCATEGORY',
                'ITEM_SPECIFIC_CATEGORY',
                'AVAILABILITY', 
                'ASIN',                                                                                  
                'URL', 
                'STATUS',
                'OBSERVATIONS'
              ]