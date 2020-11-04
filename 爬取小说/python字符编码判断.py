# -*- coding: utf-8 -*-
# @Author: jiejie
# @Date:   2020-11-03 21:24:01
# @Last Modified by:   jiejie
# @Last Modified time: 2020-11-03 21:34:53
# 更改网站即可
import urllib.request
rawdata = urllib.request.urlopen('http://www.biqukan.com/1_1094/').read()
import chardet
result = chardet.detect(rawdata)
print(result)
