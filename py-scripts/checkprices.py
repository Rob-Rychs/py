# Script to scrape price of specific item or any item from amazon, snapdeal and flipkart
# Pranjal Saxena ( github.com/itsshady101 )

import requests, bs4

def find_price(item_name):

    prices = {}

    # Amazon: Find and scrape the price of first item( most probably right one if specific ex: cs go )
    re = requests.get('http://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords='+item_name)
    soup = bs4.BeautifulSoup(re.text, 'html.parser')
    price = soup.select('.a-size-base.a-color-price.s-price.a-text-bold')

    if len(price) > 0:
        price = price[0].getText().strip()
        prices['amazon'] = price
    
    # Snapdeal
    re = requests.get('http://www.snapdeal.com/search?keyword='+item_name)
    soup = bs4.BeautifulSoup(re.text, 'html.parser')
    price = soup.select('.product-price')
    if len(price) > 0:
        price = price[0].getText().strip()
        prices['snapdeal'] = price

    # Flipkart
    re = requests.get('http://www.flipkart.com/search?q='+item_name)
    soup = bs4.BeautifulSoup(re.text, 'html.parser')
    price = soup.select('.pu-final')
    if len(price) > 0:
        price = price[0].getText().strip()
        prices['flipkart'] = price

    return prices


prices = find_price('cs go')
print('Amazon: ' + prices['amazon'])
print('Snapdeal: ' + prices['snapdeal'])
print('Flipkart: ' + prices['flipkart'])
