# 초단기예보에서 강수형태(PTY), 1시간강수량(RN1), 하늘상태(SKY), 기온(T1H), 습도(REH) 
# PTY - RN1 - SKY - T1H - REH
# 1시간마다 업데이트, 10분에 발표
# SKY 맑음(1) / 구름많음(3) / 흐림(4)
# PTY 없음(0) / 비(1) / 진눈깨비(2) / 눈(3) / 소나기(4)

# 변수명_ / 함수이름대문자

import json
from datetime import datetime
from urllib.request import urlopen

def get_forecast_data(data):
    now = datetime.now()
    now_date = now.strftime('%Y%m%d')
    base_date = now_date
    # print(base_date)
    now_hour = int(now.strftime('%H'))
    base_time = now_hour
    # print(base_time)
    now_min = int(now.strftime('%M'))
    if now_min <= 20:
        temp_time = now_hour - 1
    else:
        temp_time = now_hour
    # print(temp_time)
    base_time = str(temp_time) + '30'
    # print(base_time) 
    fcstTime = int(str(temp_time+1) + '00')
    # print(fcstTime)
    service_key = 'lgkNpxB8TTbXXj4%2BEK9KumE72Q78STsTzIR9MEgjrEARC7OGjiX4cS8UTFTxT55PqDvk1ARfSgMATErdYQKb9A%3D%3D'
    # x,y 좌표 받아오기
    nx = str(61)
    ny = str(125)
    _type = 'json'
    try:
        num = int(len(data))
        target_data = []
        for i in range(num):
            if data[i]['fcstTime'] == fcstTime:
                target_data.append(data[i])
        # print(target_data)
        data_num = int(len(target_data))
        forecast_data = []
        for i in range(data_num):
            # PTY - RN1 - SKY - T1H - REH
            # if target_data[i]['category'] == 'PTY':
            #     # print(target_data[i]['fcstValue'])
            #     forecast_data.append(target_data[i]['fcstValue'])
            # elif target_data[i]['category'] == 'RN1':
            #     forecast_data.append(target_data[i]['fcstValue'])
            # elif target_data[i]['category'] == 'SKY':
            #     forecast_data.append(target_data[i]['fcstValue'])
            # elif target_data[i]['category'] == 'T1H':
            #     forecast_data.append(target_data[i]['fcstValue'])
            # elif target_data[i]['category'] == 'REH':
            #     forecast_data.append(target_data[i]['fcstValue'])
            if target_data[i]['category'] == 'T1H':
                forecast_data.append(target_data[i]['fcstValue'])
        return forecast_data
    except KeyError: print('API 호출 실패!')
def ForecastTimeData():
    now = datetime.now()
    now_date = now.strftime('%Y%m%d')
    base_date = now_date
    # print(base_date)
    now_hour = int(now.strftime('%H'))
    base_time = now_hour
    # print(base_time)
    now_min = int(now.strftime('%M'))
    if now_min <= 20:
        temp_time = now_hour - 1
    else:
        temp_time = now_hour
    # print(temp_time)
    base_time = str(temp_time) + '30'
    # print(base_time) 
    fcstTime = int(str(temp_time+1) + '00')
    # print(fcstTime)
    service_key = 'lgkNpxB8TTbXXj4%2BEK9KumE72Q78STsTzIR9MEgjrEARC7OGjiX4cS8UTFTxT55PqDvk1ARfSgMATErdYQKb9A%3D%3D'
    # x,y 좌표 받아오기
    nx = str(61)
    ny = str(125)
    _type = 'json'
    api_url = f'http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData?serviceKey={service_key}&base_date={base_date}&base_time={base_time}&nx={nx}&ny={ny}&numOfRows=40&_type={_type}'
    data = urlopen(api_url).read()
    json_data = json.loads(data)
    # print(json_data)
    weather_info = json_data['response']['body']['items']['item']
    # print(weather_info)
    t1h = get_forecast_data(weather_info) # 낮 최고기온
    return t1h
ForecastData = ForecastTimeData()
# print(ForecastData)
