#sözlk comp.

dictionary={"a":1,
            "b":2,
            "c":3,
            "d":4}

dictionary.keys()
dictionary.values()
dictionary.items()  #tuple formda cagırmak için 

#amaç her bir valuenin karesini almak

#lst compre [] ile baslıyordu, dic'inki ise {} ile
t={k: v**2 for (k,v) in dictionary.items()}
print(t)
{k.upper(): v**2 for (k,v) in dictionary.items()}



#MÜLAKAT SORUSU: çift sayıların karesini bir sözlüğe ekle
numbers= range(3,10)
newDict = {}

for n in numbers:
    if n%2==0:
        newDict[n] =n**2

print(newDict)

#OR
numbers = range(3, 10)
aa = {k: k**2 for k in numbers if k % 2 == 0}
print(aa)


