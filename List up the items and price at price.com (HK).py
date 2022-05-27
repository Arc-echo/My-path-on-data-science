import requests 
from bs4 import BeautifulSoup

def price_dot_com (brand):
    
    website = "https://www.price.com.hk/search.php?g=A&q=" + brand + "&page=1"
    r = requests.get(website)
    soup = BeautifulSoup(r.text)
    
    # create a variable to update the pages of website later on (try/except if only one page)
    try:
        # get how many pages
        pages = int(soup.find("div", {"class" : "pagination-total"}).text.strip()[1: -1])
        website_end = 1
        
    except:
        website_end = 1
        pages = 1
        
    d = dict()

    # for each page, crawl info
    while pages > 0:
        
    # locate product name, price and update those into the dictinary

        for product in soup.findAll("div", {"class" : "item club-list-row"}):
            product_name = product.find("div", {"class" : "line line-01"}).text.strip()
            
            #Since None type may be appear in the price tag, add a try/ except to prevent errors
            try:
                product_price = product.find("span", {"class" : "product-price-text"}).text.strip()
            except AttributeError:
                pass
    
            d[product_name] = product_price
        
        pages -= 1

        # update the website to the next page
        try:
            website_end += 1
            if website_end <= 10:
                website = website.replace(website[-1], str(website_end))

            else:
                website = website.replace(website[-2:], str(website_end))
        except:
            pass
        
        r = requests.get(website)
        soup = BeautifulSoup(r.text)
        
        continue
                                
# return the result to list of dictionary
    return d
