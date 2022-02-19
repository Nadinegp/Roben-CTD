n=int(input("Enter array size: "))
bag = []
if n<5:
    print("Array size can't be less than 5 ")
    exit()
else:
    for i in range (0,n):
        o=int(input("Add number to the list"))
        bag.append(o)
    print(bag)
    ans=(input("do you want to remove an element?"))
    if(ans== "yes" or ans== "Yes"):
        num=int(input("Enter number you want to remove: "))
        bag.remove(num)
        if n>5:
            print(bag)
            print("Thankssssss :3")
        else:
            print("array size is less than 5!")
    else:
        print("Thankssssss :3")