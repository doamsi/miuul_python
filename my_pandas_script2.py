#TOPLULAŞTIRMA VE GRUPLAMA

import pandas as pd 
import seaborn as sns
pd.set_option("display.max_columns",None)
df= sns.load_dataset("titanic")
df.head()

#group by ile: count(),first(),last(),mean(),median(),min(),max(),std(),var(),sum(),pivot table

#(cinsiyete) göre [yaş ortalamsı]
#1. yol
a=df.groupby("sex")["age"].mean()
print(a)
'''sex
female    27.915709
male      30.726645'''
#2. yol
a= df.groupby("sex").agg({"age": "mean"}) 
print(a)  #aynı sey




a= df.groupby("sex").agg({"age": ["mean","sum"]})     #sexe göre agein meani ve sumu
print(a)  
"""
          mean       sum
sex
female  27.915709   7286.00
male    30.726645  13919.17
"""




a= df.groupby("sex").agg({"age": ["mean","sum"],
                          "survived": "mean"}) 
print(a)  
"""
              age            survived
             mean       sum      mean
sex
female  27.915709   7286.00  0.742038
male    30.726645  13919.17  0.188908
"""




a= df.groupby(["sex","embark_town"]).agg({"age": ["mean","sum"],
                          "survived": "mean"}) 
print(a)  
"""
                               age         survived
                         mean       sum      mean
sex    embark_town
female Cherbourg    28.344262   1729.00    0.876712
       Queenstown   24.291667    291.50    0.750000
       Southampton  27.771505   5165.50    0.689655
male   Cherbourg    32.998841   2276.92    0.305263
       Queenstown   30.937500    495.00    0.073171
       Southampton  30.291440  11147.25    0.174603
"""



a= df.groupby(["sex","embark_town","class"]).agg({"age": ["mean","sum"],
                          "survived": "mean"}) 
print(a)
"""
                                 age         survived
                             mean      sum      mean
sex    embark_town class
female Cherbourg   First   36.052632  1370.00  0.976744
                   Second  19.142857   134.00  1.000000
                   Third   14.062500   225.00  0.652174
       Queenstown  First   33.000000    33.00  1.000000
                   Second  30.000000    30.00  1.000000
                   Third   22.850000   228.50  0.727273
       Southampton First   32.704545  1439.00  0.958333
                   Second  29.719697  1961.50  0.910448
                   Third   23.223684  1765.00  0.375000
male   Cherbourg   First   40.111111  1444.00  0.404762
                   Second  25.937500   207.50  0.200000
                   Third   25.016800   625.42  0.232558
       Queenstown  First   44.000000    44.00  0.000000
                   Second  57.000000    57.00  0.000000
                   Third   28.142857   394.00  0.076923
       Southampton First   41.897188  2681.42  0.354430
                   Second  30.875889  2778.83  0.154639
                   Third   26.574766  5687.00  0.128302

"""


a= df.groupby(["sex","embark_town","class"]).agg({"age": ["mean","sum"],
                          "survived": "mean",
                          "sex":"count"}) 
print(a)

"""
                                 age           survived   sex
                                mean      sum      mean count
sex    embark_town class
female Cherbourg   First   36.052632  1370.00  0.976744    43
                   Second  19.142857   134.00  1.000000     7
                   Third   14.062500   225.00  0.652174    23
       Queenstown  First   33.000000    33.00  1.000000     1
                   Second  30.000000    30.00  1.000000     2
                   Third   22.850000   228.50  0.727273    33
       Southampton First   32.704545  1439.00  0.958333    48
                   Second  29.719697  1961.50  0.910448    67
                   Third   23.223684  1765.00  0.375000    88
male   Cherbourg   First   40.111111  1444.00  0.404762    42
                   Second  25.937500   207.50  0.200000    10
                   Third   25.016800   625.42  0.232558    43
       Queenstown  First   44.000000    44.00  0.000000     1
                   Second  57.000000    57.00  0.000000     1
                   Third   28.142857   394.00  0.076923    39
       Southampton First   41.897188  2681.42  0.354430    79
                   Second  30.875889  2778.83  0.154639    97
                   Third   26.574766  5687.00  0.128302   265
"""






#PIVOT TABLE veri setini kırılım açısından degerlendirir.

