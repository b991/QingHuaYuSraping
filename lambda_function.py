import boto3
from bs4 import BeautifulSoup
import requests
import datetime

def lambda_handler(event: any, context, any):
    #create a dynamodb client
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table('QingHuaTable')

    html_text = requests.get('https://allcp.net/').text
    soup = BeautifulSoup(html_text, 'lxml')
    count_div = soup.find('span',class_='xs1')
    count_text = count_div.find('strong').text
    now = datetime.datetime.now()
    nowdate = now.date()
    nowtime = now.strftime("%H:%M")
    timezone = datetime.datetime.now().astimezone().tzinfo


    response = table.put_item(
        Item={
            'date': str(count_text),
            'time': str(nowdate),
            'timezone':str(timezone),
            'count' : str(count_text)
        }
    )
    return(response)

