#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Mengecek bilangan prima
#bilangan prima adalah bilangan yang hanya habis dibagi dengan 1 dan bilangan itu sendiri => 2 faktor


bil = int(input("Masukan bilangan"))

jumlah = 0 

for i in range(1, bil + 1):
    sisa = bil % i
    
    if sisa == 0:
        jumlah = jumlah + 1
        
if jumlah == 2:
       print(f"{bil} adalah bilangan PRIMA")
else: 
        print(f" {bil} adalah bukan bilangan PRIMA")
          


# In[7]:


bil = int(input("Masukan bilangan "))
keterangan = "Bilangan prima"
jumlah = 0 

for i in range(1, bil + 1):
    sisa = bil % i       
    if jumlah == 0:
        print(f" {bil} adalah bukan bilangan PRIMA")
    

    
print(f"{bil} adalah {keterangan}") 
          


# In[2]:


#Break

for i in range(1,100):
    print(i)
    if i==5:
        break


# In[4]:



for i in range(1,100):
    print(i)
    if i==5:
        break
        
print()
for j in range (1,10):
    if j==5:
        continue
    print(j, end=" ")


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



kalimat = input ('Isikan kalimat')
panjang = len(kalimat)

for i in range(0,panjang):
    kika = kalimat[i]
    kaki = kalimat[panjang-i - 1]
    print(kika,kaki)

