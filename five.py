#-*- coding:utf-8 -*-

import string

sentence = input("Bir cumle giriniz:")

ilkharfler=[]


for w in sentence.split():
    ilkharfler.append(w[0])

for i in enumerate(ilkharfler):
    print(i)
    
