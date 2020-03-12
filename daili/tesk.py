import requests
from selenium import webdriver
headers = {
    'Server': 'Tengine',
    'Content-Type': 'text/plain; charset=utf-8',
    'Content-Length': '9006',
    'Connection': 'keep-alive',
    'X-Powered-By': 'PHP/7.1.2',
}
res = requests.get('http://m.gateway.7723api.com/v3/bbs/npl/list_rows/20/params_version_code/397/page/1/tid/823422/ordertype/0', headers =headers)
html = res.content
print(html)
# options = webdriver.ChromeOptions()
# options.add_argument('--disable-gpu')
# # options.add_argument('window-size=1200x600')
# # 设置中文
# options.add_argument('lang=zh_CN.UTF-8')
# # 更换头部
# options.add_argument(headers)
# browser = webdriver.Chrome(options=options)
# browser.get('http://m.gateway.7723api.com/v3/bbs/npl/list_rows/20/params_version_code/397/page/1/tid/823422/ordertype/0')