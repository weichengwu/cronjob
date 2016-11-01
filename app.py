# -*- coding: UTF-8 -*-
from jinja2 import Template
from weather import weather
from sendMail import send_message
from NBA import nba
import os

def template():
    file_obj = open(os.path.join(os.path.abspath('.'), 'template.html'), 'r+')
    template_str = file_obj.read()
    temp = str(template_str).decode('utf-8')
    return Template(temp)

temp = template()
weather_info = weather()
nba_info = nba()

if not weather_info == None:
    weather_info['nba'] = nba_info
    html = temp.render(weather_info)
    print send_message(html)

