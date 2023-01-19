import pandas as pd
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import requests

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

url = 'https://www.amazon.in/s?k=laptop'

s = HTMLSession()
amazon_data=[]

for i in range(1,20):
    print('page is extracting = ',i)
    bas_url = 'https://www.amazon.in/s?k=laptop&page={i}'
    req = requests.get(bas_url,headers=headers)
    name = BeautifulSoup(req.content,'html.parser')
    
    for link in name.find_all('a',class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal", href=True):
        pro_link = 'https://www.amazon.in'+str(link['href'])
        pro_req = requests.get(pro_link,headers=headers)
        pro_soup = BeautifulSoup(pro_req.content,'html.parser')

        try:
            pro_title = pro_soup.find('span',id='productTitle').text.strip()
        except:
            pro_title='None'
        try:
            pro_price = pro_soup.find('span',class_='a-price-whole').text.strip()
        except:
            pro_price='None'
        try:
            pro_brand = pro_soup.find('tr',class_='a-spacing-small po-brand').text
        except:
            pro_brand='None'
        try:
            pro_model = pro_soup.find('tr',class_='a-spacing-small po-model_name').text
        except:
            pro_model='None'
        try:
            pro_display_size = pro_soup.find('tr',class_='a-spacing-small po-display.size').text
        except:
            pro_display_size='None'
        try:
            pro_CPU_model = pro_soup.find('tr',class_='a-spacing-small po-cpu_model.family').text
        except:
            pro_CPU_model='None'
        try:
            pro_RAM = pro_soup.find('tr',class_='a-spacing-small po-ram_memory.installed_size').text
        except:
            pro_RAM='None'
        try:
            pro_Operating = pro_soup.find('tr',class_='a-spacing-small po-operating_system').text
        except:
            pro_Operating='None'            
            

        items_m = {
            'Title':pro_title,
            'Price':pro_price,
            'Brand':pro_brand,
            'Model':pro_model,
            'Display Size':pro_display_size,
            'CPU Model':pro_CPU_model,
            'RAM':pro_RAM,
            'Operating system':pro_Operating
        }
        amazon_data.append(items_m)
        
with open('laptop_data.csv','a') as f:
    df = pd.DataFrame(amazon_data)
    df.to_csv('laptop_data.csv')