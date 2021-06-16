# -*-coding: utf-8-*-

import sys
import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import pyarabic as araby
import datetime
import time
session=HTMLSession()

bot_token = '1635482629:AAFBJjhx2tipAi3kNs7YiGK_GmrwAvoioUA'
chat_id = '1712954683'

def sendtele(chat_id,msg):
	url1= 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'.format(bot_token,chat_id,msg)
	requests.get(url1)

goldpoundurl='https://market.isagha.com/'
golddolarurl='https://goldprice.org/gold-price-today'
usdpoundurl='https://www.google.com/search?q=%D8%B3%D8%B9%D8%B1+%D8%A7%D9%84%D8%AF%D9%88%D9%84%D8%A7%D8%B1+%D8%A7%D9%84%D9%8A%D9%88%D9%85&client=ubuntu&hs=XG1&channel=fs&ei=bByEYJjVOaS0gwfK9Y7QBg&oq=%D8%B3%D8%B9%D8%B1+%D8%A7%D9%84%D8%AF%D9%88%D9%84%D8%A7%D8%B1&gs_lcp=Cgdnd3Mtd2l6EAMYADIKCAAQsQMQRhCCAjIFCAAQsQMyBQgAELEDMgUIABCxAzIICAAQsQMQgwEyAggAMgUIABCxAzIFCAAQsQMyAggAMggIABCxAxCDAToHCAAQRxCwAzoHCAAQsAMQQzoECAAQQzoHCAAQsQMQQ1DVhANY76IDYPu1A2gGcAJ4AIAB2QmIAf09kgELMy0xLjEuMC4zLjSYAQCgAQGqAQdnd3Mtd2l6yAEKwAEB&sclient=gws-wiz'



#while True:
msg=''
goldpoundr=session.get(goldpoundurl)
golddolarr=session.get(golddolarurl)
usdpoundr=session.get(usdpoundurl)

soup_gold_pound=BeautifulSoup(goldpoundr.content, 'lxml')
soup_gold_dolar=BeautifulSoup(golddolarr.content, 'lxml')
soup_dolar_pound=BeautifulSoup(usdpoundr.content, 'lxml')

gold_price_pound=soup_gold_pound.find('td', {'class':'header-price-item'}).text.strip()
gold_price_dolar=soup_gold_dolar.find('td', {'class':'text-right'}).text.strip()
dolar_price_pound=soup_dolar_pound.find('span',{'class':'DFlfde SwHCTb'}).text.strip()


a=round((float(gold_price_dolar)/31.103/8*7),3)

msg+= str((datetime.date.today()))+'\n'
msg+= ('gold price in EGP: '+gold_price_pound)[0:22]+'\n'
msg+= ('gold price in USD: ' + str(a)+'\n')
msg+= ('dolar price in EGP: '+dolar_price_pound)

print (msg)
sendtele(chat_id,msg)
#time.sleep(3576)

