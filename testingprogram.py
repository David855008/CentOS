#coding=utf-8
import jieba 
import word2vec
from hanziconv import HanziConv

# 讀檔：一條一條讀進來
fileTrainRead = []
with open('test.txt',"rb") as      fileTrainRaw:
  for line in fileTrainRaw:
      fileTrainRead.append(HanziConv.toTraditional(line)) # 簡轉繁
      # 斷詞
fileTrainSeg=[]
for i in range(len(fileTrainRead)):
    fileTrainSeg.append([' '.join(list(jieba.cut(fileTrainRead[i][9:-11],cut_all=False)))])
# 因為會跑很久，檢核是否資料有持續在跑
    if i % 50000 == 0 :
        print (i)
# 精確模式、同時也是預設模式
seg_list1 = jieba.cut('corpus123.txt', cut_all=False)
print( "Default Mode: " + "/ ".join(seg_list1)  )
# 將jieba的斷詞產出存檔
fileSegWordDonePath ='corpusSegDone.txt'
with open(fileSegWordDonePath,'wb') as fW:
    for i in range(len(fileTrainSeg)):
        fW.write(fileTrainSeg[i][0].encode('utf-8'))
# 檢視斷詞jieba的結果
def PrintListChinese(list):
    for i in range(len(list)):
        print (list[i],end=" ")
PrintListChinese(fileTrainSeg[10])
# jieba分詞轉word2vec向量
word2vec.word2vec('corpusSegDone.txt', 'corpusWord2Vec.bin', size=300,verbose=True)
model = word2vec.load('corpusWord2Vec.bin')
#for i in range(5,10):
#    print (model.vocab[i])
"""for i in range(995,1000):
    print (model.vocab[i])"""
zhfont = matplotlib.font_manager.FontProperties(fname='/Users/youngmihuang/Downloads/wqy-microhei.ttc')
# 畫圖
fig = plt.figure()
ax = fig.add_subplot(111)
 
for i in index1:
    ax.text(X_reduced[i][0],X_reduced[i][1],model.vocab[i], fontproperties=zhfont,color='C3')
for i in index2:
    ax.text(X_reduced[i][0],X_reduced[i][1],model.vocab[i], fontproperties = zhfont,color= 'C1')
for i in index3:
    ax.text(X_reduced[i][0],X_reduced[i][1],model.vocab[i], fontproperties=zhfont,color='C7')
for i in index4:
    ax.text(X_reduced[i][0],X_reduced[i][1],model.vocab[i], fontproperties=zhfont,color='C0')
for i in index5:
    ax.text(X_reduced[i][0],X_reduced[i][1],model.vocab[i], fontproperties=zhfont,color='C4')
ax.axis([0,0.5,-0.2,0.6])
plt.figure(figsize=(60,60))
plt.show()
