#for

""""
    for <var> in range(<num>) :
"""

# num = int(input("Enter your number : "))
# for i in range(1, number + 1) :
#     print(i)

# num = int(input("Enter your number : "))
# sum = 0
# i = 1
# while i <= num :
#     sum = sum + 5
#     print(f"ครั้งที่ {i} ได้ผลเป็น", sum)
#     i = i + 1

# num = int(input("Enter your number : "))
# sum = 0

# i = 1
# while i < 5 :
#     print(f"ครั้งที่ {i}")
#     i = i + 1

mons = "ouan"
hp = 100
gun = 30
knife = 20
pan = 5

manu = int(input("Enter your choice 1(fight) 2(run) : "))
if manu == 1 :
    print("You have to fight!!")
    times = int(input("how many move you wanna fight : "))
    weapon = input("which weapon you want 1(gun) 2(knife) 3(pan) : ")
else :
    print("loser lol")
