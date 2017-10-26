#-*- coding:utf-8 -*-
import string
import sys
import time
from os import*


sesli_harfler="aeıioöuü"

katar = raw_input("Bir şeyler yazın:")

yeni_list=[]

sayac=0
for k in katar:
    if k in sesli_harfler:
       if k not in yeni_list:
           yeni_list.append(k)
           sayac+=1

mesaj = "{} kelimesinde {} adet sesli harf vardır"
for y in yeni_list:
    print(y)
print(mesaj.format(katar,sayac))
    
