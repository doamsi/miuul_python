#fonx okur yazarlıgı
'''
Parametre fonx tanımlanırken ifade edilen değişkenlerdir.
Argümanlar ise fonxlar cagrıldıgında parametre degerlerine karsılık girilen değerlerdir.

'''


#mesela print fonxunda kullanılabilen argumanlar
print("a","b", sep="__")  #__ ile a ve b i seperate et. >> a_b



#fonx tanımlama:

def calculate(x):   #def+isim+(parametre)
    print(x*2)      #body kısmı

calculate(5) #10


def summer(arg1, arg2):   #2 parametreli/argumanlı fonx
    print(arg1+arg2)

summer(7,8)   #we call the fonx
summer(arg2=7, arg1=8)   



#fonx statement

def say_hi():
    print("Merhaba")
    print("Hello")
    print("Hi")

say_hi()


def say_hi(string): 
    print(string)
    print("Hello")
    print("Hi")

say_hi("miuul")  #miuul hello hi




def multipl(a,b):
    c=a*b
    print(c)

multipl(10,9)



#girilen degelerleri bir liste içinde saklayacak fonx

list_store=[]

def add_element():
    a=int(input("sayi: "))
    b=int(input("sayi: "))

    c=a*b 
    list_store.append(c)     #c local etki alanda
    print(list_store)        #list store global 

add_element()

#-------------------------------------------------

liste_store=[]

def add_elemente(a,b):

    c=a*b 
    liste_store.append(c)
    print(liste_store)

add_elemente(3,6)
add_elemente(18,3)
add_elemente(6,8)



def divide(a,b=3):
    print(a/b)

divide(6,2) #3
divide(6) #2




'''
Tekrar eden işlemlerde (dont repeat urself)

'''


def calculate(varm, moisture, charge):
    print((varm + moisture )/ charge)

calculate(98,12,78)




#ne zaman return?
'''
Fonxların cıktılarını girdi olarak kullabilmek için return kullanıllır

'''
def calculate(varm, moisture, charge):
    return((varm + moisture )/ charge)  #return goruldukten sonra returnden sonraki kod calısmaz

calculate(98,12,78)*10   #normalde return olmasa fonx*int olamaz!!
a=calculate(90,80,70)



def calculate(varm, moisture, charge):
    varm=10*varm
    moisture=10*moisture
    charge=4*charge
    output= ((varm + moisture )/ charge)
    return varm, moisture, charge, output   #tuple

calculate(98,36,2)  #cvp tuple
varm, moisture, charge, output = calculate(50,12,5) 









#FONX İÇİNDEN FONX CAGIRMA

def calculate(varm, moisture, charge):
    return((varm + moisture )/ charge)

def standardization(b,p):
    return b*10*p**2

def all_calculate(varm,moisture,charge,p):
    a=calculate(varm, moisture,charge)   #return fonxu olduugndan cıktısını kaydedebildik. Ara (Not ana) fonxu cagırdık
    c=standardization(a,p)   # Ana fonxun icine ara fonxu koyduk (a=.. argumanını). standartizyon fonxunda b,p argumanları vardı ama biz sadece p'i almak istedik. Ama diger ilk(b) argumanı a'dan geliyor. bir üstteki koddan elde ettigimiz deger yani
    print(c*10)   #a'yı cagırdık sonra c'e koyduk ve sonra da işlemi yaptık

all_calculate(1,3,5,6) #>>2880



#Aynısı deneme --------------------------------------------------------------------------------


def calculate(varm, moisture, charge):
    return((varm + moisture )/ charge)

def standardization(b,p):
    return b*10*p**2

def all_calculate(varm,moisture,charge,b,p):
    print(calculate(varm, moisture,charge) )  
    c=standardization(b,p)
    print(c*10)
all_calculate(1,3,5,3,2) #>>2880






#LOCAL GLOBAL DEGİSKENLER

list=[1,2]

def add_element(a,b):
    c=a*b            #c, local etki alanında olan bir degisken. globalde göremeyiz
    list_store.append(c)
    print(list_store)

add_element(1,9)