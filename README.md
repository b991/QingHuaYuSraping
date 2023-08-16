# 青花鱼 Web Scraping 
### Introduction
This code scrapes **the number of users** who are currently online from [青花鱼论坛](https://allcp.net/) using python bs4 and requests library. Then, we upload this code to AWS Lambda to run it serverlessly at the interval of 1 hour. We store the data from AWS lambda to AWS DynamoDB. 


In this documentation, we will build this code from scratch. By the end of the documentation, you will learn how to web scrape using python bs4 and requests. You will also learn how to upload your web scraping code to AWS Lambda, how to run the code at the interval of your preference, and how to store the web scraping data in AWS DynamoDB. 

### Steps
1. Using [this](https://dev.to/aissalaribi/how-to-use-beautiful-soup-in-aws-lambda-for-web-scrapping-1gh8) document, create a python virtual environment using pipenv. I used python version 3.11. The reason that we created virtual enviornment is to make packaging python dependencies easier when we upload them to AWS Lambda in the future. In order to learn python virtual environment and pipenv, please watch [this](https://youtu.be/zDYL22QNiWk?list=PL_GcZFQb3yYjwt-rg7mHob-9ujdsN6B6R) video. 
2. Watch [this](https://youtu.be/XVv6mJpFOb0?list=PL_GcZFQb3yYjwt-rg7mHob-9ujdsN6B6R) video to learn about web scraping. Create a lambda_function.py and start to scrape. Here are a few notes:
   * It's important to name the function lambda_function.py and the function in it lambda_handler. You will know why in the next step.
   * Instead of using lxml module as the video suggested, I used the code below. This is because AWS Lambda throws errors if I use lxml. html.parser is python's innate module. You don't need to install it.
    ```
    BeautifulSoup(html_text, 'html.parser')
    ```
   * I also used pipenv to install only requests and bs4 modules. datetime and time modules are already included in python. Boto3 is also provided by AWS lambda function. So we don't need to install them using pipenv. 

4. Watch [this](https://youtu.be/ijyeE-pXFk0?list=PL_GcZFQb3yYjwt-rg7mHob-9ujdsN6B6R) video to create your AWS account, IAM, lambda function and DynamoDB.

5. Follow [this](https://dev.to/aissalaribi/how-to-use-beautiful-soup-in-aws-lambda-for-web-scrapping-1gh8) document, zip your pacakges and upload them to AWS Lambda. 

6. Finally, follow [this](https://youtu.be/-8L4OxotXlE?list=PLD_RqipW0-9s-u1HXTglYV8Aam-5P3XLi) video to set up the time inverval to run your lambda function serverlessly. 

### Congratulations! You've just created a web scraping tool and it's running on the cloud!
