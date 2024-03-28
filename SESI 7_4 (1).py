#!/usr/bin/env python
# coding: utf-8

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
    while (jawab!="Y" and jawab!="T"):
     ulang = input("Apakah mau mengulang program (T/Y)? : ")
    ulang = jawab


# In[2]:


#NESTED for

for i in range(1,5):
    for j in range(1,5):
         print(i,j)

