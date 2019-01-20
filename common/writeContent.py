# 常用python文件
# 方法1 写文件

import time
import json
import requests

__all__ = ['create_file_func','get_html_data','create_html']

text_name = time.strftime('%Y%m%d', time.localtime(time.time()))

def create_file_func(content):
    
    with open('./{}.txt'.format(text_name), 'a', encoding='utf8') as file_content:
        file_content.write(content)

def create_html (content,mask_id) :
        # text_name = time.strftime('%Y%m%d', time.localtime(time.time()))
        with open('./html/{0}-{1}.html'.format(text_name,mask_id), 'w', encoding='utf8') as fs:
                # print(type(content))
                fs.write(content) 

def get_html_data(url = 'https://www.meipian.cn/hot'):
        # url = 'https://www.meipian.cn/hot'
        response = requests.get(url)
        if int(response.status_code) == 200 :
                return response.content
        else:
                return ''

