#!/usr/bin/env python3
import csv
import requests
from urllib.request import urlopen

import bs4

from bs4 import BeautifulSoup

headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
      }

urls='https://en.wikipedia.org/wiki/October_28' ##https://games.mail.ru/pc/games/calendar/2017-10-27/


page = requests.get (urls, headers=headers)
stp = requests.get (urls)
print (stp.status_code)
##<div id="main" class="tabcontent"
##print (page)

def parse_g(urls):
    results = []
    soup = BeautifulSoup (page)
    game_list = soup.find ('div', {'class': 'tabcontent'})
    ##games = game_list.findall ('div', {'class' : 'b-pc__cal-list-item'})
    ##for game in games:
        ##game_name = game.find('h3', {'class': 'b-pc__cal-list-title'}).find('a').text
        ##game_link = game.find('h3', {'class': 'b-pc__cal-list-title'}).find('a').get('href')
        ##game_plat = game.find ('div', {'class': 'b-pc__cal-list-release'}).text
        ##game_desc = game.find ('div', {'class': 'b-pc__cal-list-descr'}).text
        ##results.append({
            ##'game_name' : game_name,
            ##'game_link' : game_link,
            ##'game_plat' : game_plat,
            ##'game_desc' : game_desc
             ##})
    print (game_list)
parse_g(urls)


##print (soup)

##<div class="b-pc__cal-list-item"
##<div class="b-pc__cal-list-text">
##<h3 class="b-pc__cal-list-title">
##<div class="b-pc__cal-list-type">
