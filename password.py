# 创建密码

    # 需求如下
    #     1、6-20个字符（数字、大写字母，小写字母组成）
    #     2、相邻连续3个字符不能相同
    #     3、至少含有1个大写字母，1个小写字母，一个数字
    # 实现如下功能：

    # script :
    # let reg = /\w{6,20}/ 

#  已知1998年是平年，1.2号星期五，要求输入一个年份（大于1998） ，能够判断是否闰年，并返回该年份中即是周五又是13号的月份的个数
import time , datetime
# print(time.time())
# tss1 = '1998-01-02 23:40:00'
# 转为时间数组
# timeArray = time.strptime(tss1, "%Y-%m-%d %H:%M:%S")
# print(timeArray)
def is_leap_year (num) :

    year = int (num)
    count_mon = 0
    is_leap = '平年'

    if(year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
        is_leap = '闰年'

    for m in range(1,13):
        year_str = '{0}-{1}-13'.format(year,m)
        timeArray = time.strptime(year_str, "%Y-%m-%d")
        if timeArray[6] == 4 :
            count_mon += 1
    print('{0}是{1},周五又是13号的月份的个数{2}'.format(year,is_leap,count_mon))

year_string = input('请输入年')
is_leap_year(year_string)