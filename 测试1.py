# -*- coding:utf-8 -*-

from selenium  import webdriver

url = 'https://www.pinterest.com/'
driver = webdriver.Firefox()

for img  in driver.find_elements_by_xpath("//div[@class='TPW xEW']//img"):
       img_src = img.get_attribute("src")
       print(img_src)
