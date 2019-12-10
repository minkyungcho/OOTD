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
from .models import Article, Board
from django.http.response import HttpResponse

def home(request):
    return render(request, 'index.html')

def mapToGrid(lat, lon, code = 0 ):
    NX = 149            ## X축 격자점 수
    NY = 253            ## Y축 격자점 수
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
        RADDEG = 180.0 / PI
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
            return redirect('codi:codiBook')
        else:
            return redirect('codi:codiBook')
    else:
        articles = Article.objects.all().order_by("created_at").reverse()
        context = {
            'articles': articles
        }
        return render(request, 'codi/codiBook.html', context)

@login_required
def mypage(request):
    return render(request, 'codi/mypage.html')


@login_required
def myCloset(request):
    id = request.user.id
    # top = Cloth.objects.filter(month=11, category_id=1)
    tops = Cloth.objects.filter(Q(category_id=1) & Q(user_clothes__id=id)).values('img_url', 'cloth_type').distinct()
    outers = Cloth.objects.filter(Q(category_id=2) & Q(user_clothes__id=id)).values('img_url', 'cloth_type').distinct()
    bottoms = Cloth.objects.filter(Q(category_id=4) & Q(user_clothes__id=id)).values('img_url', 'cloth_type').distinct()
    skirts = Cloth.objects.filter(Q(category_id=3) & Q(user_clothes__id=id)).values('img_url', 'cloth_type').distinct()
    onepieces = Cloth.objects.filter(Q(category_id=5) & Q(user_clothes__id=id)).values('img_url', 'cloth_type').distinct()
    # print("-------------")
    # print(len(top))
    context={
        'tops':tops,
        'outers':outers,
        'bottoms':bottoms,
        'skirts':skirts,
        'onepieces':onepieces
    }
    return render(request, 'codi/myCloset.html',context)

@login_required
def addCloth(request):
    # top = Cloth.objects.filter(month=11, category_id=1)
    # print("-------------")
    # print(len(top))
    context={
        # 'tops':top
    }
    return render(request, 'codi/addCloth1.html', context)

@login_required    
def getClothList(request):
    category_id = request.POST["category_id"]
    # print(type(category_id))
    if int(category_id) == 99:
        print(category_id)
        # print(category_id)
        id = request.user.id
        # top = Cloth.objects.all()
        topN = Cloth.objects.filter(~Q(user_clothes__id=id)).values('img_url', 'cloth_type').distinct()
    else:
        # print(category_id)
        id = request.user.id # user 저장된 고유 id 번호
        # print(type(id))
        top = Cloth.objects.filter(~Q(user_clothes__id=id))
        topN = Cloth.objects.filter(Q(category_id=category_id) & ~Q(user_clothes__id=id)).values('img_url', 'cloth_type').distinct()
        
        
        # cnt = 0
        # for n in topN:
        #     # print(n) # {'img_url' : '~~~'} 형식의 dict
        #     for t in top:
        #         if t.img_url == n['img_url']:
        #             cnt += 1
        # print(cnt)
        # print(len(top))
        # print(len(topN))
        # print(type(topN))
        for tmp in top:
            # print(tmp.user_clothes.all().id)
            if len(tmp.user_clothes.all()) >= 1:
            #     # print(len(tmp.user_clothes.all()))
            #     for t in tmp.user_clothes.all():
            #         # print(type(tmp))
            #         print(t.id+" "+request.user.id)
            # for t in tmp.user_clothes.all():
                # t 는 User
                # if t.id == id:
                    # t.id는 옷 가진 user의 id
                    # id는 로그인한 user의 고유 id 번호
                noUserTop = Cloth.objects.filter(Q(category_id=category_id) & Q(id=tmp.id))
                # print(type(noUserTop))
                # print(len(noUserTop)) # 쿼리셋
                # print(tmp.id) # cloth id
                    # noUserTop = Cloth.objects.filter(category_id=category_id, )
                    # print(len(t.id))
                # else:
                    # print("1")
        #이거 유저 아이디를 찾으다음에 없으면 어디에 붙여서 쿼리셋 만들고 .values 로 찾아와서 distinct 하자 
        #top = Cloth.objects.filter(category_id=category_id).values('product_id','img_url','cloth_type', 'label').distinct()
        # print(len(top))

    context = {
        "tops": topN
    }
    return render(request, 'codi/cloth_card.html', context)

@login_required
def add(request):
    # product_id = request.POST["product_id"]
    # label = request.POST["label"]
    # pid = Cloth.objects.filter(product_id=product_id, label=label)
    img_url = request.POST["img_url"] # 선택한 옷의 url
    print(img_url)
    pid = Cloth.objects.filter(img_url=img_url) # 선택한 옷 url이랑 이미지 같은 옷들 다 가져오기.
    # pids = []
    # for p in pid:
    #     # print(p.id)
    #     print(len(p.user_clothes.all()))
    #     pids.append(p)
    
    # print(len(pids))

    # 사용자의 옷장 DB에 옷을 추가한다!
    if request.user in pid[0].user_clothes.all():
        for tmp in pid:
            tmp.user_clothes.remove(request.user)
    else:
        for tmp in pid:
            # print(type(tmp))
            tmp.user_clothes.add(request.user)
#           print(pid.user_clothes.all())
    context = {

    }
    return HttpResponse(json.dumps(context), status=200, content_type='application/json')


def getWeather(request):
    lng = request.POST["lng"]
    lat= request.POST["lat"]
    x = (mapToGrid(float(lat),float(lng))[0])
    y = (mapToGrid(float(lat),float(lng))[1])
    min = get_tmn_data(x,y)
    max = get_tmx_data(x,y)
    now = ForecastTimeData()
    context = {
        'min':min,
        'max':max,
        'now':now
    }
    return HttpResponse(json.dumps(context), content_type="application/json")
