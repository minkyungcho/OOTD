#-*- coding: utf-8 -*-
#-*- coding: euc-kr -*-
# -- coding: utf-8 --
from django.shortcuts import render, redirect
import requests, json
from bs4 import BeautifulSoup
import os
from PIL import Image
import requests

# Create your views here.
def index(request):

    return render(request, 'index.html')

def link(request, category_id):

    # url = 'https://cf-api-c.brandi.me/v1/web/categories/3/products?offset=0&limit=100&order=popular&type=all&order=popular'
    url = f'https://cf-api-c.brandi.me/v1/web/categories/{category_id}/products?offset=0&limit=100&order=popular&type=all&order=popular'

    headers = {
        # 'authority': 'cf-api-c.brandi.me',
        # 'method': 'GET',
        # 'path': '/v1/web/categories/3/products?offset=0&limit=100&order=popular&type=all&order=popular',
        # 'scheme': 'https',
        # 'accept': 'application/json, text/plain, */*',
        # 'accept-encoding': 'gzip, deflate, br',
        # 'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization': '3b17176f2eb5fdffb9bafdcc3e4bc192b013813caddccd0aad20c23ed272f076_1423639497',
        # 'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
        # 'cookie': 'PHPSESSID=s10jgtah1vq3v4kju4t39hpqut',
        # 'origin': 'https://www.brandi.co.kr',
        # 'referer': 'https://www.brandi.co.kr/categories/3',
        # 'sec-fetch-mode': 'cors',
        # 'sec-fetch-site': 'cross-site',
        # 'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    print(response)
    
    data = response.json()

    dics = data['data']
    for dic in dics:
        idd = dic['id']
        # print(idd)
        name = dic['name']
        # print(name)
    context = {
        'dics': dics
        # 'product_id': dic
    }
    return render(request, 'link.html', context)

def product(request, product_id):
    url = f'https://cf-api-c.brandi.me/v1/web/products/{product_id}?res-type=section1'
    # url = 'https://cf-api-c.brandi.me/v1/web/products/11339428?res-type=section1'
    headers = {
        'authorization': '3b17176f2eb5fdffb9bafdcc3e4bc192b013813caddccd0aad20c23ed272f076_1423639497'
    }
    response = requests.get(url, headers=headers)
    print(response)
    
    data = response.json()
    # products = data[]
    # print(data["data"]["category_hierarchies"])
    category_hierarchies = data["data"]["category_hierarchies"]
    options = data["data"]["options"]
    colors = []
    # if len(options) > 1:
    #     for option in options:
    #         if len(option["attributes"]) > 1:
    #             a = option["attributes"][0]["value"]
    #             print(a)
    #             if a in colors:
    #                 continue
    #             colors.append(a)        
    for option in options:
        a = option["attributes"][0]["title"]
        b = option["attributes"][0]["value"]
        if a == "색상" or a == "색상1" or a == "color" or a == "COLOR" or a == "Color" or a == "컬러" or a == "컬러1":
            # print(a+" "+b)
            if b in colors:
                continue
            colors.append(b)

        
    # print(colors)
        # attributes = data["data"]["options"][0]["attributes"]
    # attributes = data["data"]["options"][0]["attributes"]
    # for attr in attributes:
        # print(attr)
    category = category_hierarchies[0]['name']
    length = len(category_hierarchies)
    if length == 2:
        category_type = category_hierarchies[1]['name']
    else:
        category_type = category
    # print(category+" "+category_type+" "+str(length))
    # print(len(colors))

    products = []
    if len(colors)>=1:
        for color in colors:
            temp = {
                "id": product_id,
                "category": category,
                "category_type": category_type,
                "color": color
            }
            products.append(temp)
    else:
        temp = {
            "id": product_id,
            "category": category,
            "category_type": category_type,
            "color": '-'
        }
        products.append(temp)
    
    context = {
        'products': products,
        'product_id': product_id
    }
    
    return render(request, 'product.html', context)

def detail(request, product_id):
    url = f'https://cf-api-c.brandi.me/v1/web/products/{product_id}?res-type=section1'
    headers = {
        'authorization': '3b17176f2eb5fdffb9bafdcc3e4bc192b013813caddccd0aad20c23ed272f076_1423639497'
    }
    response = requests.get(url, headers=headers)
    print(response)
    data = response.json()
    image_urls = data["data"]["images"]
    # print(image_urls)
    images = []
    for image_url in image_urls:
        temp = image_url["image_url"]
        images.append(temp)
    # print(images)
    filenames = []
    for image in images:
        img = requests.get(image).content
        filename = os.path.basename(image)
        filenames.append(filename)
        with open(filename, 'wb') as f:
            f.write(img)
    # print(filenames)
    
    context = {
        'images': images,
        'filenames': filenames
    }
    return render(request, 'detail.html', context)
