import pandas as pd
import numpy as np
from selenium import webdriver
from bs4 import BeautifulSoup
browser=webdriver.Chrome()
url=('https://comic.naver.com/webtoon?tab=mon')
browser.get(url)

html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')

html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')
counts = len(soup.select('#content > div:nth-child(1) > ul')[0]) #해당 요일 웹툰 수

import time
monday = []
for i in range(1, counts+1):
    x = browser.find_elements('xpath', f'//*[@id="content"]/div[1]/ul/li[{i}]/div')[0].text.split('\n')
    if '휴재' in x:
        x.remove('휴재')
    if '별점' in x:
        x.remove('별점')
    if 'UP' in x:
        x.remove('UP')
      
    browser.find_elements('xpath', f'//*[@id="content"]/div[1]/ul/li[{i}]/a')[0].click() #웹툰 클릭
    time.sleep(1)
    tag = browser.find_elements('xpath','//*[@id="content"]/div[1]/div/div[2]/div')[0].text#태그
    like = browser.find_elements('xpath','//*[@id="content"]/div[2]/div/button[1]/span[2]')[0].text #관심수
    browser.find_element('css selector',"""
    #content > div.EpisodeListView__episode_list_wrap--q0VYg > div.EpisodeListView__episode_list_head--PapRv 
    > div.EpisodeListView__tab_control--qqhjW > button:nth-child(2)""").click() #첫 화 클릭
    time.sleep(1)
    starting_date = browser.find_elements('xpath','//*[@id="content"]/div[3]/ul/li[1]/a/div[2]/div/span[2]')[0].text #연재시작일
    monday.append([x[0], x[1], x[2], tag, like, starting_date])
    
    browser.get(url) #월요 웹툰 화면으로 돌아가기
    time.sleep(1)
    if i == 93:
        break
monday

#성인 웹툰의 경우 로그인이 필요한데 자동로그인을 네이버 웹툰 홈페이지에서 막아둔 관계로 요일별로 위의 과정을 반복