from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/')
yc_web = response.text
soup = BeautifulSoup(yc_web, "html.parser")
articles_tags = soup.findAll(name='span', class_='titleline')
article_upvotes_tag = soup.findAll(name='span', class_='score')

article_text = [article.find(name='a').get_text() for article in articles_tags]
article_link = [article.find(name='a').get('href') for article in articles_tags]
article_upvotes = [int(vote.get_text().split()[0]) for vote in article_upvotes_tag]
max_vote = max(article_upvotes)
max_index = article_upvotes.index(max_vote)
final_text = article_text[max_index], \
    article_link[max_index], \
    article_upvotes[max_index]
print(final_text)
