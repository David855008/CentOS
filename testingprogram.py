# coding=utf-8
import jieba 
import word2vec
from hanziconv import HanziConv

# 讀檔：一條一條讀進來
fileTrainRead = []
with open('corpus_simpl.txt') as      fileTrainRaw:
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
seg_list1 = jieba.cut("一是嬰兒哭啼二是學遊戲三是青春物語四是碰巧遇見你", cut_all=False)
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
for i in range(5,10):
    print (model.vocab[i])
"""for i in range(995,1000):
    print (model.vocab[i])"""