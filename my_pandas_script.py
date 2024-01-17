##PANDAS veri analizinde en sık kullanılan kutup.
#

import pandas as pd 

s=pd.Series([10,77,12,4,5])
print(type(s))  #int64
print(s)
'''
0    10
1    77
2    12
3     4
4     5
'''
print(s.index) #RangeIndex(start=0, stop=5, step=1)
print(s.size)  #5 eleman
print(s.ndim)  #1 tek boyutlu
print(s.values) #array([10,77,12,4,5])    numpy.ndarray olarak döndürülür.
print(s.head(3)) # ilk 3 degeri döndürür
print(s.tail(3))  #son 3 degeri döndürür



#DIŞ KAYNAKLI VERİ OKUMA  csv dosyalar

import pandas as pd

file_path = r"C:\Users\Dell\Desktop\PartData.csv"
df = pd.read_csv(file_path, encoding='ISO-8859-1')  #karakter kodlamasıyla ilgili sorun varmıs CHATGBT YAZDI. 
print(df.head())

'''
  isim;dogum yili;tecrube;maas
0             Ali;1998;15;6000
1           Zeynep;2000;2;4000
2            Ilgýn;2001;1;3000
3           Ýlkan ;2001;2;6000

'''





#VERİye hızlı bakıs

import seaborn as sns

df= sns.load_dataset("titanic")    #titanikteki insanların haayatta kalıp kalmadıkları db
print(df.head())
print(df.tail)
print(df.shape)
print(df.info)   #891 rows 15 columns
print(df.columns)
print(df.index)
print("özet: ",df.describe().T)  #özet alıyoruz
'''
özet:            count       mean        std   min      25%      50%   75%       max
survived         891.0   0.383838   0.486592  0.00   0.0000   0.0000   1.0    1.0000
pclass           891.0   2.308642   0.836071  1.00   2.0000   3.0000   3.0    3.0000
age              714.0  29.699118  14.526497  0.42  20.1250  28.0000  38.0   80.0000
sibsp            891.0   0.523008   1.102743  0.00   0.0000   0.0000   1.0    8.0000
parch            891.0   0.381594   0.806057  0.00   0.0000   0.0000   0.0    6.0000
fare             891.0  32.204208  49.693429  0.00   7.9104  14.4542  31.0  512.3292
'''

print("eksik deger var mi: ", df.isnull().values.any())   #TRUE       isnull tru fals dondurur. values= deger döndürdü VE NUMPY ARRAYINE CEVİRDİ. any ifadesi varsa true yazdrcak demek ki eksk var.  
print("eksiklik:", df.isnull().sum())  #truleri 1 falseleri 0 olarak toplar  sonucta: her bir de4giskende kac tane eksik deger var
'''
eksiklik: 
survived         0
pclass           0
sex              0
age            177       #177 tane true yani isnull? yess 177 tane bos deger
sibsp            0
parch            0
fare             0
embarked         2
class            0
who              0
adult_male       0
deck           688
embark_town      2
alive            0
alone            0

'''
#dframeden degiseken secmek istrsek df[" ?? "]
print(df["sex"].value_counts())   
'''sex
male      577
female    314'''


#PANDASTA SECİM İSLEMLERİ

df.index 
print(df[0:13])  #0dan 13e kadr gitti
print(df.drop(0,axis=0).head(10))   #0. index satırdkni (KALICI OLARAK SİLEMEDİK)sildik. yanlamasına sildik 0. degeri
delete_indexes=[1,2,3,4]  #KALICI OLARAK SİLMEK İCİN İNPLACE=TRUE
#print(df.drop(delete_indexes,axis=0, inplace=True))
print(df.drop(delete_indexes,axis=0).head(10))    #ANLIK SİLMEK İCİN

#insexle degiskenin yerini degistirelm
df["age"].head()  #YA DA    df.age.head()

df.index=df["age"]
df.drop("age",axis=1).head()  #sutunlardan silecez artık ageyi
'''
YANİ İLK BAŞTA: 
ındex   age    name
0       25     John
1       30     Jane
2       35     Doe
3       40     Alice
4       45     Bob            İDİ

INDEXLE DEGİSKEN DEGİSİNCE:
      name
age      
25    John
30    Jane
35    Doe
40    Alice
45    Bob                     OLDU. artık 0,1,2,3,4 indexleri yok// yaslara göre indexleniyor:D
'''

#indexi nasıl degisken olarak atarız
#1.yol
df.drop("age",axis=1, inplace=True)  #index artık age idi. onu tamamen sildik tekrar index olana ageyi nasıl degisken yapacagız:
print(df.head())  #age yok(sadece indexde var)

df.index
df["age"]= df.index   #tekrar aynı adı verdik= index diyerek indexe eştledik.
print("ageli", df.head())  #age var(index+degiskende var)


