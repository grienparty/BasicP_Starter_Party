# x = int(input("Enter your grade : "))

# if x > 50 :
#     print("You're Passed")
#     if x >= 80 :
#         print("your grade is A")
#     elif x >= 70 :
#         print("your grade is B")
#     elif x >= 60 :
#         print("your grade is C")
#     else :
#         print("your grade is D")
# else :
#     print("FAILED")



user_type = input("Enter your type : ")
price = int(input("Enter total price : "))
date = int(input("Enter date of order : "))

print("your user type is", user_type)
print("price of order is", price)

if user_type == "gold" :
    if price >= 1000 :
        print("you'll get discount 15%")
    else :
        print("you'll get discount 10%")

elif user_type == "silver" :
    if price >= 1000 :
        print("you'll get discount 10%")
    else :
        print("you'll get discount 5%")
else :
    print("sorry there is no discount for you")

#โปรพิเศษ วันที่เลขคี่
if date%2 == 1 :
    print("")