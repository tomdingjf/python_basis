# -*- coding: utf-8 -*-
import requests
from lxml import etree


def cha_hao_ma(number):
    """
    查询指定手机号码的归属地信息。
    
    参数:
    number: str - 需要查询归属地的手机号码。
    
    返回值:
    无返回值，直接在控制台打印归属地信息。
    """
    # 构造查询URL
    url = f"https://shouji.ip38.com/{number}.html"

    # 设置请求头，模拟浏览器访问
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    }
    # 发起HTTP GET请求
    response = requests.get(url, headers=headers)
    # 解决中文乱码问题
    response.encoding = "utf-8"
    # 获取响应内容
    html = response.text

    # 使用lxml的HTML解析器解析HTML内容
    html = etree.HTML(html)

    # 打印解析出的归属地信息
    data = html.xpath('/html/body/div[2]/div[2]/div[2]/div[2]/p[1]/text()')

    result = [item.strip() for item in data if item.strip()]
    print(f"手机号码：          {number}")
    print(f"归属地定位：         {result[0]}")
    print(f"运营商 & SIM卡类型： {result[1]}")
    print(f"手机号段：          {result[2]}")
    print(f"归属地区号：         {result[3]}")
    print(f"归属地邮证编码：      {result[4]}")


if __name__ == "__main__":
    # 调用函数，查询指定手机号码的归属地
    cha_hao_ma("13972536393")
