# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import requests
import xlwt
import pymysql
from bs4 import BeautifulSoup
from lxml import etree
from flask import Flask,render_template
# def test():
#     url="https://search.51job.com/list/050000,000000,0000,00,9,99,%25E8%2587%25AA%25E5%258A%25A8%25E5%258C%2596,2,2.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84'    }
#     response=requests.get(url=url,headers=headers)
#     print(response.status_code)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

def get_data():
    pass



def main():
    pass
    

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000,debug=True)
