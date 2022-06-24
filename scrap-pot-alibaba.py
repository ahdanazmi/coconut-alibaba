from selenium import webdriver
import time
import json

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")# this is to make the chrome tab will not pop up. the scrapping run in background
number_page= 21 # number of page from pagination
output=[]

for i in range (number_page):
    i= i+1
    url= "https://www.alibaba.com/trade/search?IndexArea=product_en&SearchText=coconut_coir_pot&page="+ str(i) +"&viewtype=L&f0=y"

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(10) # wait 10 sec for my browser completely load he page . you can change the number

    #to scroll and load items in javascript
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(60) 

    #collecting data

    items = driver.find_elements_by_css_selector(".J-offer-wrapper")
       
    
    for j in items:
        try:        #use try-except so the program will not stop if didnt find the expected element
            product_name = j.find_element_by_css_selector("h2").text
        except:
            product_name = None
        try:    
            price = j.find_element_by_css_selector(".elements-offer-price-normal__promotion").text
        except:
            price = None
        try:    
            MOQ = j.find_element_by_css_selector(".element-offer-minorder-normal__value").text
        except:
            MOQ = None
        try:
            img_div = j.find_element_by_css_selector(".seb-img-switcher__imgs")
            img_url = img_div.get_attribute("data-image")
            img_url = "https:" + img_url
            img_url = img_url.replace("_300x300.jpg", "")
        except:
            img_url: None        
        try:    
            country = j.find_element_by_css_selector(".seller-tag__country").text
        except:
            country = None
        try:
            product_link = j.find_element_by_css_selector("h2.elements-title-normal__outter > a").get_attribute('href')
        except:
            product_link = None
       


        #print(price,MOQ, product_name, img_url)
        output_item ={
        "name" : product_name,
        "product_link" : product_link,
        "price" : price,
        "MOQ" :MOQ,
        "country":country,
        "img_url" : img_url,
    
        }
        output.append(output_item)
    
    driver.close()

json.dump(output,open("pot.json","w"), indent=2) #name your file in .json
