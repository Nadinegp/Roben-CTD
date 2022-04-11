import random
bag1=10
bag2=10
bag3=10

print(bag1,"- ",bag2," -",bag3 )

def check(compobj):
    if(bag1<compobj):
        compobj=random.randint(1, bag1)
    elif(bag2<compobj):
        compobj=random.randint(1, bag2)
    elif(bag3<compobj):
        compobj=random.randint(1, bag3)
    
        return compobj;

def userobj():
    try:
            userobj=int(input("number of obj u want to remove: "))
            if(userobj>5 or userobj<0):
                userobj=int(input("enter a valid number: "))
    except ValueError:
        print("incorrect input")
        userobj=int(input("number of bag: "))
    return userobj
        
def userbag():
    print("User's turn: ")
    try:
        if(userbag>3 or userbag<0):
            userbag=int(input("enter a valid number: "))
    except ValueError:
        print("incorrect input")
        userbag=int(input("number of bag: "))
    return userbag;
 
while True:
    userbag=int(input("number of bag: "))
    userBag = userbag()
    userObj = userobj()
    if(userBag==1):
        bag1=bag1-userObj
    elif(userBag==2):
        bag2=bag2-userObj
    elif(userBag==3):
        bag3=bag3-userObj
    print(bag1,"- ",bag2," -",bag3)
    if bag1==0 and bag2==0 and bag3==0:
        print("user wins")
        break
    else: 
        print("-------------------------------------------")
        print("Computer's turn")
        compbag=random.randint(1, 3)
        compobj=random.randint(1, 5)
        check(compobj)
        try:
            if(compbag==1 and bag1!=0):
                bag1=bag1-compobj
            elif(compbag==2 and bag2!=0):
                bag2=bag2-compobj
            elif(compbag==3 and bag3!=0):
                bag3=bag3-compobj
            print(bag1,"- ",bag2," -",bag3 )
        except:
            print("bag is empty")
        if bag1==0 and bag2==0 and bag3==0:
            print("computer wins")
            break
                
                    
            
                                
            
    