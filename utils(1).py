import re

# import matplotlib.pyplot as plt
# plt.switch_backend('agg')
# import matplotlib.ticker as ticker
import time
import math
import unicodedata
from langconv import *

#编码码转换
def unicode2Ascii(s):
    return ''.join(
        c for c in unicodedata.normalize('NFD',s)
        if unicodedata.category(c) != 'Mn'
    )
#处理字符
def normalizeString(s):
    s=unicode2Ascii(s.lower().strip())
    s= re.sub(r"([.!?])",r" \1",s)
    s = re.sub(r"[^a-zA-Z.!?]+",r" ",s)
    return s

#繁体字转简体字
def cht_to_chs(line):
    line = Converter('zh-hans').convert(line)
    line.encode('utf-8')
    return line

def asMinutes(s):
    m = math.floor(s/60)
    s -= m*60
    return '%dm %ds' % (m,s)

def timeSince(since,percent):
    now = time.time()
    s = now - since
    es = s/(percent)
    rs = es -s
    return '%s (-%s)' % (asMinutes(s),asMinutes(rs))

# def showPlot(points):
#     plt.figure()
#     fig, ax = plt.subplots()
#     loc = ticker.MultipleLocator(base=0.2)
#     ax.yaxis.set_major_locator(loc)
#     plt.plot(points)