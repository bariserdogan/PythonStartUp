#-*- coding:utf-8 -*-
# Search in dictionary
import string
import sys
import time


def main():
    
    sozluk = { "kitap":"book",
               "bilgisayar":"computer",
               "masa":"table",
               "programlama":"programming",
               "envanter":"inventory"}
    sozcukler=[]
    counter=0
    while True:
        giris =input("Bir şey veya birseyler yazın(Çıkmak için q)")

        if giris=="q" :
            print("Çıkılıyor...")
            time.sleep(2)
            sys.exit()

        else:
            if counter <= 5:
                sozcukler.append(giris)
                counter+=1
            else:
                break
        
    
    karsilik_bul(*sozcukler,**sozluk)



def karsilik_bul(*args,**kwargs):
    for sozcuk in args:
        if sozcuk in kwargs:
            print("{} = {}".format(sozcuk,kwargs[sozcuk]))
        else:
            print("Aradığınız sözcük : {} ,sözlükte bulunmuyor".format(sozcuk))




main()
