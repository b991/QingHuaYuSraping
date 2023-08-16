from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import datetime 
import time 
import boto3

def lambda_handler(event, context):
    options = Options()
    options.binary_location = '/opt/headless-chromium'
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--single-process')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome('/opt/chromedriver',chrome_options=options)
    driver.get('http://www.mtslash.me/forum.php')
    time.sleep(3)
    
    #create a dynamodb client
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table('SuiYuanJuTable')

    #extract info that I need
    element = driver.find_element(By.CLASS_NAME,"xs1")
    count = element.find_element(By.TAG_NAME,"strong")
    returnCount = str(count.text)
    now = datetime.datetime.now()
    nowdate = now.date()
    nowtime = now.strftime("%H:%M")
    timezone = datetime.datetime.now().astimezone().tzinfo

    driver.close()
    driver.quit()

    response = table.put_item(
        Item={
            'date': str(nowdate),
            'time': str(nowtime),
            'timezone':str(timezone),
            'count' : returnCount
        }
    )

    return response