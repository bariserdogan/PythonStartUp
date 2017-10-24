#-*- coding:utf-8 -*-
# döngü ile hata yakalama programı
import sys
import time

while True:
    ilksayi = input("İlk sayi(Lütfen çıkmak için q ya basınız):")

    if ilksayi == "q":
        print("Çıkılıyor")
        time.sleep(2)
        sys.exit()

    ikincisayi = input("İkinci sayiyi giriniz:")

    try:
        sayi1 = int(ilksayi)
        sayi2 = int(ikincisayi)
        sonuc = sayi1/sayi2
        print ("Sonuc: {}".format(sonuc))
    except ValueError as hata:
        print("===== Lütfen sadece sayı giriniz =====")
        print("Beklenmedik Değer: { }".format(hata))
        
    except ZeroDivisionError :
        print("Hiçbir sayı 10'a bölünemez")
        
        
