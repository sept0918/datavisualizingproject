from selenium import webdriver
from bs4 import BeautifulSoup
browser=webdriver.Chrome()
url=('https://comic.naver.com/webtoon?tab=mon')
browser.get(url)

html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')
