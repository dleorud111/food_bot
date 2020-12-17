# 웹 크롤링
# requests(html 파일 가져옴), bs4(추출한 html 분석)

import requests
from bs4 import BeautifulSoup
import datetime # 오늘 날짜 구하기

now = str(datetime.datetime.now())
date = now[:4] + now[5:7] + now[8:10]
#print(date)

req = requests.get("http://school.cbe.go.kr/chungjuja-e/M01040504/list?ymd=" + date)

soup = BeautifulSoup(req.text, "html.parser")

atag = soup.find("a", href="/chungjuja-e/M01040504/list?ymd=" + date)


li = atag.find_all('li')

food = ""
for i in li:
    food = food + i.text + "\n"
#print(food)

# 3.텔레그램 봇 만들기
import telegram

token = "1424522521:AAGone3SxqhnL67kzjA4AwsMDB9eGrKtKEc"
bot = telegram.Bot(token=token)
# for i in bot.getUpdates():
#     print(i.message)
bot.send_message(1477195321, food)