#-*- coding:utf-8 -*-
# metindeki kelime sayısı
import string

global counter

def wordCount(text):
    newtext = text.split(" ")
    counter=0
    for word in newtext:
        if isword(word) and len(word)>3:
            counter+=1
        else:
            print("""Harf sayısı 3'ten az olan öğeler
    kelime olarak kabul edilmemektedir""")
    return counter


def isword(katar):
    for ch in katar:
        if not ch in string.punctuation:
            return True
    return False


sentence = input("Bir cümle giriniz:")
print("Toplam kelime sayısı: {}".format(wordCount(sentence)))
