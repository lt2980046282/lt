from selenium import webdriver
url = 'https://www.zhipin.com/job_detail/?query=python&city=100010000&industry=&position='

browser = webdriver.Chrome()
res = browser.get(url)
cookies = browser.get_cookies()
js = browser.execute_script("""var req = new XMLHttpRequest();
req.open('GET', document.location, false);
req.send(null);
var headers = req.getAllResponseHeaders().toLowerCase();
console.log(headers)""")
print(js)