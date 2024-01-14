#IF
 
if 1==1:
    print("something")




def numberCheck(number):
    if number==10:
        print("number is 10")

numberCheck(20)
numberCheck(10)



#ELSE-ELİF

def numberCheck(number):
    if number==10:
        print("number is 10")
    elif number>10:
        print("number is greater than 10")
    else:
        print("number is less 10")


numberCheck(20)