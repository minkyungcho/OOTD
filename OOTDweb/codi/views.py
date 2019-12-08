from django.shortcuts import render , HttpResponse
from datetime import datetime
from urllib.request import urlopen
from .weather1 import get_tmn_data , get_tmx_data
from .weather2 import get_forecast_data , ForecastTimeData
from .models import Cloth
import json
import math
# Create your views here.

def index(request):
    return render(request, 'index.html')

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

def codiWorldcup(request):
    return render(request, 'codi/codiWorldcup.html')

def myCloset(request):
    top = Cloth.objects.filter(month=11, category_id=1)
    # print("-------------")
    # print(len(top))
    context={
        'tops':top
    }
    return render(request, 'codi/myCloset.html',context)

    
def getWeather(request):
    lng = request.POST["lng"]
    lat= request.POST["lat"]
    x = (mapToGrid(float(lat),float(lng))[0])
    y = (mapToGrid(float(lat),float(lng))[1])
    # print("------------------")
    # print(x)
    # print(y)
    min = get_tmn_data(x,y)
    max = get_tmx_data(x,y)
    now = ForecastTimeData()
    # 세 값들을 이쁘게만들어서 html한테 뿌려주자.
    context = {
        'min':min,
        'max':max,
        'now':now
    }
    return HttpResponse(json.dumps(context), content_type="application/json")