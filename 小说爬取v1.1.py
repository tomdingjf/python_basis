# -*- coding: utf-8 -*-

import requests
from lxml import etree

# 初始化书籍ID和书名
book_id = "66743"
shu_ming = "hq"
# 替换原文本中的特定字符串
replace_old_txt = "请收藏本站：https://www.biqg.cc。笔趣阁手机版：https://m.biqg.cc"
replace_new_txt = ""

# 定义完整网站地址和书籍具体地址
wan_zhan_server = "https://www.biqg.cc"
shujia_book = f" {wan_zhan_server}/book/{book_id}/"
url = f"{shujia_book}/1.html"
print(url)

# 定义XPath用于抓取文本内容、标题和下一页链接
wen_ben_zhu_ti = '//div/div/div[@class="Readarea ReadAjax_content"]/text()'
biao_ti = '//div/h1/text()'
xia_yi_zhan_url = '//div/div/div/a[@class = "Readpage_down js_page_down"]/@href'

# 无限循环，直至遍历完所有页码
while True:
    # 设置请求头，伪装为浏览器访问
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}

    # 发送HTTP请求并获取响应
    resp = requests.get(url, headers=headers)
    resp.encoding = "utf-8"

    # 使用lxml解析HTML响应文本
    e = etree.HTML(resp.text)

    # 提取正文内容，替换特定字符串
    info = "\n".join(e.xpath(wen_ben_zhu_ti))
    info = info.replace(replace_old_txt, replace_new_txt)

    # 提取书籍标题
    title = "\n".join(e.xpath(biao_ti))

    # 获取下一页URL
    url = f"{wan_zhan_server}{e.xpath(xia_yi_zhan_url)[0]}"

    # 如果URL未改变，说明已遍历到最后一页，循环结束
    if url == shujia_book:
        break

    # 将标题和正文内容写入文本文件
    with open(f"{shu_ming}.txt", "a", encoding="utf-8") as f:
        f.write("\n" + title + "\n" + info + "\n")