#2. yol
'''df.reset_index().head()   #indexde yer alan degskeni siler sonra yeni bir sutunda bir degisken olarak tanımlar
df= df.reset_index()
df.head()

naptık: degiskenlerde olan bir degeri indexe, daha sonrasında da degiskene gönderdk.

'''



#SUTUN INDEXLERİNDE: DEGİSKENLER UZDRİNDE İŞLEMLER.

pd.set_option("display.max_columns", None)
df= sns.load_dataset("titanic")
print(df)

print("age" in df)   #TRUE BU DEGİSKEN BU DATABASEDE VAR MI
df["age"].head() #degisken secme

print(type(df["age"].head()))  #type pandas.core.series.Series
print(type(df[["age"]].head())) #type pandas.core.frame.DataFrame

df[["age","alive"]]    #birden fazla degisken secmek icin

col_names= ["age", "adult_male", "alive"]
print(df[col_names])



#DF'E degisken eklemek
df["age2"] = df["age"]**2
print(df.head())
df["age3"]=df["age2"]/df["age"]
print(df.head())

#degisken silmek
df.drop("age3", axis=1, inplace= True)
print(df.head())


#birden fazla silmek istersek

df.drop(col_names, axis=1, inplace=True)
print(df.head())


#belirli özellikteki degiskeni silmek
a=df.loc[:, df.columns.str.contains("age")].head()   #içerisinde yaş ifadesi barındıranlrı getir dedik
print(a)

a=df.loc[:, ~df.columns.str.contains("age")].head()   #içerisinde yaş ifadesi haric diger her sutunu getirir ~ ile   alt gr+ü
print(a)





#iloc ve loc yapıları seçim için kullanılır   iloc: integer base: ..'e kadar   loc:label base seleciton:  ..de dahil

print(df.iloc[0:3]) #3e kadar
print(df.iloc[0,0])  #0. sutun 0.satır elemanı seç  : 0

print(df.loc[0:3]) #3.index de dahil

print(df.iloc[0:3,0:3])     #buarada string kullanamzsn int base   3satır 3 sutun
print(df.loc[0:3,"age2"])   #burada string kullanbilirz            3 satır age sutunu

col_names=["age2", "embarked", "sex"]
print(df.loc[0:3, col_names])   #ilk 3 satırdan istedigin kolonları seçip getir.





#KOŞULLU SEÇİM
pd.set_option("display.max_columns", None)
df=sns.load_dataset("titanic")
print("titanic: ", df.head())

print("kosul1: ", df[df["age"]>50].head())   #veristesinde yaşı 50den buyuk olanlar
"""
BURADA LOCA GEREK YO CUNKU TUM DB GELDİ
kosul1:     
        survived  pclass     sex   age  sibsp  parch     fare    embarked   class  \
6          0       1    male      54.0      0     0    51.8625        S      First        
11         1       1  female      58.0      0     0    26.5500        S      First        
15         1       2  female      55.0      0     0    16.0000        S      Second        
33         0       2    male      66.0      0     0    10.5000        S      Second        
54         0       1    male      65.0      0     1    61.9792        C      First        

      who  adult_male deck  embark_town alive  alone
6     man        True    E  Southampton    no   True
11  woman       False    C  Southampton   yes   True
15  woman       False  NaN  Southampton   yes   True
33    man        True  NaN  Southampton    no   True
54    man        True    B    Cherbourg    no  False
64

"""

print(df[df["age"]>50]["age"].count())  #kaç kişi var:   64


print("loclu: ",df.loc[df["age"]>50,["class"]].head())  #loc getirdik cunku bir degisken sectik.
"""
loclu:  cunku class degiskenini secmek isiyoruz. ondan loc.

6      First
11     First
15    Second
33    Second
54     FirsT
"""


print("loclu: ",df.loc[df["age"]>50,["class","age"]].head())  #2 dene degiken
"""
      class   age
6    First  54.0
11   First  58.0
15  Second  55.0
33  Second  66.0
54   First  65.0
"""



#EĞER 1DEN FAZLA KOŞUL GİRMEK İSTERSEN (KOŞUL) & (KOŞUL) YAPMAN GEREK
print(df.loc [(df["age"]>50)&(df["sex"]=="male"),["class","age"]].head()) #2 dene degiken



#İLK BAŞTA EMBARKIN GRUPLARI
print(df["embark_town"].value_counts())
"""embark_town
Southampton    644
Cherbourg      168
Queenstown      77
"""
df_new = df.loc [(df["age"]>50)
                &(df["sex"]=="male")
                &((df["embark_town"]=="Cherbourg")|(df["embark_town"]=="Southampton")),
                ["class","age","embark_town"]] 

#FİLRTLRELER GELİNCE EMBARKIN GRUPLARI
print(df_new["embark_town"].value_counts())
"""embark_town
Southampton    35
Cherbourg       9
"""