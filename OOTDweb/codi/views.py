import json
import math
import random
import requests
from django.shortcuts import render , HttpResponse, redirect
from datetime import datetime
from urllib.request import urlopen
from .weather1 import get_tmn_data , get_tmx_data
from .weather2 import get_forecast_data , ForecastTimeData
from .models import Cloth
from PIL import Image
from django.db.models import Q
from .models import Cloth, Closet, Category, Month, Temp
from django.contrib.auth.decorators import login_required # 로그인권한부여
from .models import Article

def home(request):
    articles = Article.objects.all().order_by("created_at").reverse()
    recent_codibook = {
        'articles': articles
    }
    return render(request, 'index.html', recent_codibook)

@login_required
def codiWorldcup(request):
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

    
    context1 ={
        'top1':top1,
        'top2':top2,
        'bot1':bot1,
        'bot2':bot2,
        'out1':out1,
        'out2':out2,
        'ran_one':ran_one,
    }
    a = [1,2]
    context = {
        'top1':a, 
        'top2':a ,
        'bot1':a ,
        'bot2':a ,
        'out1':a ,
        'out2':a ,
        'ran_one':a 
    }
    return render(request, 'codi/codiWorldcup.html', context1)

@login_required
def codiBook(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            article = Article()
            article.contents = request.POST['contents']
            article.user_id = request.user.id  
            article.save()

            # 원본 이미지 저장
            article.image = request.FILES['image'] 
            # 원본 이미지를 프로세싱 한 이미지 저장
            # article.image_resized = request.FILES["image"]
            article.save(0)
            # for image in request.FILES.getlist("image"):
            #     ArticleImages.objects.create(article_id=article.id, image=image)
            return redirect('codi:codiBook')
        else:
            return redirect('codi:codi')
    else:
        id = request.user.id
        articles = Article.objects.filter(user_id=id).order_by("created_at").reverse()
        # articles = Article.objects.all().order_by("created_at").reverse()
        context = {
            'articles': articles
        }
        return render(request, 'codi/codiBook.html', context)

@login_required
def myCloset(request):
    top = Cloth.objects.filter(month=11, category_id=1)
    # print("-------------")
    # print(len(top))
    context={
        'tops':top
    }
    return render(request, 'codi/myCloset.html',context)

@login_required
def addCloth(request):
    top = Cloth.objects.filter(month=11, category_id=1)
    # print("-------------")
    # print(len(top))
    context={
        'tops':top
    }
    return render(request, 'codi/addCloth1.html', context)

@login_required
def mypage(request):
    return render(request, 'codi/mypage.html')


def mapToGrid(lat, lon, code = 0 ):
    Re = 6371.00877     ##  지도반경
    grid = 5.0          ##  격자간격 (km)
    slat1 = 30.0        ##  표준위도 1
    slat2 = 60.0        ##  표준위도 2
    olon = 126.0        ##  기준점 경도
    olat = 38.0         ##  기준점 위도
    xo = 210 / grid     ##  기준점 X좌표
    yo = 675 / grid     ##  기준점 Y좌표
    first = 0
    if first == 0 :
        PI = math.asin(1.0) * 2.0
        DEGRAD = PI/ 180.0
        re = Re / grid
        slat1 = slat1 * DEGRAD
        slat2 = slat2 * DEGRAD
        olon = olon * DEGRAD
        olat = olat * DEGRAD
        sn = math.tan(PI * 0.25 + slat2 * 0.5) / math.tan(PI * 0.25 + slat1 * 0.5)
        sn = math.log(math.cos(slat1) / math.cos(slat2)) / math.log(sn)
        sf = math.tan(PI * 0.25 + slat1 * 0.5)
        sf = math.pow(sf, sn) * math.cos(slat1) / sn
        ro = math.tan(PI * 0.25 + olat * 0.5)
        ro = re * sf / math.pow(ro, sn)
        first = 1
    ra = math.tan(PI * 0.25 + lat * DEGRAD * 0.5)
    ra = re * sf / pow(ra, sn)
    theta = lon * DEGRAD - olon
    if theta > PI :
        theta -= 2.0 * PI
    if theta < -PI :
        theta += 2.0 * PI
    theta *= sn
    x = (ra * math.sin(theta)) + xo
    y = (ro - ra * math.cos(theta)) + yo
    x = int(x + 1.5)
    y = int(y + 1.5)
    return x, y
def getWeather(request):
    lng = request.POST["lng"]
    lat= request.POST["lat"]
    x = (mapToGrid(float(lat),float(lng))[0])
    y = (mapToGrid(float(lat),float(lng))[1])
    min_tmp = get_tmn_data(x,y)
    max_tmp = get_tmx_data(x,y)
    now_tmp = ForecastTimeData(x,y)
    context = {
        'min': min_tmp,
        'max': max_tmp,
        'now': now_tmp
    }
    return HttpResponse(json.dumps(context), content_type="application/json")
