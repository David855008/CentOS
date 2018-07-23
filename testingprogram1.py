import re
import pandas as pd
from collections import Counter
df = pd.read_excel('Deleted.xlsx', sheet_name = 'Raw Data')
newlist = []
oldlist = []
count = 0
count_reply = 0
count_new = 0
count_old = 0
count_trigger = 0
listTopic = df['監測主題']
listTitle = df['標題']
listContent = df['內容']
listSource = df['來源']
listForum = df['來源網站']
listCate = df['主文/回文']
listTime = df['發佈時間']
listTotal = df['討論串總則數']
listPV = df['點閱數']
listAuthor = df['作者']
listPos = df['正面強度']
listNeg = df['負面強度']
listMode = df['情緒標記']
listLink = df['原始連結']
print(df['正面強度'].count())
for Cate in listCate:
	if Cate == '主文':
		#print(count,listTitle[count],Cate)
		newlist.append(listTitle[count])
		count_new+=1
	count+=1

count = 0
for Cate in listCate:
	if '回文' in Cate:
		count_reply+=1
		if not listTitle[count] in newlist:
			#print(count,listTitle[count],Cate)
			if not listTitle[count] in oldlist:
				oldlist.append(listTitle[count])
				count_old+=1
		else:
			count_trigger+=1
	count+=1
counter = Counter(listCate)
print("總文章數=",listTopic.count())
print("新文數=",counter['主文'])
print("舊文數=",count_old)
print("總回文數=",count_reply)
#print(counter['主文'])
#print("總回文數=",listCate.["回文"]count(level="回文"))
print("新文引發回文數=",count_trigger)
print(listMode.value_counts())