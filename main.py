import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup
from time import sleep

class Torrent:
    def __init__(self,url='https://www.1377x.to/',movie_name='The terminal'):
        self.error = False
        self.url = url
        self.movie_name=movie_name
        self.driver = ''
        self.connection_establishment()
        if self.error is False:
            self.main_site()
        if self.error is False:
            self.search_for_movie()
        if self.error is False:
            self.magnet_download()

    def connection_establishment(self):
        try:
            chrome_options = Options()
            chrome_options.add_experimental_option("prefs", {'protocol_handler.allowed_origin_protocol_pairs': 
            {"https://www.1377x.to":{"magnet": True}}})
            self.driver = webdriver.Chrome('E:\\Programming Courses\\chromedriver\\chromedriver',options=chrome_options)
        except Exception as e:
            print('Error occured')
            print(e)
            self.error = True
    
    def main_site(self):
        try:
            self.driver.get(self.url)
            main_site = self.driver.find_element_by_xpath('/html/body/main/div/div/div[3]/div/div[2]/p/a[1]')
            main_site.click()
        except Exception as e:
            print('Error occured')
            print(e)
            self.error = True
    
    def search_for_movie(self):
        try:
            search_bar = self.driver.find_element_by_xpath('//*[@id="autocomplete"]')
            search_bar.send_keys(self.movie_name)
            search_bar.submit()
            soup = BeautifulSoup(self.driver.page_source,'lxml')
            movie_names = soup.find_all('td',attrs={'class':'coll-1 name'})
            movie_url = self.url + movie_names[0].a.next_sibling['href']
            print(movie_url)
            self.driver.get(movie_url)
        except Exception as e:
            print('Error occured')
            print(e)
            self.error = True
    def magnet_download(self):
        try:
            magnet_downlaod = self.driver.find_element_by_xpath('/html/body/main/div/div/div/div[2]/div[1]/ul[1]/li[1]/a')
            magnet_downlaod.click()
            sleep(5)
            self.driver.close()
        except Exception as e:
            print('Error occured')
            print(e)
            self.error = True

if __name__=='__main__':
    Torrent()

