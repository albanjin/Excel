# 读取Excel文件数据
import xlrd 
import json
# file_url = './music.xlsx'
# 读取Excel中数据生成json

def sheet1_content_transform_json(file_url):
    workbook = xlrd.open_workbook(file_url)
    sheet1_name = workbook.sheet_names()[0]
    sheet_content =  workbook.sheet_by_name(sheet1_name)
    sheet1_transform_json = []
    for val in range(1,sheet_content.nrows):
        row_content = {}
        for index in range(len(sheet_content.row_values(0))): 
            row_content[sheet_content.row_values(0)[index]] = sheet_content.row_values(val)[index]
        sheet1_transform_json.append(row_content)
    return sheet1_transform_json


# print()
file_url = './music.xlsx'
content_json = sheet1_content_transform_json(file_url)
with open('./music.json','a') as file_music_json:
    print(content_json)
    json.dump(content_json,file_music_json)

# print(content_json)
# sheet的名称，行数，列数
# print(workbook.sheet_names())