#-*- coding:utf-8 -*-
import string
import sys
import time
from os import*


class Calisan:

   personel = []

   def __init__(self,name):
       self.name= name
       self.talents=[]
       self.addtoPersonel()


   def addtoPersonel(self):
       self.personel.append(self.name)
       print("{} adlı kişi personel listesine eklendi".format(self.name))

    ## bu fonksiyona sınıf adı üzerinden erişebilmek için @classmethod bezeyicisini ekledik.
   @classmethod
   def getPersonel(self):
       print(10*('*'),"Personel Listesi",10*('*'))
       for p in self.personel:
           print(p)

   ## bu fonksiyona sınıf adı üzerinden erişebilmek için @classmethod bezeyicisini ekledik.
   ## Yani bu sınıfı örneklemek zorunda kalmadan da metodu çalıştırabiliriz
   @classmethod 
   def showPersonCount(self):
       print(10*('*'),"Toplam Personel Sayısı",10*('*'))
       print(len(self.personel))

   def addTalent(self,talent):
       self.talents.append(talent)

   def displayTalents(self):
       print(10*'=',"Personelin Kabiliyetleri",10*'=')
       for t in self.talents:
           print(t)
       



   

