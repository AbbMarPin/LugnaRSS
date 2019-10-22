import html
import feedparser
import datetime

d = feedparser.parse("https://www.fazerfoodco.se/modules/MenuRss/MenuRss/CurrentWeek?costNumber=6417&language=sv")

foodlist = []

for x in range(5):
    food = html.unescape(d.entries[x].description)
    food = food.replace("<p>","").replace("</p>","")
    food = food.replace("<br />","")
    foodlist.append(food.split("\n"))

for x in foodlist[datetime.datetime.today().weekday()]:
    print(x)