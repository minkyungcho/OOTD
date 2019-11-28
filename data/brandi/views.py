#-*- coding: utf-8 -*-
#-*- coding: euc-kr -*-
# -- coding: utf-8 --
from django.shortcuts import render, redirect
import requests, json
from bs4 import BeautifulSoup

# Create your views here.
def index(request):
    # url1 = 'https://cf-api-c.brandi.me/v1/web/categories/3/'
    # url = 'https://www.brandi.co.kr/categories/33'
    # url = 'https://cf-api-c.brandi.me/v1/web/main'
    url = 'https://cf-api-c.brandi.me/v1/web/categories/3/products?offset=0&limit=100&order=popular&type=all&order=popular'
    # url2 = 'https://cf-api-c.brandi.me/v1/web/categories/2/products?offset=0&limit=100&order=popular&type=all&order=popular'
    # url3 = 'https://cf-api-c.brandi.me/v1/web/categories/47/products?offset=0&limit=100&order=popular&type=all&order=popular'
    # url4 = 'https://cf-api-c.brandi.me/v1/web/categories/50/products?offset=0&limit=100&order=popular&type=all&order=popular'
    headers = {
        'authority': 'cf-api-c.brandi.me',
        'method': 'GET',
        'path': '/v1/web/categories/3/products?offset=0&limit=100&order=popular&type=all&order=popular',
        'scheme': 'https',
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization': '3b17176f2eb5fdffb9bafdcc3e4bc192b013813caddccd0aad20c23ed272f076_1423639497',
        'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
        'cookie': 'PHPSESSID=s10jgtah1vq3v4kju4t39hpqut',
        'origin': 'https://www.brandi.co.kr',
        'referer': 'https://www.brandi.co.kr/categories/3',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    print(response)
    
    data = response.json()
    print(data['data']['id'])
    # print(response.text)
    
    html = BeautifulSoup(response.text, 'html.parser')
    product_names = html.select('ul li.list_title')
    # for product in product_names:
    #     print(product.text)
    # context = {
    #     # app > div > div.frame > div.content_right > div > div.list_full > ul:nth-child(1)
    #     # document.querySelector("#app > div > div.frame > div.content_right > div > div.list_full > ul:nth-child(1) > li.list_title")
    # }
    # print(response)
    # return render(request, 'index.html', )
    return ''