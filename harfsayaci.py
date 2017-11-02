#-*- coding:utf-8 -*-
import string
import sys
import time
from os import*


class HarfSayaci:

    def __init__(self):
        self.sesli=0
        self.sessiz=0
        self.sesli_harfler="aeıioöuü"
        self.sessiz_harfler="bcçdfgğhjklmnprsştvyz"

    def kelime_sor(self):
        return raw_input("Bir şeyler yazınız")

    def seslimi(self,harf):
        return harf in self.sesli_harfler

    def sessizmi(self,harf):
        return harf in self.sessiz_harfler

    def artir(self):
        for harf in self.kelime:
            if self.seslimi(harf):
                self.sesli+=1
            if self.sessizmi(harf):
                self.sessiz+=1
        return(self.sesli,self.sessiz)


    def ekrana_bas(self):
        sesli,sessiz = self.artir(self)
        mesaj = "{} stringinde {} adet sesli , {} adet sessiz harf vardır"
        print(mesaj.format(self.kelime,sesli,sessiz))

    def calistir():
        self.kelime = self.kelime_sor()
        self.ekrana_bas()


if __name__=="main":
    sayac = HarfSayaci()
    sayac.calistir()
