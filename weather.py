# -*- coding: UTF-8 -*-
import urllib2,json

weather_url = 'http://apis.baidu.com/thinkpage/weather_api/suggestion?location=shanghai&language=zh-Hans&unit=c&start=0&days=3'
api_key = '4778a1e93a640fe4bbe2f6d660455cf5'

def get_weather():
    request = urllib2.Request(weather_url)

    """API from baidu API Store
    """
    request.add_header('apikey', api_key)

    response = urllib2.urlopen(request)
    content = response.read()

    if content:
        try:
            result = json.loads(str(content))
        except:
            return None
        return result
    return None

def weather():
    weather = get_weather()
    if weather == None:
        return None
    info = weather['results'][0]['daily'][0]
    return {
        'date': info['date'],
        'weather': info['text_day'],
        'temperature': info['low'] + '~' + info['high'] + '摄氏度'.decode('utf-8')
    }
