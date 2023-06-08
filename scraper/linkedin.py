#scrape with selenium
# import selenium and beautiful soup
import pandas as pd
import numpy as np

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
# import service
from selenium.webdriver.chrome.service import Service
import time
import os
import requests
import shutil
import random

from bs4 import BeautifulSoup
from bs4.element import Comment

# chrome_options.add_argument("--headless")


class LinkedInScraper:
    def __init__(self,chrome_options_list = ["--window-size=1920x1080",],chrome_driver_path="",output_path="./") -> None:

        chrome_options = Options()
        [chrome_options.add_argument(option) for option in chrome_options_list]
        service = Service(executable_path=chrome_driver_path)

        self.chrome_driver_path = chrome_driver_path
        self.output_path = output_path
        self.driver = webdriver.Chrome(
            service=service, 
            options=chrome_options
            )
        
    

    def tag_visible(self,element):
        if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
            return False
        if isinstance(element, Comment):
            return False
        return True
    
    def text_from_html(self,body):
        soup = BeautifulSoup(body, 'html.parser')
        texts = soup.findAll(text=True)
        visible_texts = filter(self.tag_visible, texts)  
        return u" ".join(t.strip() for t in visible_texts)


        
    def scrape(self,url):
        linkedin_url = url
        # linkedin_url = "https://www.linkedin.com/in/andrewyng/"
        # open chrome
        self.driver.get(linkedin_url)
        # wait for page to load
        time.sleep(5)
        # scroll to bottom of page
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # wait for page to load
        time.sleep(5)
        # get page source
        html = self.driver.page_source
        # get text from html
        text = self.text_from_html(html)
        return text
    

if __name__ == "__main__":
    scraper = LinkedInScraper(chrome_driver_path="/Users/suchattangjarukij/Downloads/chromedriver_mac_arm64\ 2/chromedriver")
    text = scraper.scrape("https://www.linkedin.com/in/andrewyng/")
    # save to txt
    with open("linkedin.txt","w") as f:
        f.write(text)
