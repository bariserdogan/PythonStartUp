#-*- coding:utf-8 -*-
#random işlemleri

import random
import string

liste=[]
i=0
while i<7:
    k=raw_input("İsim giriniz:")
    liste.append(k)
    i=i+1

print("Orjinal Liste")
for n in liste:
    print(n)

print("{{{{{{{{{{{{===========}}}}}}}}}}}}}}}}}}}}}}}}")

newlist=[]
for i in range(len(liste)):
    temp = random.choice(liste)
    if temp not in newlist:
        newlist.append(temp)
    else:
        print("Ooops...!!! Aynı öğeler tekrar tekrar çekilemez")
     

print("Yeni oluşturulmuş liste:\n********************")
for n in newlist:
    print(n)




    
