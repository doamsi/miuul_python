#for: listenin elamanlrına erişmek için

students=["Jon", "Mark", "Vanessa","Mariam"]
for student in students:  #kimi nerede gezdircen
    print(student) 


for student in students:  #kimi nerede gezdircen
    print(student.upper()) 





salaries= [100,200,2300,600,2000]
for salary in salaries:
    print(salary*20/100 + salary)



#DONGU İCİNDE FONX!!

salaries= [100,200,2300,600,2000]
def new_salary(salari,rate):
    return salari*rate/100 + salari
for i in salaries:            
    print(new_salary(i, 10))     #forda i olarak kullandın o zaman fonxda da salari degil i. cunku dısarıya uygulanmış şekli bu.




salaries= [100,200,2300,600,2100]
for o in salaries:
    if o>2000:
        print(new_salary(o,10))    #eğer maas 2000den fazlaysa maasa yuzde10 zam
    else:
        print(new_salary(o,8))     #degilse yuzde8 zam



#ÖRNEKLER GIRILEN STRİNG İFADELERİN ÇİFT İNDEXLERİNDEKİNİ BUYULT. BIR MULAKAT SORUSU
        
def alternating(string):
    new_string= ""
    for index in range(len(string)):
        if index%2==0:
            new_string += string[index].upper()
        else:
            new_string += string[index].lower()
    print(new_string)

alternating("naber nasılın teşekkürler")  #NaBeR NaSıLıN TeŞeKkÜrLeR
#enumerate ile:



def altern(string):
    stringing=""
    for index, letter in enumerate(string):
        if index%2==0:
            stringing+=letter.upper()
        else:
            stringing+=letter.lower()
    print(stringing)
altern("naber canımın içi")
    









#BREAK- CONTINUE- WHILE

salaries=[1000,2000,3000,4000,6000]
for i in salaries:
    if i ==3000:
        break
    print(i)          #sadece 1000 ve 2000 yazılır


for i in salaries:
    if i ==3000:
        continue   
    print(i)          #1000 2000 4000 5000 yazılır 3000 yok CALISMA BREAK!!


number=1
while number<5:
    print(number)
    number+=1
  


#enumarte indeksi çift olana bir işlem tek olana bir işlem 
students=["A", "B", "C","D"]

a=[]
b=[]
for index, student in enumerate(students):   #İŞİN İÇİNE İNDEXLE İLGİLİ BİR SORUN GELİNCE ENUMERATE KULLAN
    if index%2==0:
        a.append(student)
    else:
        b.append(student)
    print(a,b)






students=["A", "B", "C","D"]
def divideStudents(stud):
    groups=[[],[]]               #enumerate(studeents,1) demek index numarası 1 ile başlasın demek.
    for index, student in enumerate(students):   #İŞİN İÇİNE İNDEXLE İLGİLİ BİR SORUN GELİNCE ENUMERATE KULLAN
        if index%2==0:
            groups[0].append(student)
        else:
            groups[1].append(student)
        
    return groups
    
st= divideStudents(students)
print(st)

print(st[0])





#ZİP birbirinden farklı listelerle ilgilenir match eder birleştirir tuple formda

stude=["ılgın", "ilkan"]
ages=(10,30)
y=list(zip(stude,ages))
print(y)






#LAMBDA, MAP, FİLTER, REDUCE

'''
Lambda kullan at fonxdur.
'''
new_sum= lambda a,b: a+b
new_sum(4,5)


"""
map: dongu gibi
"""
salaries=[1000,2000,3000,4000]
def news_alary(x):
    return x*120/100

list(map(news_alary,salaries))  #map(fonksion,gezineblecegi bir liste)
#OR 
list(map(lambda x:x*120/100, salaries))


#filter
listes=[1003,2000,3009,4000]
list(filter(lambda x: x%2==0, listes))

#reduce indirgeyici
from functools import reduce
listes=[1,2,3,4]
reduce(lambda a,b: a+b, listes)



