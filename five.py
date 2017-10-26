#-*- coding:utf-8 -*-

import string
import sys
import time
from os import name
import subprocess as sp

##sentence = input("Bir cumle giriniz:")
##
##ilkharfler=[]
##
##
##for w in sentence.split():
##    ilkharfler.append(w[0])
##
##for i in enumerate(ilkharfler):
##    print(i)


#recursive function examps

def decrease(word):
    if len(word) < 1:
        return word

    else:
        print(word)
        return decrease(word[1:])

print(decrease("erdogan"))


sys.getrecursionlimit()
def decrease(word):
    if len(word) < 1:
        return word

    else:
        print("Özyineleme sürecine girerken:",word)
        time.sleep(0.5)
        decrease(word[1:])
        time.sleep(0.5)
        print("Özyineleme sürecinden çıkarken:",word)
        
decrease("erdogan")

def fact(sayi):

    if sayi==1 or sayi == 0:
        return 1;
    
    else:
        return sayi * fact(sayi-1)

num = input("Faktöriyeli alınacak sayı")

print("Sonuc: {}".format(fact(int(num))))

#sp.call("seven.py")




