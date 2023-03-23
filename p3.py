d={'Nepal':'Kathmandu','Italy':'Rome','England':'London' }
a=str(input("Enter what you want: "))
items = d.items()  
for key, value in items:  
    if value == a: 
        print(key)
