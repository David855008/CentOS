#oding=utf-8
import jieba 
import word2vec
from hanziconv import HanziConv

# 讀檔：一條一條讀進來
fileTrainRead = []
with open('taiwanmobile.txt',"rb") as      fileTrainRaw:
  for line in fileTrainRaw:
      fileTrainRead.append(HanziConv.toTraditional(line)) # 簡轉繁
      # 斷詞
fileTrainSeg=[]
for i in range(len(fileTrainRead)):
    fileTrainSeg.append([' '.join(list(jieba.cut(fileTrainRead[i][9:-11],cut_all=False)))])
# 因為會跑很久，檢核是否資料有持續在跑
    if i % 50000 == 0 :
        print (i)

jieba.set_dictionary('dict.txt.big')
jieba.load_userdict("dict.txt")
# 精確模式、同時也是預設模式
jieba.add_word('台灣大哥大')
jieba.add_word('中華電信')
jieba.add_word('台灣之星')
jieba.add_word('攜碼')
jieba.add_word('台哥大')
jieba.add_word('中華')
jieba.add_word('遠傳')
jieba.add_word('基地台')
jieba.add_word('亞太')
jieba.add_word('或')
jieba.add_word('台灣')
jieba.add_word('之星')
jieba.add_word('，')
jieba.add_word('。')
jieba.add_word('）')



seg_list1 = jieba.cut('corpus123.txt', cut_all=True)
print( "Default Mode: " + "/ ".join(seg_list1)  )
# 將jieba的斷詞產出存檔
fileSegWordDonePath ='corpusSegDone.txt'
with open(fileSegWordDonePath,'wb') as fW:
    for i in range(len(fileTrainSeg)):
        fW.write(fileTrainSeg[i][0].encode('utf-8'))
        print(fileTrainSeg[i][0])
# 檢視斷詞jieba的結果
def PrintListChinese(list):
    for i in range(len(list)):
        print (list[i],end=" ")
PrintListChinese(fileTrainSeg[10])
# jieba分詞轉word2vec向量
word2vec.word2vec('corpusSegDone.txt', 'corpusWord2Vec.bin', size=100,verbose=True)
model = word2vec.load('corpusWord2Vec.bin')
print(model.vocab.size)
#for i in range(model.vocab.size):
    #print (model.vocab[i])

print("跟'遠傳'最相關的詞彙：")
# '遠傳' 的相關字詞
indexes = model.cosine(u'中華')
for index in indexes[0]:
    print (model.vocab[index])