a=df.pivot_table("survived","sex","embarked")  #kesşimde neyi görmek istersin, indexde(satırda) hangi degisken, sutunda hangi degisken 
print(a)  #,aggfunc= default deger ortalamadır.
"""
embarked      C         Q         S
sex
female    0.876712  0.750000  0.689655
male      0.305263  0.073171  0.174603
"""

a=df.pivot_table("survived","sex","embarked",aggfunc="std")  #kesşimde neyi görmek istersin, indexde(satırda) hangi degisken, sutunda hangi degisken 
print(a)






a=df.pivot_table("survived","sex",["embarked","class"])       #sex degeri embarked ve class olark gruopbylandı ve deger olarak survivod ortalaması alındı.
print(a)
'''

embarked              C                       Q                                 S  
class      First    Second Third     First  Second   Third        First      Second    Third
sex
female    0.976744   1.0  0.652174   1.      1.0    0.727273     0.958333   0.910448  0.375000
male      0.404762   0.2  0.232558   0.0     0.0    0.076923     0.35443    0.154639  0.128302
 
'''



#KATOGORİZE 

df["new_age"]= pd.cut(df["age"], [0,10,18,25,40,90])                    #saysal degiskeni katogorize degiskene cevirmek. Elindeki degiskeni biliyorsan(yas: cocuk 1-10 yas) cut..... bilmiyorsan qcut?
#yaşsal olarak böldük katogorize ettik

a=df.pivot_table("survived", "sex", "new_age")
print(a)
"""
new_age   (0, 10]  (10, 18]  (18, 25]  (25, 40]  (40, 90]              #yas gruplarına ve cinsiyetlerine göre survived yuzdesi
sex
female   0.612903  0.729730  0.759259  0.802198  0.770833
male     0.575758  0.131579  0.120370  0.220930  0.176471

"""



a=df.pivot_table("survived", "sex", ["new_age","class"])
print(a)
"""
new_age                      (25, 40]                      (40, 90]            \  
class      Second     Third     First    Second     Third     First    Second    Third 
sex
female   0.933333  0.500000  1.000000  0.906250  0.464286  0.961538  0.846154    0.111111
male     0.047619  0.115385  0.513514  0.071429  0.172043  0.280000  0.095238    0.064516
"""

pd.set_option("display.width",500)    #yanyana gelsn cıktılar diye




#Apply ve lambda: ihityacalrdan hareketle
#apply: satır ve sutunlarda otomatik olarak fonx uygular
#lambda bir fonx tanımalama şeklidir.


#FOR İLE AGE İCEREN TUM SUTUNLARI10A BOLERİZ
df=sns.load_dataset("titanic")

df["age2"]=df["age"]*2
df["age3"]=df["age"]*5
print(df)

for col in df.columns:
    if "age" in col:
        df[col]= df[col]/10    

#LAMBDA İLE NASIL YAPARIZ
        
df[["age","age2","age3"]].apply(lambda x: x/10).head()
df.loc[:, df.columns.str.contains("age")].apply(lambda x: x/10).head()  #ageyi yakala



def standart_scale(col_name):
    return (col_name+col_name.mean())/col_name.std()

df.loc[:, df.columns.str.contains("age")]=df.loc[:, df.columns.str.contains("age")].apply(standart_scale).head()  #apply içine fonx yazdık

print(df)



#BİRLEŞTİRME

import numpy as np 

m=np.random.randint(1,30,size=(5,3))
df1=pd.DataFrame(m, columns=["var11","var2", "var3"])  #Dataframe 0dan database olusturmaya yarar    var: degisken isimleri

df2=df1+99                    

print(df1)


a=pd.concat([df1,df2], ignore_index=True)  #LİSTE İÇERSİNDE OLUSTURDUGUMUZ 2 DBSİ DE BİRLEŞTİRİR.
print(a) #ikisin de indexleri 0123401234 olms birininkini yok edek 240 içinde





#merge ile birleştirme

df1 = pd.DataFrame({"employees": ["ılgın", "ilkan"],
                    "group": ["management", "engineering"]})

df2 = pd.DataFrame({"employees": ["ılgın", "ilkan"],
                    "start_date": ["2023", "2021"]})

a = pd.merge(df1, df2, on="employees")
print(a)


"""
   employees    group        start_date
0     ılgın     management        2023
1     ilkan     engineering       2021
"""



















 