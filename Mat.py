import html
import feedparser

d = feedparser.parse("https://www.fazerfoodco.se/modules/MenuRss/MenuRss/CurrentWeek?costNumber=6417&language=sv")


food = html.unescape(d.entries[0].description)
food = food.replace("<p>","").replace("</p>","")

food = food.split("\n")

print(food)