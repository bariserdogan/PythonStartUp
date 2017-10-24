#-*- coding:utf-8 -*-

import string

# Girilen bir metindeiki kelimelerin ilk harfini büyüten program

##sent = raw_input("Bir cümle giriniz:")
##
##sent = sent.split()
##
##for s in sent:
##    if s.startswith("i"):
##        s = s.replace(s[0],"İ")
##        s = s.capitalize()
##        print(s)
##    else:
##        s = s.capitalize()
##        print(s)

# Hangi harften kaç tane olduğunu gösteren program

sent = raw_input("Bir cümle giriniz:")
counter=0

for k in sent[:]:
    counter=0
    if k != ' ':
        for x in sent[:]:
            if k == x:
                counter+=1
                print(k,counter)
    else:
        pass
            
        

