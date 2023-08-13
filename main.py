from bs4 import BeautifulSoup
import requests
import datetime

#def find_online_num():
html_text = requests.get('https://allcp.net/').text
soup = BeautifulSoup(html_text, 'lxml')
count_div = soup.find('span',class_='xs1')
count_text = count_div.find('strong').text
now = datetime.datetime.now()
timezone = datetime.datetime.now().astimezone().tzinfo
print(count_text)
print(now)
print(timezone)
