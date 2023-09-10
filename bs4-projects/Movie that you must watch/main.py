from bs4 import BeautifulSoup
import requests

response = requests.get(
    'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
best_films_web = response.text

soup = BeautifulSoup(best_films_web, 'html.parser')
best_films_tag = soup.findAll(name='h3', class_='title')
films_name = [film.get_text() for film in best_films_tag]
films_name.reverse()


with open('Top_100.txt', 'w') as file:
    for film in films_name:
        file.write(f'{film}\n')

