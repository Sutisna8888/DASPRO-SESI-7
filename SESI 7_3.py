#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# LOOPING untuk string, menghitung huruf vokal

kalimat = input("Masukan kalimat")

vokal_a = 0
vokal_i = 0
vokal_u = 0
vokal_e = 0
vokal_o = 0

for i in kalimat:
    if i=='a' : 
        vokal_a += 1
    elif i=='i' :    
         vokal_i += 1
    elif i=='u' :
        vokal_u += 1
    elif i=='e' :
        vokal_e += 1
    elif i=='o' :
        vokal_o += 1
            
                        
print(f"Jumlah huruf a:{vokal_a} ")
print(f" jumlah huruf i : {vokal_i} ")
print(f" jumlah huruf u : {vokal_u} ")
print(f" jumlah huruf e : {vokal_e} ")
print(f" jumlah huruf o : {vokal_o} ")

total = vokal_a+vokal_i+vokal_u+vokal_e+vokal_o
print(f"jumlah total huruf vokal {total}")


# In[ ]:


#kalimat polindrome atau bukan
#polindrome adalah kalimat yang dibaca dari kiri ke kanan == dari kanan ke kiri
#katak => polindrome

ulang = "Y"
while(ulang=="Y")

    kalimat = input ('Isikan kalimat : ')
    panjang = len(kalimat)
    keterangan = "PALINDROME"
    for i in range(0,panjang):
        kika = kalimat[i]
        kaki = kalimat[panjang-i - 1]
        print(kika,kaki)

        if kika != kaki :
            keterangan = "BUKAN PALINDROME"
            break

    print(f"{keterangan}")


# In[ ]:


ulang = "Y"
while(ulang =="Y"):

    kalimat = input ('Isikan kalimat : ')
    panjang = len(kalimat)
    keterangan = "PALINDROME"
    for i in range(0,panjang):
        kika = kalimat[i]
        kaki = kalimat[panjang-i - 1].lower()
        print(kika,kaki)

        if kika != kaki :
            keterangan = "BUKAN PALINDROME"
            break

    print(f"{keterangan}")
    jawab =""
    while (jawab!="Y" and jawab!="T")
     ulang = input("Apakah mau mengulang program (T/Y)? : ")
    ulang = jawab

