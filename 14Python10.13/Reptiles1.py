# 抓取Top排名100名的电影名称，简介以及其他信息
import requests, jason
import lxml.etree


# header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}

# 获取页面的html并返回
def get_html_tree(url):
    resp = requests.get(url).text
    resp_tree = lxml.etree.HTML(resp)
    return resp_tree


# 获取初始页的电影链接
def get_movie_link(resp_tree):
    names = resp_tree.xpath('//div[@class="mov_con"]//h2/a/text()')
    links = resp_tree.xpath('//div[@class="mov_con"]//h2/a/@href')
    director = resp_tree.xpath('//div[@class="mov_con"]//p[1]/a/text()')
    performer1 = resp_tree.xpath('//div[@class="mov_con"]//p[2]/a[1]/text()')
    performer2 = resp_tree.xpath('//div[@class="mov_con"]//p[2]/a[2]/text()')
    type1 = resp_tree.xpath('//div[@class="mov_con"]//p[3]/span/a[1]/text()')
    type2 = resp_tree.xpath('//div[@class="mov_con"]//p[3]/span/a[2]/text()')
    introduce = resp_tree.xpath('//div[@class="mov_con"]//p[@class="mt3"]/text()')
    score1 = resp_tree.xpath('//div[@class="mov_point"]//b/span[1]/text()')
    score2 = resp_tree.xpath('//div[@class="mov_point"]//b/span[2]/text()')
    return links, names, director, performer1, performer2, introduce, type1, type2, score1, score2


# global headers
url = 'http://www.mtime.com/top/movie/top100/'
resp_tree = get_html_tree(url)
links, names, director, performer1, performer2, introduce, type1, type2, score1, score2 = get_movie_link(resp_tree)

for i in range(len(names)):
    print(names[i])
    print(links[i])
    print("导演:" + director[i])
    print("主演:" + performer1[i] + " " + performer2[i])
    print("类型:" + type1[i] + "/" + type2[i])
    print("简介:" + introduce[i])
    print("评分:" + score1[i] + score2[i])
