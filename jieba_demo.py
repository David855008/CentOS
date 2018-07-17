# coding=utf-8
import jieba 
#一是嬰兒哭啼二是學遊戲三是青春物語四是碰巧遇見你
seg_list1 = jieba.cut("南橋供電等部分也沒有背光裝飾，邊緣音頻部分都特殊強化", cut_all=False)
print( "Default Mode: " + "/ ".join(seg_list1))