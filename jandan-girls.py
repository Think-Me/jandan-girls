import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)
dir = 'C:/spider-download/jandan-girls/'
img_urls = []
page_urls = ["http://jandan.net/ooxx/page-{}#comments".format(str(i)) for i in range(5, 6)]

def GetImgUrl(u):
    driver.get(u)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    images = soup.select('a.view_img_link')
    for i in images:
        t = i.get('href')
        if str('gif') in str(t):
            pass
        else:
            img_url = 'http:' + t
            img_urls.append(img_url)

def DownloadImg():
    n = 1
    for i in img_urls:
        print('第 ' + str(n) + ' 张 ... ', end='')
        with open(dir + i[-20:], 'wb') as f:
            f.write(requests.get(i).content)
        print('OK!')
        n = n + 1

for u in page_urls:
    GetImgUrl(u)
print('*** 开始下载 ***')
DownloadImg()
print('*** 下载完成 ***')