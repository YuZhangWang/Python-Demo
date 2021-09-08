from django.http import HttpResponse
from django.shortcuts import render
from register import models
import requests
from lxml import etree
from camera.views import camera, camera2

books = []

# 获取每页地址
def getUrl():
    for i in range(10):
        url = 'https://book.douban.com/top250?start={}'.format(i*25)
        urlData(url)


# 获取每页数据
def urlData(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
    }
    html = requests.get(url, headers=headers).text
    res = etree.HTML(html)
    trs = res.xpath('//*[@id="content"]/div/div[1]/div/table/tr')
    for tr in trs:
        name = tr.xpath('./td[2]/div/a/text()')[0].strip()
        score = tr.xpath('./td[2]/div/span[2]/text()')[0].strip()
        comment = tr.xpath('./td[2]/div/span[3]/text()')[0].replace('(', '').replace(')', '').strip()
        info = tr.xpath('./td[2]/p[1]/text()')[0].strip()
        books.append("《{}》--{}分--{}--{}".format(name, score, comment, info))


def facelogin(request):
    if request.method == 'POST':
        name = camera2()
        if name == False:
            return HttpResponse("人脸认证失败")
        else:
            getUrl()
            context = {
                'name': name,
                'books': books,
            }
            return render(request, 'login.html', context=context)
    else:
        return render(request, 'camera.html')


def tologin(request):
    if request.method == "POST":
        username = request.POST.get('usernameOrEmail', None)
        password = request.POST.get('password', None)
        # faceValue = camera(username)
        if username and password:  # 确保用户名和密码都不为空
            try:
                user = models.userdata.objects.get(username=username)
            except:
                user = models.userdata.objects.get(email=username)
            if user.password == password:
                getUrl()
                context = {
                    'name': username,
                    'books': books,
                }
                return render(request, 'login.html', context=context)
            else:
                return render(request, 'failed.html')
        else:
            return render(request, 'logout.html')
    else:
        return render(request, 'logout.html')


def login(request):
    return render(request, 'login.html')