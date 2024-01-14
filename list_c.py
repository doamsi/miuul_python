#birden fazla satırdaki kodları tek satıra indirgemek
# []





salaries=[1000,2000,3000,4000,5000]

def news_alary(x):
    return x*120/100

null_list=[]
for salary in salaries:
    if salary>3000:
        null_list.append(news_alary(salary))
    else:
        null_list.append(news_alary(salary*2))

print(null_list)
#listcomp hali:
a=[news_alary(salary*2) if salary <3000 else news_alary(salary) for salary in salaries]
print("a=",a)
#TEK SATIRDA SONUCU LİSTE OLAN YUKARDAKİ KOD DİZİSİNİN TEK SATIRDA OLMASI


b=[salary*2 for salary in salaries if salary<3000]  #ne yap - hangi döngüde - if 
print(b)

c=[salary*2 if salary<3000 else salary*1  for salary in salaries]     #else varsa yerler degisir

