import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException
PATH="C:\chromedriver.exe"
driver=webdriver.Chrome(PATH)
driver.get("https://www.myntra.com/")
search=driver.find_element_by_class_name("desktop-searchBar")
search.send_keys("tshirt")
search.send_keys(Keys.RETURN)
try:
    output=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,"results-base")))
    source=driver.page_source
    soup=BeautifulSoup(source,'lxml')
    l=soup.find_all('li',class_='product-base')
    for op in l:
        pic=op.find('img',class_='img-responsive')['src']
        inf1=op.find('h3',class_='product-brand').text
        inf2=op.find('h4',class_='product-product').text
        inf3=op.find('span',class_='product-discountedPrice').text
        inf4=op.find('span',class_='product-strike').text
        inf5=op.find('span',class_='product-discountPercentage').text
        html_content=f'<html><head></head><body style="color:aqua;text-align:center;background-color:black;"> <img src={pic}> <div >{inf1}</div> <div>{inf2}</div><div>{inf3}</div> <div>{inf4}</div> <div>{inf5}</div></body></html>'
        with open("myntra.html","a") as html_file:
            html_file.write(html_content)
            print("html file created")
finally:
    driver.quit()
