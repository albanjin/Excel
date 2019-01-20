

from common import writeContent
from bs4 import BeautifulSoup

#要抓取的目标页码地址


#查看响应状态码
# status_code = response.status_code

#使用BeautifulSoup解析代码,并锁定页码指定标签内容
response = writeContent.get_html_data()
html = BeautifulSoup(response,'html.parser')
# find_all(['a','.item.server-item'])
target_arr  =  html.select('#list .item.server-item>a')
target_hot = html.select('.hot > .item > a')
# print(target_hot)
target_arr.extend(target_hot)
# for val in target_arr :
#     print(val.attrs['href'])

for val in target_arr :
    print(val.attrs['href'])
    writeContent.create_file_func(val.attrs['href'] + '\n') 
    resp = writeContent.get_html_data(val.attrs['href'])
    writeContent.create_html(resp.decode('utf-8'),val.attrs['href'].replace('https://www.meipian.cn/',''))

# writeContent.create_file_func(response.content.decode('utf-8'))
