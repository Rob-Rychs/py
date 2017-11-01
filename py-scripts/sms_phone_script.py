# -*- coding: utf-8 -*-
import plivo
from lxml import html
import requests
import schedule
import time

def scriptfile():
    page = requests.get('https://finance.yahoo.com/quote/AAPL?ltr=1')

    tree = html.fromstring(page.content)

    price = tree.xpath('//*[@id="quote-header-info"]/div[2]/div[1]/section/span[1]/text()')
    change = tree.xpath('//*[@id="quote-header-info"]/div[2]/div[1]/section/span[2]/text()')
    time = tree.xpath('//*[@id="quote-market-notice"]/span/text()')
    opentoday = tree.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[1]/td[2]/text()')
    daysrange = tree.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[5]/td[2]/text()')
    closeprev = tree.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[2]/td[2]/text()')

    auth_id = "XXX"
    auth_token = "XXX"

    p = plivo.RestAPI(auth_id, auth_token)

    for a, b, c, d, e, f in zip(price, change, time, opentoday, daysrange, closeprev):
        a = "Current: $" + a
        b = "Change: " + b
        c = c.replace(" EDT","",1)
        d = "Open: $" + d
        e = "Range: $(" + e + ")"
        f = "Prev close: $" + f
        params = {
        'src': 'XXXXXXXXXX',
        'dst' : 'XXXXXXXXXX',
        'text' : u"AAPL"+"\n"+a+"\n"+b+"\n"+c+"\n\n"+d+"\n"+e+"\n"+f,
        'log' : 'false'
        }
        response = p.send_message(params)
        print "message sent"
        print response

if __name__ == '__main__':
    schedule.every().monday.at("09:30").do(scriptfile)
    schedule.every().tuesday.at("09:30").do(scriptfile)
    schedule.every().wednesday.at("09:30").do(scriptfile)
    schedule.every().thursday.at("09:30").do(scriptfile)
    schedule.every().friday.at("09:30").do(scriptfile)

while True:
    schedule.run_pending()
    time.sleep(1)
