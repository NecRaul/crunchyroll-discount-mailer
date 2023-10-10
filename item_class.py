import variables
import requests
from bs4 import BeautifulSoup

class Item:
    def __init__(self, name, price, link):
        self.name = name
        self.price = price
        self.link = "https://store.crunchyroll.com" + link


# item array to contain items that we consider discounted
item_array = []

def find_discounted_item(url):
    r = requests.get(url)
    
    # parsing the content from the url with BeautifulSoup + lxml
    soup = BeautifulSoup(r.content, "lxml")
    
    # information about the items in the current wishlist
    items_content = soup.find_all("div", class_="cart-item-attributes-block")
    
    for item_content in items_content:
        # get item's price
        price_str = item_content.find("span", class_="sales").find("span", class_="value").get("content")
        # convert it to float
        price = float(price_str)
        if price < variables.base_price:
            item_element = item_content.find("a", class_="line-item-name")
            # get each item's name and link
            name = item_element.text.strip()
            link = item_element.get("href")
            # create new item based on these values
            item = Item(name, price, link)
            # add it to the item array
            item_array.append(item)
    return item_array