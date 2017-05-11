import bs4 as bs
import requests
import time

resp = requests.get('https://socialblade.com/youtube/top/5000/mostsubscribed')
soup = bs.BeautifulSoup(resp.text, 'lxml')

for other_thing in soup.find_all('div', {'class': 'TableHeader'}):
    print(other_thing.text)

for index, info in enumerate(soup.find_all('div', {"class": "TableMonthlyStats"})):
    new_index = 0
    if (index % 5 == 2):
        print(info)
        for title in info.find_all('a'):
            print(new_index)
            print('Channel:', title.text)
            print('Youtube URL: ', title.get('href'))
        new_index += 1
    time.sleep(1)
# for url in soup.find_all('a'):
#     print(url.get('href'))
