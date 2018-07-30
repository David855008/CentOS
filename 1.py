import re
import pandas as pd
from collections import Counter
import os
import os.path
if os.path.isfile('pandas_simple.xlsx'):
	os.remove('pandas_simple.xlsx')
df = pd.read_excel('Deleted.xlsx',sheet_name = 'Raw Data')
new_list = []
old_list = []
extra_list = []
count_reply = 0
count_trigger = 0
countnew = 0
countold = 0
listTopic = df['監測主題']
listTitle = df['標題']
listPos = df['正面強度']
listNeg = df['負面強度']
listMode = df['情緒標記']
listLink = df['原始連結']
listCate = df['主文/回文']
for i in listCate:
	if '回文' in i:
		extra_list.append('回文')
	else:
		extra_list.append('主文')
for (i,j) in zip(reversed(listCate),reversed(listTitle)):
	if i == '主文':
		new_list.append(j)
		countnew+=1
for (i,j) in zip(reversed(listCate),reversed(listTitle)):
	if '回文' in i:
		count_reply+=1
		if not j in old_list:
			if not j in new_list:
				old_list.append(j)
				countold+=1
			elif j in new_list:
				count_trigger+=1

counter = Counter(listCate)
counterGB = Counter(extra_list)
print(counterGB.get('主文'))
print(counterGB.get('回文'))
#print(extra_list)
#print(counter.get('主文'))
mode = listMode.value_counts()
dw = pd.DataFrame({'總文章數': [listTopic.count()],
				   '新文數': [countnew],
				   '舊文數': [countold],
				   '總回文數': [count_reply],
				   '新文引發回文數':[count_trigger],
				   '舊文引發回文數':[count_reply-count_trigger],
				   '正面': [mode.get('正面')],
				   '中立': [mode.get('中立')],
				   '負面': [mode.get('負面')],
				   '正面程度': [sum(listPos)],
				   '負面程度': [sum(listNeg)]
				   })
writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')
dw.to_excel(writer, sheet_name='總覽')
writer.save()
writer.close()
