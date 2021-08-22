# coding=utf-8
import requests
import pdfkit  # PDF模块
import re
import os
from bs4 import BeautifulSoup  # html解析

# 定义头部
header = '''<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="referrer" content="origin">

    <meta http-equiv="Cache-Control" content="no-transform">
    <meta http-equiv="Cache-Control" content="no-siteapp">
    <title>小戳同学 - 博客园</title>

    <link rel="stylesheet" href="https://www.cnblogs.com/css/blog-common.min.css?v=sqi5FxOybx6gjGoG6Zfy1wD-0AwznLNLYOVx7Y9tIN0">
    <link id="MainCss" rel="stylesheet" href="https://www.cnblogs.com/skins/coffee/bundle-coffee.min.css?v=pdMIVgsH8kXt-vOWnlL0N20TlHt3UyP9HzGgocfsP4s">

    <link id="mobile-style" media="only screen and (max-width: 767px)" type="text/css" rel="stylesheet" href="https://www.cnblogs.com/skins/coffee/bundle-coffee-mobile.min.css?v=MGucLWekW6t3A88Ks-YfEzrx4X_hEIpMacbOAC9lJUs">

    <link type="application/rss+xml" rel="alternate" href="https://www.cnblogs.com/xiaokuangnvhai/rss">
    <link type="application/rsd+xml" rel="EditURI" href="https://www.cnblogs.com/xiaokuangnvhai/rsd.xml">
    <link type="application/wlwmanifest+xml" rel="wlwmanifest" href="https://www.cnblogs.com/xiaokuangnvhai/wlwmanifest.xml">
    <script async="" src="https://www.google-analytics.com/analytics.js"></script><script src="https://common.cnblogs.com/scripts/jquery-2.2.0.min.js"></script>
    <script src="https://www.cnblogs.com/js/blog-common.min.js?v=ruOFvx8_pDlyiWjHGHyOXclVmNo396_IKB8YFZjMllo"></script>
    <script>
        var currentBlogId = 516754;
        var currentBlogApp = 'xiaokuangnvhai';
        var cb_enable_mathjax = false;
        var isLogined = true;
    </script>  
</head>'''


# 获取博客一共多少页码
def page_num():
    page_url = "https://www.cnblogs.com/wkrbky/p/5898017.html"
    page_request = requests.request("get", page_url)
    page_list = re.findall('共(.*?)页', page_request.text)  # 正则提取页面上的总页码
    return int(page_list[0].strip())  # 返回总页码


# 文章链接获取
def page_url_list(pagenum):
    page_url_list = []
    for num in range(1, pagenum + 1):  # 遍历每个文章列表页面，获取每个文章列表的文章URL
        page_url = 'https://www.cnblogs.com/wkrbky/p/5898017.html' % num
        page_request = requests.request("GET", page_url)
        page_list = re.findall('<a class="postTitle2" href="(.*?)">', page_request.text)  # 正则获取文章列表页面的所有文章链接
        page_url_list.extend(page_list)  # 叠加文章链接list
    return page_url_list  # 返回总的文章链接list


# 文章HTML文件生成
def file_page(page_url_list):
    for url in page_url_list:
        new_html = requests.request("GET", url, )  # 遍历获取文章页面HTML

        try:
            soup = BeautifulSoup(new_html.text, "html.parser", from_encoding="utf-8")  # 声明文章对象
            link_node2 = soup.find("h1", class_='postTitle')  # 获取文章标题的HTML代码
            link_node = soup.find('div', class_='postBody')  # 获取文章主体的HTML代码

            # 打开文章文件
            file = open("./page_html/%s.html" % soup.find('a', class_='postTitle2').text, 'w+', encoding="utf-8")
            file.write(header)  # 写文章头部
            file.write("<h1 class='postTitle'>" + str(link_node2.contents[1]) + "</h1")  # 写文章标题
            file.write("<div class='postBody'>" + str(link_node.contents[1]) + "</div>")  # 写文章主体
            file.close()  # 写完毕后，文件关闭

        except Exception as e:
            print("问题链接:%s" % url)  # 如果有带密码等异常的文章，输出连接


# 生成PDF
def pdf_html(path):
    pagelist = os.listdir(path)  # 获取文件名称list
    for filename in pagelist:  # 遍历文件
        file = "./page_html/%s" % filename  # HTML文件路径拼接
        confg = pdfkit.configuration(wkhtmltopdf=r'D:\下载\IDM下载')  # 声明wkhtmltopdf地址
        pdfkit.from_file(file, './blog_pdf/%s.pdf' % filename, configuration=confg)  # HTML文件转换为PDF


# 调取函数
file_page(page_url_list(page_num()))
pdf_html("./page_html")