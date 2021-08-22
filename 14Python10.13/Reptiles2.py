from gevent import monkey

monkey.patch_all()

import requests, time, gevent
from bs4 import BeautifulSoup
from gevent.queue import Queue

res = requests.get('http://www.mtime.com/top/movie/top100/')
html = res.text
bs = BeautifulSoup(html, 'html.parser')
page = bs.find(id='PageNavigator').find_all('a')
url_list = []
url_list.append('http://www.mtime.com/top/movie/top100/')
for p in page:
    try:
        url_list.append(p['href'])
    except KeyError:
        pass
# print(url_list)


# 非多协程的时间
start = time.time()


def crawler(url):
    res = requests.get(url)
    # print(res.status_code)
    html = res.text
    bs = BeautifulSoup(html, 'html.parser')
    movies = bs.find(class_="colm").find(class_='top_list').find('ul').find_all('li')
    for movie in movies:
        name = movie.find(class_='px14 pb6').find('a').text
        print(name)


for url in url_list:
    crawler(url)
end = time.time()
interval = end - start

# 多协程的时间
start2 = time.time()
work = Queue()
for url in url_list:
    work.put_nowait(url)
    # 把url放进队列


def crawler(url):
    while not work.empty():
        url = work.get_nowait()
        res = requests.get(url)
        # print(res.status_code)
        html = res.text
        bs = BeautifulSoup(html, 'html.parser')
        movies = bs.find(class_="colm").find(class_='top_list').find('ul').find_all('li')
        for movie in movies:
            name = movie.find(class_='px14 pb6').find('a').text
            print(name)


task_list = []
for x in range(5):
    # 同时建立了5个爬虫，越多越快
    task = gevent.spawn(crawler, url)
    task_list.append(task)
gevent.joinall(task_list)
end2 = time.time()
interval2 = end2 - start2
print("\n" + '同步爬虫时间为：' + str(interval))
print('5个异步爬虫时间为：' + str(interval2))
