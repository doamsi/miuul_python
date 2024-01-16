#örnek1: Bir veri setindeki değişken isimlerini değiştirmek mesela upper yap

import seaborn as sns   #kutup import etk
df = sns.load_dataset("car_crashes") #carcrashes veri setini getir
df.columns  

liste=[]
for col in df.columns:
    liste.append(col.upper())

#print(liste)     #['TOTAL', 'SPEEDING', 'ALCOHOL', 'NOT_DISTRACTED', 'NO_PREVIOUS', 'INS_PREMIUM', 'INS_LOSSES', 'ABBREV']
df.columns= liste
print(df.columns) 
#Index(['TOTAL', 'SPEEDING', 'ALCOHOL', 'NOT_DISTRACTED', 'NO_PREVIOUS', 'INS_PREMIUM', 'INS_LOSSES', 'ABBREV'],dtype='object')



df.columns= [col.upper() for col in df.columns]
print(df.columns)




#örnek2: isminde INS olan car_crashdaki degiskenerin basına FLAG, digerlerine NO_FLAG getir.

df.columns= ["FLAG" + col.upper() if "INS" in col else "NO_FLAG" + col for col in df.columns ]           # "__" + col  = ___col   string+string 
print(df.columns)    




#örnek3: keyi string valuesiicinde fonx isimleri de string. Sadece sayısal degiskenlerle iş yapmak istiyoruz

import seaborn as sns   #kutup import etk
df = sns.load_dataset("car_crashes") #carcrashes veri setini getir
df.columns

num_cols= [col for col in df.columns if df[col].dtype != "O"]   #data type= object olmayanlar yani int olan sutunları seçti (numericleri seçti)
soz = {}  #bos sozluk olusturduk
agg_list= ["mean", "min", "max", "sum"]   #value kısmı oluşturduk

for col in num_cols:
    soz[col]= agg_list   # key[numaric sutunlar]= value[meanmaxminsum degerleri]

#OR 
a={col: agg_list for col in num_cols}
print("a=", a)

new_dict= {col: agg_list for col in num_cols}

df[num_cols].head() #df[__] yaparsan o degiskenleri seçer datafream


a=df[num_cols].agg(new_dict)
print(a)