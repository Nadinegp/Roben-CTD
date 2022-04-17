import random
global bag1,bag2,bag3,bag
bag1=10
bag2=10
bag3=10
bag=[bag1 , bag2 , bag3]

print (bag)

def isEmpty(userBag):
    if(bag[userBag] == 0):
        return True
    else:
        return False
        
def tooMuch(userBag,userObj):
    x = bag[userBag]-userObj 
    if(x < 0):
        return True
    else:
        return False 
         
def validateObj(noObj):
    if(noObj<=5 and noObj>=0):
        return noObj
    else:
        noObj=int(input("Pick number of objects "))
        return noObj

def validateBag(userBag):
    try:
        if(userBag>2 or userBag<-1):
            userBag=int(input("Enter a valid number: "))
    except Exception:
        print("Incorrect input")
        userBag=int(input("Number of bag: "))
        validateBag(userBag)
    return userBag     
    
while True:
    print("User's turn: ")
    try:
        userBag=int(input("Number of bag: "))
    except Exception:
        print("Enter a valid input: ")
        userBag=int(input("Number of bag: "))
    userBag-=1
    userBag = validateBag(userBag) #chose index
    while(isEmpty(userBag)==True):
        userBag=int(input("Bag is empty, pick another bag: "))
        userBag = validateBag(userBag)
        userBag-=1
    try:
        userObj=int(input("Pick number of objects "))   
    except Exception:
        userObj=int(input(" **Enter a valid input** "))
    userObj = validateObj(userObj)
    while(tooMuch(userBag,userObj) == True):
        print(" **Not enough objects in the bag** ")
        try:
            userObj=int(input("Pick number of objects "))
        except Exception:
            print("Enter a valid input: ")
            userObj=int(input("Enter a valid input: "))
        userObj = validateObj(userObj)
    bag[userBag] = bag[userBag] - userObj
    print("list ",bag)
    if bag[0]==0 and bag[1]==0 and bag[2]==0:
        print("User wins")
        break
    else: 
        print("-------------------------------------------")
        print("Computer's turn")
        compBag=random.randint(0, 2)
        while(isEmpty(compBag) == True):
            compBag = random.randint(0, 2)
        compObj=random.randint(1, 5)
        while(tooMuch(compBag,compObj)==True):
            compObj=random.randint(1, 5)
        bag[compBag]-=compObj
        print(bag)
        if bag[0]==0 and bag[1]==0 and bag[2]==0:
            print("Computer wins")
            break
        
