from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time
from dotenv import load_dotenv
import os

load_dotenv()

WEBSITE_LINK = "https://appbrewery.github.io/Zillow-Clone/"
FORM_LINK = os.getenv('FORM_LINK')


header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

responce = requests.get(url=WEBSITE_LINK, headers=header)
content = responce.text


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)


# get the rent info from the website, the price, address and the link.
class Rental_place:
    def __init__(self):
        self.soup = BeautifulSoup(content, "html.parser")

        self.driver = webdriver.Chrome(chrome_options)

        self.address = []
        self.links = []
        self.prices = []

    def get_web_data(self):
        # print(self.soup)
        # get the links of the listings
        link = self.soup.select(selector=".StyledPropertyCardDataArea-anchor")
        # print(link[2].get('href'))
        self.links = [i.get('href') for i in link]
        print(self.links)


        # get the address of all the listings in a list.
        address = self.soup.select(selector='.StyledPropertyCardDataArea-anchor address')
        # print(address[0].text)
        self.address = [j.text.strip() for j in address]
        print(self.address)


        # get all the prices of all the listings in the list.
        prices = self.soup.select(selector='.PropertyCardWrapper__StyledPriceLine')
        # print(prices[1].text)
        for price in prices:
            if '+' in price.text:
                price = price.text.split('+')
            elif '/' in price.text:
                price = price.text.split('/')
            self.prices.append(price[0])
        print(self.prices)



    # insert the data into a google form using selenium
    def insert_data(self):
        self.driver.get(FORM_LINK)

        for i in range(len(self.prices)):
            time.sleep(2)

            address = self.driver.find_element(By.XPATH, '//input[@aria-describedby = "i2 i3"]')
            address.send_keys(self.address[i])

            price = self.driver.find_element(By.XPATH, '//input[@aria-describedby = "i7 i8"]')
            price.send_keys(self.prices[i])

            link = self.driver.find_element(By.XPATH, '//input[@aria-describedby = "i12 i13"]')
            link.send_keys(self.links[i])

            submit = self.driver.find_element(By.XPATH, '//div[@aria-label = "Submit"]')
            submit.click()


            repeat_link = self.driver.find_element(By.XPATH, '//a[contains(text(), "Submit another response")]')
            repeat_link.click()






rs = Rental_place()
rs.get_web_data()
rs.insert_data()
