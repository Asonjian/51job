#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：51job 
@File    ：main.py.py
@Author  ：安健
@Date    ：2022/1/3 16:05 
'''
import requests
import xlwt
import pymysql
from bs4 import BeautifulSoup
from lxml import etree
import wordcloud

def get_html(src):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84'}
    cookies = {'acw_sc__v2':'61d3000171599fd9df8bfe9a4596efb8b322365e'}
    response = requests.get(url=src, headers=headers,cookies=cookies)
    response.encoding = response.apparent_encoding
    return response


def xpth_html(html_data):
    html_data = html_data.text
    tree = etree.HTML(html_data)
    div_list = tree.xpath("/html/body/div[2]/div[3]/div/div[2]/div[4]/div[1]")
    print(div_list)
    for div in div_list:
        station = div.xpath("div[1]/a/p[1]/span[1]/@title")
        print(station)


def init_base():
    # 连接数据库
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123', db='51job')
    cursor = conn.cursor()  # 建立一个游标
    # 数据库建立以及建表
    sql = '''
        create table data_list
        (
        `order` int primary key AUTO_INCREMENT,
        `station` char,
        `enterprise_name` char,
        `enterprise_type` char,
        `enterprise_address` char,
        `degree` char,
        `salary` char
        )
    '''
    cursor.execute(sql)  # 提交sql
    print("\n creat table successd ! \n")
    conn.commit()  # 提交数据库操作
    conn.close()  # 关闭数据库


def main():
    # for i in range(300):
    #     try:
    #         src="https://search.51job.com/list/050000,000000,0000,00,9,99,%25E8%2587%25AA%25E5%258A%25A8%25E5%258C%2596,2,"+str(i) +".html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
    #         html_data=get_html(src)
    #         xpth_html(html_data)
    #     except:
    #         break
    src = "https://search.51job.com/list/050000,000000,0000,00,9,99,%25E8%2587%25AA%25E5%258A%25A8%25E5%258C%2596,2," \
          "1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0" \
          "&dibiaoid=0&line=&welfare= "
    html_data = get_html(src)
    print(html_data.text)
    xpth_html(html_data)


if __name__ == '__main__':
    # init_base()
    main()
