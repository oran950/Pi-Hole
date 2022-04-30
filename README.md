# Web-Scraping

from bs4 import BeautifulSoup
import requests

html_text=requests.get('https://www.payngo.co.il/computers-pcs/computing-gaming/laptops.html').text
soup = BeautifulSoup(html_text, 'lxml')
products = soup.find_all('li',class_='item product product-item product-item-5')

for product in products:
    price = product.find('span',class_='price').text.replace(' ', '')
    computer_type = product.find('strong', class_='product name product-item-name product_name').text.replace(' ','')
    more_info = product.div.a['href']
    print(f"Type Name:{computer_type.strip()}")
    print(f"Price:{price}")
    print(f"More Info:{more_info}")
    print(" ")



