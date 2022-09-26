import time
import requests
import pandas as pd
from bs4 import BeautifulSoup

# urls_https_main = "https://www.themoviedb.org/movie"
movie_url_list = []
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

for x in range(1, 16):

    time.sleep(4)
    rq = requests.get(f"https://www.themoviedb.org/movie?page={x}",
                      headers=headers)
    soup = BeautifulSoup(rq.content, 'lxml')

    all_cards = soup.find_all('div', class_='card style_1')

    for items in all_cards:
        for link in items.find_all('div', class_='content'):
            for links in link.find_all('a', href=True):
                movie_url = "https://www.themoviedb.org" + links['href']

                movie_url_list.append(movie_url)

# OKay No Need To change anything
all_data_list = []
for movie_data in movie_url_list:
    time.sleep(1)  # To Avoid ConnectionResetError
    page_in_url = requests.get(movie_data, headers=headers)
    time.sleep(0)  # To Avoid ConnectionResetError
    soup_movie = BeautifulSoup(page_in_url.content, 'lxml')
    soup_movie1 = soup_movie.find('section', class_='header')
    # time.sleep(2)  # To Avoid ConnectionResetError
    that_div = soup_movie1.find_all('div', class_='title')
    for that_3things in that_div:
        # Name
        h2_ = that_3things.find('h2')
        name = h2_.find('a').text.strip()

        #Ratings
        rating = soup_movie.find('div',
                                 {'class': "user_score_chart"})['data-percent']

        # Release Date
        release = that_3things.find('span', class_='release').text.strip()

        # Runtime
        try:
            runtime = that_3things.find('span', class_='runtime').text.strip()
        except AttributeError:
            runtime = "No Runtime"
            pass

        # Genres
        try:
            genres = that_3things.find('span', class_='genres').text.strip()
        except AttributeError:
            genres = "Genres Not Available"
            pass

        # Director
        try:
            go_p = soup_movie.find('li', class_='profile')
            director = go_p.find('p').text.strip()
        except AttributeError:
            director = "Director Not Available"
            pass

        # URL
        go_url = h2_.find('a', href=True)
        url = "https://www.themoviedb.org" + str(go_url['href'])

        all_data_dict = {
            'Name': name,
            'Rating': rating,
            'Genres': genres,
            'Release Date': release,
            'Runtime': runtime,
            'Director': director,
            'URL': url
        }
    all_data_list.append(all_data_dict)

    df = pd.DataFrame(all_data_list)
df.index = df.index + 1
# df.to_excel( "D:\Programming\Python Coding\Movie Scrape\Data\Movies300Data.xlsx", index_label='Sr No.') #It was path in my file explorer for Movies300Data.xlsx
df.to_excel("Movies300Data.xlsx", index_label='Sr No.')
