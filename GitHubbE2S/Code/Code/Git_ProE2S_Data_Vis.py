import requests
import pandas as pd
from bs4 import BeautifulSoup

base_url = 'https://github.com/topics/data-visualization?page='
url_list = []
for p_num in range(1, 8):
    url_list.append(base_url + str(p_num))

    first30name = []

for url in url_list:
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'lxml')

    all_divs = soup.find_all('div', class_='d-flex flex-justify-between my-3')
    for items in all_divs:
        all_h3 = items.find_all(
            'h3', class_='f3 color-fg-muted text-normal lh-condensed')
        # User names
        for owner in all_h3:
            owner_name = owner.find('a')
            name = owner_name.text.strip()

        # Repository names
        for repo in all_h3:
            repo_name = repo.find('a', class_='text-bold wb-break-word')
            repository = repo_name.text.strip()

        # Repository links
        for link in items.find_all('a',
                                   class_='text-bold wb-break-word',
                                   href=True):
            repo_links = "https://github.com/" + link['href']

        # Stars
        for star in items.find_all('span', class_='Counter js-social-count'):
            stars = star.text.strip()
            ownername_dict = {
                'User Name': name,
                'Repository Name': repository,
                'Stars': stars,
                'Repository URL': repo_links
            }
        first30name.append(ownername_dict)

    df = pd.DataFrame(first30name)
    df.index = df.index + 1

# Deleting 10 extra rows from Data Frame
update_df = df.drop(index=[201, 202, 203, 204, 205, 206, 207, 208, 209, 210])

reindex_df = update_df.reset_index(drop=True)
reindex_df.index = reindex_df.index + 1
reindex_df.to_excel(
    "D:\Programming\Python Coding\GitProE2S\All Data That U Want\Visualization_Data.xlsx",
    index_label='Sr No.')
