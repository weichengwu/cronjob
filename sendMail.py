# -*- coding: UTF-8 -*-
import requests
def send_message(html):
    return requests.post(
        "https://api.mailgun.net/v3/noreply.stephenw.cc/messages",
        auth=("api", "key-75f9cf9639283b1080e762c9d9bd87db"),
        data={"from": "PI机器人 <noreply@stephenw.cc>",
              "to": ["zhilong.wang@ele.me", "wuvcen@gmail.com"],
              "subject": "PI日报",
              "text": "sorry, some error happened",
              "html": html})
