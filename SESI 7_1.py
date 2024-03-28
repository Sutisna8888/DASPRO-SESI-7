#!/usr/bin/env python
# coding: utf-8

# In[5]:



# Syntax: For nama in object

# mencetak angka 1-10

for i in range (1,11):
 print(i, end =" ")


# In[6]:


#mencetak angka 10 20 30...100


for i in range (1,11):
 print(i *10, end=" ")


# In[7]:


#mencetak angka 10 20 30...100

for i in range (10,101):
 print(i, end=" ")


# In[8]:


# Mencetak angka 10 9 8 7....1

for i in range (1,11):
    print(11-i, end=" ")


# In[9]:


for i in range (100,0,-1):
    print(i, end=" ")


# In[10]:


#Mencetak angka 1 -2 3 -4 5 -6....10

sign = 1
for i in range (1,11):
  
     print(sign * i, end=" ")
     sign = sign * -1
  
 
    


# In[3]:


#mencari bilangan fakotorial

#input = 3, output = 3*2*1 = 6
#input = 4, output = 4*3*2*1 = 6

bil = int(input("Masukan bilangan : "))

hasil = 1

for i in range(1, bil+1):
    hasil = hasil * i
print(f"{bil}! adalah {hasil}")


# In[15]:


#mencari bilangan fakotorial

#input = 3, output = 3*2*1 = 6
#input = 4, output = 4*3*2*1 = 6

bil = int(input("Masukan bilangan : "))

hasil = 1
label = ""

for i in range(1, bil+1):
    
    hasil = hasil * i
    
    if i < bil :
        label = label + str((bil+1) - i) + " * "
    else:
        label = label + str((bil+1)-i)
        
print(f"{bil}! adalah {hasil}")
print(f"{label} = {hasil}")


# In[19]:


#menghitung pangkat

bil = int(input("Masukan bilangan : "))
pangkat = int(input("isukan pangkat : "))

hasil = 1

for i in range(1, pangkat+1):
    hasil *= bil
    
print(f"{bil} pangkat {pangkat} adalah {hasil}")


# In[ ]:


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
          
        

        


# In[ ]:




