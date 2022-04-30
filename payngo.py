from bs4 import BeautifulSoup
import requests # call to the site 

html_text=requests.get('https://www.payngo.co.il/computers-pcs/computing-gaming/laptops.html').text # call to the site 
soup = BeautifulSoup(html_text, 'lxml')# scan the html text
products = soup.find_all('li',class_='item product product-item product-item-5')#'li' is the attributes that contain the products on site.

for product in products:
    price = product.find('span',class_='price').text.replace(' ', '')# span - is attributes that contain the price
    computer_type = product.find('strong', class_='product name product-item-name product_name').text.replace(' ','')
    more_info = product.div.a['href']
    print(f"Type Name:{computer_type.strip()}")
    print(f"Price:{price}")
    print(f"More Info:{more_info}")
    print(" ")



