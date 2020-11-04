
# @Author: jiejie
# @Date:   2020-11-03 19:40:48
# @Last Modified by:   jiejie
# @Last Modified time: 2020-11-04 08:37:55
# -*- coding: gb2312 -*-

# 初级文章爬取
import requests

if __name__ == '__main__':
        # 当在最后加上反斜杠就会出现乱码！！！注意
    # target = 'http://www.biqukan.com/1_1094/'
    target = 'http://www.biqukan.com/1_1094/5403177.html'
    req = requests.get(url=target)
    print(req.text)


# 带有特殊符号的爬取
# from bs4 import BeautifulSoup
# import requests
# if __name__ == "__main__":
#     target = 'http://www.biqukan.com/1_1094/5403177.html'
#     req = requests.get(url=target)
#     html = req.text
#     bf = BeautifulSoup(html)
#     texts = bf.find_all('div', class_='showtxt')
#     print(texts)

# 最终文字爬取
# from bs4 import BeautifulSoup
# import requests
# if __name__ == "__main__":
#     target = 'http://www.biqukan.com/1_1094/5403177.html'
#     req = requests.get(url=target)
#     html = req.text
#     bf = BeautifulSoup(html)
#     texts = bf.find_all('div', class_='showtxt')
#     print(texts[0].text.replace('\xa0' * 8, '\n\n'))
