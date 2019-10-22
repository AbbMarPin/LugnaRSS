import html
import feedparser
import datetime
from gtts import gTTS
import os
import playsound
from time import sleep

d = feedparser.parse("https://www.fazerfoodco.se/modules/MenuRss/MenuRss/CurrentWeek?costNumber=6417&language=sv")

foodlist = []

for x in range(5):
    food = html.unescape(d.entries[x].description)
    food = food.replace("<p>","").replace("</p>","")
    food = food.replace("<br />","")
    foodlist.append(food.split("\n"))
try:
    for x in foodlist[datetime.datetime.today().weekday()]:
        print(x)
        tts = gTTS(text=x, lang='sv')
        tts.save("say.mp3")
        playsound.playsound('say.mp3', True)
        os.remove("say.mp3")
except:
    try:
        os.remove("say.mp3")
    except:
        print("exiting")