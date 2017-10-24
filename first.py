#import httplib
import datetime
import time

tarih="02.10.2016"
gun="Pazartesi"
vakit = "ogleden sonra"

print(tarih,gun,vakit,"buluşalım",end=".\n")

print(20*"=")

gun =22
gidis_ucreti = 1.5
gelis_ucreti = 1.5

masraf = gun*(gidis_ucreti+gelis_ucreti)

print("Toplam masraf",end="\n")
print("-"*20)
print("Çalışılan gün sayısı: \t",gun)
print("OTobus gidiş ucreti: \t",gidis_ucreti)
print("Otobus geliş ücreti: \t",gelis_ucreti)
print("-"*20)
print("Aylık toplam masraf:\t",masraf)

#veri = input("İşleminiz:")
#hesap=eval(veri)
#print(hesap)

#c= httplib.HTTPConnection('www.google.com')
#c.request("HEAD",'')
#if c.getresponse().status==200:
#    print("Url is real")
    
#url = input("Lütfen ulaşmak istediğiniz sitenin adını yazınız:")
#print("Hata! '{}' adlı site bulunamadı".format(url))
print("Yaz Okulu Başvuru Dilekçesi")
print(20*"=")

dilekçe= """

\t\t\t\t tarih: {}-{}-{} 
T.C                

{} Üniversitesi
{} Fakültesi Dekanlığına

Fakülteniz {} Bölümü {} numaralı öğrencisiyim\n
YAz okulunda '{}' dersine kayıt olmak istiyorum\n
Bilgilerinizi ve gereğini arz ederim.

\t\t\t\t\t\t İmza:

Ad    : {}
Soyad : {}
Numara: {}
TCNO  : {}

"""

now=datetime.datetime.now()
year=now.year
month=now.month
day=now.day
ad=input("Adınız:")
soyad=input("Soyadınız:")
tcno=input("TC kimlik numaranız:")
ogrencino =input("Öğrenci numaranız:")
uni = input("Üniversite adı:")
fakulte = input("Fakülteniz:")
ders = input("Alacağınız ders:")
bolum = input("Bölümünüzün Adı:")
print(dilekçe.format(day,month,year,uni,fakulte,bolum,
                     ogrencino,ders,
                     ad,soyad,ogrencino,tcno))


