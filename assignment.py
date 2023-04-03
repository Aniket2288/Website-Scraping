# import requests
# from bs4 import BeautifulSoup
# from csv import writer

# URL = "https://www.theverge.com"
# r = requests.get(URL)
# soup = BeautifulSoup(r.content, 'html5lib')

# lists = soup.find_all('div' , class_='max-w-content-block-standard')

# with open('30-03-2023_verge.csv' , 'w' , encoding='utf8' , newline='') as f:
#     thewriter = writer(f)
#     header = ['ID','URL', 'Headlines' , 'Authors' , 'Date']
#     thewriter.writerow(header)

#     for list in lists:
#         id = list.find('div' , class_='z-10').text
#         url = URL + list.find('a', class_='group-hover:shadow-underline-franklin')['href']
#         headline = list.find('a', class_='group-hover:shadow-underline-franklin').text
#         author = list.find('div' , class_='inline-block').text
#         date = list.find('span' , class_='text-gray-63').text
#         info = [id, url, headline, author , date]
#         thewriter.writerow(info)
#    print(info)


# Pip install mysql-connector


import requests
from bs4 import BeautifulSoup
import sqlite3

URL = "https://www.theverge.com"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')

lists = soup.find_all('div', class_='max-w-content-block-standard')

conn = sqlite3.connect('30-03-2023_verge.db')
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS news")

create_table_query = '''CREATE TABLE news (
                        id TEXT PRIMARY KEY,
                        url TEXT,
                        headline TEXT,
                        author TEXT,
                        date TEXT
                        );'''
cur.execute(create_table_query)

for list in lists:
    id = list.find('div', class_='z-10').text.strip()
    url = URL + list.find('a', class_='group-hover:shadow-underline-franklin')['href']
    headline = list.find('a', class_='group-hover:shadow-underline-franklin').text.strip()
    author = list.find('div', class_='inline-block').text.strip()
    date = list.find('span', class_='text-gray-63').text.strip()

    insert_query = f"INSERT INTO news VALUES ('{id}', '{url}', '{headline}', '{author}', '{date}')"
    cur.execute(insert_query)

conn.commit()
cur.close()
conn.close()


##############  Thank You!!! #################