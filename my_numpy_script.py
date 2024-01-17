#matematiksel işlem. veri manipülasyonu
#numerical python/ array oluturmak için// yeniden şekillendirm// ındex secimi (vektorel seçim, yuksek işlem) // slicing// fancy ındex// verimli veri saklama (sabit veri oldugundan hepsine veri tipi atama yapmıyor, yer tutuyor işlemler hızlanıyor. // dongu yazmadan daha iyi dondurme



import numpy as np 


#clasic python yolu
a= [1,2,3,4]
b= [2,3,4,5]
ab= []
for i in range(0, len(a)):
    ab.append(a[i]*b[i])
print(ab)


#numpy ile:
a=np.array([1,2,3,4])
b=np.array([2,3,4,5])
ab=a*b
print(ab)


#numpy arrey oluşturmek:   ndarrey numpyin veri tipidir.

np.array([1,2,3,4,5])  #[liste]
print(type(np.array([1,2,3,4,5])))  # <class 'numpy.ndarray'>

print(np.zeros(10,dtype=int))    #10 tane integer typinde 0 

print(np.random.randint(0,10,size=10))  #0 ile 10 arasında rastgele 10 tane int seç

print(np.random.normal(10,4,(3,4)))  #ortama 10 stspma 4  matris 3esatır  4lüksutun  normal dagılım
#ve np.arange ile de oluştıurulur.


#numpy array özellikleri
a=np.random.randint(10,size=5)  #0dan 10a 5 tane      baslangıc default0 
print(a)
a.ndim   #boyut sayisi tek boyutlu oldugundan 1     
a.shape  #boyut bilgisi: 5   5 elamanlı oldugundan    satr stn
a.size   #toplam eleman sayısı    5
a.dtype  #int64




#reshaping  : boyut degistirmek istersek  ELEMAN SAYISI ÖNEMKİ 10A10LUĞU 3E3LÜK YAPAMAZSN! yada 33e3
v=np.random.randint(1,10,size=9)   #tek boyutlu bir array   9 elemanlı
print(v)

v=np.random.randint(1,10,size=9).reshape(3,3)    #3e3 boyutlu yaptıkkkkk
print(v)  

#or        v.reshape(3,3)   



#index işlemleri
c= np.random.randint(10, size=10)
c[0]     #index seçimi
c[0:5]   #slicing: dilimle seçme


#daha cok boyutluysa
m=np.random.randint(10, size=(3,5))  #0-10 3e5 boyutlu matris
print(m)
print(m[0,0])  #2 boyutun da numarasını vermeliyiz.
print(m[2,3])
m[2,3]=999
m[2,4]=2.9  #burada 2.9 degil 2 rakamı gelir cunku numpy tek turde deger saklar. eger diger hepsi int ise bu floati kabul etmez, kuuratı siler 2i koyar
print(m)

print(m[:,0]) #0.sutunun tum satırlarını seç
print(m[1,:])
print(m[0:2 , 0:3])



#fancy index: bir liste girdiginde kolayca seçtirir
j= np.arange(0,30,3)  #0dan 30a kadar 3er artanlı array oluştur
print("j: ",j)
print(j[1])
print(j[3])

catch=[1,2,3]    #hangi elemanları seçmek istiyorsn
print(j[catch])  #j arreyinden catchdeki elemanları getir.



#koşullu işlemler
g=np.array([1,2,3,4,5])

#amaç:3den kucuk elemanlara ulasalım
#FOR İLE 
ab=[]
for i in g:
    if i <3:
        ab.append(i)
print(ab)

#NUMPY İLE  g[] eleman seçecegim demek
print(g[g<3] )
print(g[g!=3])
#COK KOLAY... GENİŞLETİLEBİLİR.


#matmatiksel/istatiksel işlemler

v=np.array([1,2,3,4,5])
print(v/5)
print(v-1)
print(v**2)
print(np.subtract(v,1))
print(np.add(v,4))
print(np.mean(v))
print(np.var(v))
print(np.sum(v))
print(np.max(v))


#2 bilinmeyenli denklem
'''
5*x1 + x2 = 12
x1 + 3*x2 = 10
'''
a= np.array([[5,1], [1,3]])   #denklemin sol tarafındaki x1 ve x2nin katsayıları
b= np.array([12,10])          #denklemin sağ tarafı

print(np.linalg.solve(a,b))   #[1.85714286 2.71428571]



arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('1. boyuttaki 2.eleman: ', arr[0, 1])
print(arr)


arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1]) 
print(arr)
