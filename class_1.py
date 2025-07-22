x = int(input("Enter your distance(km) : "))
price = 0

if x >= 5 and x <= 50 :
    print("The price is 10 Bath")
    price = 10
elif x >= 51 and x <= 100 :
    print("The price is 15 Bath")
    price = 15
elif x >= 101 and x <= 300 :
    print("The price is 25 Bath")
    price = 25
elif x >= 301 and x <= 500 :
    print("The price is 35 Bath")
    price = 35
elif x >= 500 :
    print("The price is 45 Bath")
    price = 45
else :
    print("FREE")

vat = price*7/100
result = price + vat
print(vat)
print(result)

