#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Joveoo_ads_indeed2.py
#  
#  Copyright 2018 raja <raja@raja-Inspiron-N5110>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
# 
import mechanize,requests
import cookielib
from BeautifulSoup import BeautifulSoup
import html2text 
from selenium import webdriver
from pandas.io.html import read_html

# Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(False)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.addheaders = [('User-agent', 'Firefox')]


url = 'https://secure.indeed.com/account/login?service=emp&hl=en_IN&co=IN&continue=https%3A%2F%2Fads.indeed.com%2F'
driver = webdriver.Firefox()
driver.get(url)
username = driver.find_element_by_name('__email')
password = driver.find_element_by_name('__password')
username.send_keys('MUFGBidding@indeedagencyrelations.com')
password.send_keys('unionbank.17')
password.submit()


#driver.get("https://ads.indeed.com/job/ads") #navigate to page behind login
#innerHTML = driver.execute_script("return document.body.innerHTML") #returns the inner HTML as a string

#print innerHTML
res=(br.open('https://ads.indeed.com/job/ads').read())
#res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

driver.get('https://ads.indeed.com/job/ads')
print driver.page_source
#table = driver.find_element_by_id('sjc_table')
#table_html = table.get_attribute('tbody')
driver.close()
#df = read_html(table_html)[0]
#print table_html


