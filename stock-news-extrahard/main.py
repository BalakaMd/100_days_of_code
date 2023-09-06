import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = 'VWVUO327SN9688OU'
NEWS_API = '6cddd236319f4050bf7d6a99790c7c71'

alphavantage_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={STOCK}&apikey={API_KEY}'"

response = requests.get(url=alphavantage_url)
response.raise_for_status()
data = response.json()['Weekly Time Series']
days_of_bargaining = list(data)[:2]
today_bargaining = float(data[days_of_bargaining[0]]['4. close'])
yesterday_bargaining = float(data[days_of_bargaining[1]]['4. close'])
percentage_difference = round(((today_bargaining - yesterday_bargaining) / yesterday_bargaining) * 100, 2)

if percentage_difference > 5 or percentage_difference < -5:
    news_url = ('https://newsapi.org/v2/everything?'
                f'q={COMPANY_NAME}&'
                'sortBy=DatePublished&'
                f'apiKey={NEWS_API}')
    response = requests.get(news_url)
    response.raise_for_status()
    news_data = response.json()['articles'][:3]
    for news in news_data:
        articles = news['title']
        description = news['description']
        url = news['url']
        print(f"""
                TSLA: {percentage_difference}%
                Headline: {articles}. 
                Brief: {description}
                URL: {url}
                """)
