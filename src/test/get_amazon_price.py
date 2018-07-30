#-*-coding:gbk -*-
import urllib
import lxml.html
import requests
from bs4 import BeautifulSoup


def amazon_price(url, user_agent):
    kv = {'user-agent': user_agent}
    request = requests.get(url, headers = kv)
    content = request.content
    soup = BeautifulSoup(content, "html.parser")
    print(soup)

if __name__=="__main__":
    url = "https://www.amazon.cn/dp/B00RG87DUY/"
    user_agent = 'Mozilla/5.0'
    print(amazon_price(url, user_agent))