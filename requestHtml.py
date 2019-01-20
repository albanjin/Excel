from common import writeContent
from bs4 import BeautifulSoup

#使用BeautifulSoup解析代码,并锁定页码指定标签内容
response = writeContent.get_html_data()
html = BeautifulSoup(response,'html.parser')
target_arr  =  html.select('#list .item.server-item>a')
target_hot = html.select('.hot > .item > a')
target_arr.extend(target_hot)

for val in target_arr :
    print(val.attrs['href'])
    writeContent.create_file_func(val.attrs['href'] + '\n') 
    resp = writeContent.get_html_data(val.attrs['href'])
    writeContent.create_html(resp.decode('utf-8'),val.attrs['href'].replace('https://www.meipian.cn/',''))

