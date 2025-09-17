year1=int(input("Enter first year: " ))
year2=int(input("Enter second year: " ))
if (year1<0 or year2<0):
    print("Invalid number")
elif year1>=year2:
    print("Invalid")
    
else:
    while year1<year2:
        year1=year1+1
        if( (year1 % 4 == 0) and (year1 % 100 != 0 or year1 % 400 == 0)):
            print(year1)
    

    
            
         