
type(0.2)
#sadece 6yı seçerek sağ click ile tek o satırı calıstırabilirizi

a=10
a*10  #bu iki satır secilerek a*10 işlemi yaptırabilirsin


#int-float-booolen VE:
#-------------------------------------------------------------------------------------------------------
#strngs

name= "Ilgın"
print(name)
name[0]
name[0:2]
"u" in name  #FALSE.

#STRING METODLARINA ERİŞMEK İÇİN dir(str)
print(dir(str))    #harfleri kucultme buyutme vb metodlar..

name = "john"
type(len)   #<class 'builtin_function_or_method'>
len(name)

"john".upper()
"jOHN".lower()

hi="hello naber lalalala"
hi.replace("l", "p")

"hello ai era".split() #boslukla böl

" ofofoof ".strip()   #KIRPMA İSLEMİ YAPAR EN BAŞ VE EN SONU "ofofoof"
"ofofofo".strip("o")   #fofof


#-------------------------------------------------------------------------------------------


#LİSTE list: değiştirilebilir, sıralıdır(index işlemi yapılır, kapsayıcıdır)
x=["btc", "eth", "xrp"]
type(x)

notes= [1,2,3,4,"a","b", True, [1,2,3]]
type(notes)  #LİST
print(notes[7][1])
notes[2]= 80   #veri güncelleme
print(notes)
notes[0:4]  #1den 4. elemana kadar yazdırır 1 2 80 4



#liste metodları(en önemlisi append)

notes.append(100)
notes


notes.pop(0)      #indexe göre siler 0. indexi siler calıstıgında da sildigi seyi gösterir
notes

notes.insert(2, 99)  #kaçıncı indexe ne ekleyeceksin  3. char= 99 oldu. insert bir metodur(self, index, number that you want to insert(object))
notes


#----------------------------------------------------------------------------------------------------------
#sözlük: degistirilebilir, sırasızdır(3.7 sürümünden sonra sıralıdır), kapsayıcıdır.

x={"name": "Peter", "Age" : 36}     #{key: value, key:value}
type(x)


dic={"reg": "regression",
     "log": "logistic reg" , 
     "cart" : "classification and reg"
    }

dic["reg"]   #>>>> 'regression'  DÖNDURUR               sözlük[key]= value




dic={"reg": ["regression",10],
     "log": ["logistic reg",20] , 
     "cart": ["classification and reg",30]
    }
dic["reg"]  #>>>> ['regression', 10]
dic["cart"][1] #>>>>> 30 dondurur
dic.get("reg")  #dic["reg"] ile aynı

dic.keys() #tüm keyler gelir
dic.values() #tüm valueler gelir
dic.items() #tüm elemanalar gelir tuple şeklinde

dic.update({"reg": 11})  #regi güncelledi
dic.update({"rf": 10})  #yeni deger koydu
dic


#---------------------------------------------------------------------------------------------------------------
#tuple(demet): degistirilemez, listenin aksi kardesi, sıralı(elemanlara erişlebilir), kapsayıcı

x =  ("python","ml","ds")
x[0]
x[0:2]
#t[0]=99 #degistirilemez!!!!!! e nasil? listeye cevirip yap güncelle sonra tuplea cevir

x=list(x)
x[0]=99
x=tuple(x)
x



#-------------------------------------------------------------------------------------------------------------
#set  degistirilebilir, sırasız==INDISLENEMEZ SET[1]X  ANCA FOR DONGUSU İLE , eşsiz ,kapsayıcı

x = {"python", "ml"}

set1=set([1,2,3])  #liste üzerinden de set oluşturulur
set2=set([1,2,5])

set1.difference(set2)  #set1de olup set2de olmayanlar cvp: {3}
set1.symmetric_difference(set2) #iksinde de birbirinde olmayanlar {3,5}
set1.intersection(set2) #iki kumede de ortak olan {1,2}
set1&set2 #{1, 2} ORTAK KÜME
set1.union(set2)  #2 kumenin birleşimi {1, 2, 3, 5}
set1.isdisjoint(set2) #İki kumenin kesişimi boş mu FALSE >> 1 2 VAR
set1.issubset(set2)      #set1 set2nin alt  kumesi mi FALSE 
set2.issuperset(set1) #sete2 set1i kapsıyo mu FALSE



























#NOT: Liste, tuple, set ve dic veri yapıları aynı zamanda Python Collections (Arrays) olarak geçmektedir






