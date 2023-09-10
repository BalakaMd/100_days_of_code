import requests
from bs4 import BeautifulSoup

# date = input("Which year did you want to travel to? Type tha date in this format YYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/2012-09-22/"

response = requests.get(URL)
html_web = response.text

soup = BeautifulSoup(html_web, 'html.parser')
soup_names_spans = soup.select('li ul li h3')
song_titles = [song.text.strip() for song in soup_names_spans]
