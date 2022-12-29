#    PROJECT    15
#TO FIND WEATHER THE NUMBER IS PRIME OR COMPOSITE IN A GIVEN RANGE AND COUNT OF PRIME AND COMPOSITE NUMBERS

a=int(input("Enter starting number:"))         #for lowest value in range
b=int(input("Enter finishing number:"))        #for highest value in range
countC,countP=0,0                              #for counting prime and composite numbers seperately
if a<=b:
    for i in range(a,b+1):
        if i > 1:
            for j in range(2,i):
                if i%j == 0:
                    countC = countC+1
                    print(i,"is composite")
                    break
            else:
                countP= countP+1
                print(i,"is prime")
        elif i <= 0:
            print("Error!!!  Enter natural numbers only")
            break
        elif i == 1:
            print(i,"is neither prime nor composite")
    print("Count:",countP,"prime and",countC,"composite numbers in the range")
else:
    print("Error!!! Enter valid range .i.e, a<=b")