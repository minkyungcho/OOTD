#-*- coding: utf-8 -*-
#-*- coding: euc-kr -*-
# -- coding: utf-8 --
from django.shortcuts import render, redirect
import requests, json
from bs4 import BeautifulSoup
import os
from PIL import Image
import requests
from .models import Cloth, Closet, Category, Month, Temp
from django.db.models import Q
import random
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
    context = {
        'dics': dics
    }
    return render(request, 'link.html', context)

def product(request, product_id):
    url = f'https://cf-api-c.brandi.me/v1/web/products/{product_id}?res-type=section1'
    headers = {
        'authorization': '3b17176f2eb5fdffb9bafdcc3e4bc192b013813caddccd0aad20c23ed272f076_1423639497'
    }
    response = requests.get(url, headers=headers)
    print(response)
    
    data = response.json()
    category_hierarchies = data["data"]["category_hierarchies"]
    options = data["data"]["options"]
    colors = []      
    for option in options:
        a = option["attributes"][0]["title"]
        b = option["attributes"][0]["value"]
        if a == "색상" or a == "색상1" or a == "color" or a == "COLOR" or a == "Color" or a == "컬러" or a == "컬러1":
            if b in colors:
                continue
            colors.append(b)
    category = category_hierarchies[0]['name']
    length = len(category_hierarchies)
    if length == 2:
        category_type = category_hierarchies[1]['name']
    else:
        category_type = category

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

    ########################
    # 이미지 url만 저장 근데 이걸로 이미지 불러올수 있음
    image_urls = data["data"]["images"]
    # print(image_urls)
    images = []
    images_thumbnail = []
    imglists = []
    for image_url in image_urls:
        img = image_url["image_url"]
        img_th = image_url["image_thumbnail_url"]
        images.append(img)
        images_thumbnail.append(img_th)
        imglist = [img, img_th]
        imglists.append(imglist)
        
    filenames = []
    # 이미지 저장
    # for image in images:
    #     img = requests.get(image).content
    #     filename = os.path.basename(image)
    #     filenames.append(filename)
    #     with open(filename, 'wb') as f:
    #         f.write(img)
    # print(filenames)

    context = {
        'products': products,
        'product_id': product_id,
        'images': images,
        'images_thumbnail': images_thumbnail,
        'imglists': imglists,
        'filenames': filenames
    }
    return render(request, 'product.html', context)


def data(request):
    product_id = request.POST["ProductId"]
    category = request.POST["ProductCategory"]
    cate_type = request.POST["ProductCategoryType"]
    color = request.POST["ProductColor"]
    pattern = request.POST["ProductPattern"]
    months = request.POST.getlist('ProductMonth')
    temp = request.POST["ProductTemp"]
    label = request.POST["ProductLabel"]
    img_url = request.POST["img_url"]
    img_th_url = request.POST["img_th_url"]
    clothes = []
    cate_id = ''
    if category == "아우터":
        cate_id = 2
    elif category == "상의":
        cate_id = 1
    elif category == "스커트":
        cate_id = 3
    elif category == "바지":
        cate_id = 4
    elif category == "원피스":
        cate_id = 5
    for mon in months:
        cloth = Cloth(product_id=product_id, category=Category(id=cate_id), cloth_type=cate_type, color=color, pattern=pattern, month=Month(id=mon), temp=Temp(id=temp), label=label, img_url=img_url)
        cloth.save()
        # temp = {
        #     "product_id": product_id,
        #     "category": category,
        #     "category_type": cate_type,
        #     "color": color,
        #     "pattern": pattern,
        #     "month": mon,
        #     "temp": temp,
        #     "label": label,
        #     "img_url": img_url
        #     }
        # clothes.append(temp)
        
    # print("###############")
    # print(product_id)
    # print(category)
    # print(cate_type)
    # print(color)
    # print(pattern)
    # print(month)
    # print(temp)
    # print(label)
    # print(img_url)
    cloth_all = Cloth.objects.all()
    # print(cloth_all)
    context = {
        'clothes': clothes,
        'cloth_all': cloth_all
    }
    return render(request, 'data.html', context)

def detail(request, product_id):
    url = f'https://cf-api-c.brandi.me/v1/web/products/{product_id}?res-type=section1'
    headers = {
        'authorization': '3b17176f2eb5fdffb9bafdcc3e4bc192b013813caddccd0aad20c23ed272f076_1423639497'
    }
    response = requests.get(url, headers=headers)
    print(response)
    data = response.json()
    image_urls = data["data"]["images"]
    images = []
    for image_url in image_urls:
        temp = image_url["image_url"]
        images.append(temp)
    filenames = []
    # for image in images:
    #     img = requests.get(image).content
    #     filename = os.path.basename(image)
    #     filenames.append(filename)
    #     with open(filename, 'wb') as f:
    #         f.write(img)
    
    context = {
        'images': images,
        'filenames': filenames
    }
    return render(request, 'detail.html', context)

def world(request):
    month = 10
    temp = 3
    top = Cloth.objects.filter(category_id = 1)
    bottom = Cloth.objects.filter(Q(category_id = 3)|Q(category_id=4))
    outer = Cloth.objects.filter(category_id = 2)
    onepiece = Cloth.objects.filter(category_id = 5)
    ran_top = random.sample(list(top),4)
    ran_bot = random.sample(list(bottom),4)
    ran_out = random.sample(list(outer),4)
    ran_one = random.sample(list(onepiece),2)

    top1=ran_top[:2]
    top2=ran_top[2:4]
    bot1=ran_bot[:2]
    bot2=ran_bot[2:4]
    out1=ran_out[:2]
    out2=ran_out[2:4]

    
    context ={
        'top1':top1,
        'top2':top2,
        'bot1':bot1,
        'bot2':bot2,
        'out1':out1,
        'out2':out2,
        'ran_one':ran_one,
    }
    return render(request , 'world_cup.html',context)

