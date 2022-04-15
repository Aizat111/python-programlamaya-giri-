#!/usr/bin/env python
# coding: utf-8

# In[15]:


sesli_harfler='aeıioöuü'
sayac=0
def kelime_sor():
    return input("Bir kelime girin: ")
def seslidir(harf):
    return harf in sesli_harfler
def adet(kelime):
    global sayac
    for harf in kelime:
        if seslidir(harf):
            sayac+=1
    return sayac
def ekrana_bas(kelime):
    mesaj='{} kelimesinde {} adet sesli harf var'
    print(mesaj.format(kelime,adet(kelime)))
            
def calistir():
    kelime=kelime_sor()
    ekrana_bas(kelime)
calistir()

#eğer import ettiğimizde çalışmayıp sadece kendini çağırınca çalışsın diyorsak
#if __name__=='__main__': calistir() deriz

# In[ ]:





# In[ ]:




