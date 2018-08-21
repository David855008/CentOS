#-*- coding: utf-8 -*-
from PIL import Image
#import Image
import matplotlib
from matplotlib import pyplot as plt
import re
import pandas as pd
from collections import Counter
df = pd.read_excel('Deleted.xlsx', sheet_name = 'Raw Data')
newlist = []
oldlist = []
listMode = df['情緒標記']
counter = Counter(listMode)
totcounter=counter['正面']+counter['負面']+counter['中立']
poscounter=counter['正面']*100/totcounter
negcounter=counter['負面']*100/totcounter
neucounter=counter['中立']*100/totcounter
print("正面=",poscounter)
print("負面=",negcounter)
print("中立=",neucounter)
plt.rcParams['font.sans-serif']=['SimHei']
plt.figure(figsize=(6,9)) #调节图形大小
labels = [u'正面',u'中立',u'負面']
sizes = [poscounter,neucounter,negcounter]
colors = ['red','lightskyblue','yellow'] #每块颜色定义
explode = (0,0,0) #将某一块分割出来，值越大分割出的间隙越大
patches,text1,text2 = plt.pie(sizes,
                      explode=explode,
                      labels=labels,
                      colors=colors,
                      autopct = '%3.2f%%', #数值保留固定小数位
                      shadow = False, #无阴影设置
                      startangle =90, #逆时针起始角度设置
                      pctdistance = 0.6) #数值距圆心半径倍数距离
plt.axis('equal')
plt.savefig('testing.png')