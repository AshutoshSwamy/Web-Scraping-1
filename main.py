from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

WEBSITE_URL = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser = webdriver.Chrome('C:\Users\hp\OneDrive\Desktop\chromedriver')
browser.get(WEBSITE_URL)
time.sleep(10)

def scrap():
    headers = ['Name', 'Distance', 'Mass', 'Radius']
    stars_data = []
    for index in range(0, 439):
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        for th_tag in soup.find_all('th', attrs = {'class', 'stars'}):
            tr_tags = th_tag.find_all('tr')
            temp_list = []
            for index, tr_tag in enumerate(tr_tags):
                if index == 0:
                    temp_list.append(tr_tag.find_all('a')[0].contents[0])
                else:
                    try:
                        temp_list.append(tr_tag.contents[0])
                    except:
                        temp_list.append('')
            stars_data.append(temp_list)
    with open('scraper.csv', 'w') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(stars_data)
    scrap()