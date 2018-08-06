# coding=utf-8
import jieba 
#type in some stuff
s=input("輸入")

seg_list1 = jieba.cut(s, cut_all=False)
print( "Default Mode: " + "/ ".join(seg_list1))
