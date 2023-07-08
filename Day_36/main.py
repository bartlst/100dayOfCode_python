import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "tesla"
STOCK_API_KEY = "xyz"
NEWS_API_KEY = "123"
TWILIO_SID = "345"
TWILIO_AUTH_TOKEN = '456456'

STOCK_API_PROPERTIES = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

NEWS_API_PROPERTIES = {
    "q": COMPANY_NAME,
    "sortBy": "publishedAt",
    "apiKey": NEWS_API_KEY
}

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

response = requests.get(STOCK_ENDPOINT, params=STOCK_API_PROPERTIES)
data = response.json()['Time Series (Daily)']

daily_stock_price = [{"date":key, "prices":value} for (key, value) in data.items()]

y_closing_price = float(daily_stock_price[0]['prices']['4. close'])

dby_closing_price = float(daily_stock_price[1]['prices']['4. close'])

difference = abs(round(y_closing_price-dby_closing_price))


percentage = round((difference*100)/y_closing_price, 2)


if percentage > 0:
    print("Get News")
    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

    response = requests.get(NEWS_ENDPOINT, params=NEWS_API_PROPERTIES)
    data = response.json()
    all_articles = data['articles']

    top_articles = all_articles[:3]


        ## STEP 3: Use twilio.com/docs/sms/quickstart/python
        #to send a separate message with each article's title and description to your phone number.

    headline_list = [f"Headline: {value['title']}. \nBrief: {value['description']}" for value in top_articles]
    print(headline_list)

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in headline_list:
        message = client.messages.create(
            body=article,
            from_="+11222333444",
            to="+11222333444"
        )

"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

