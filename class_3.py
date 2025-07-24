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

mons_hp = 100
gun_damage = 30
knife_damage = 20
pan_damage = 50

manu = int(input("Enter your choice 1(fight) 2(run) : "))

if manu == 1 :
    round_attack = int(input("Enter number of round attack : "))
    for i in range(round_attack) :
        print(f"GUN => damage {gun_damage}")
        print(f"KNIFE => damage {knife_damage}")
        print(f"PAN => damage {pan_damage}")

    weapon = input("which weapon you want : ")

    if weapon == "GUN" :
        mons_hp = mons_hp - gun_damage
    elif weapon == "KNIFE" :
        mons_hp = mons_hp - knife_damage
    elif weapon == "PAN" :
        mons_hp = mons_hp - pan_damage

    print(f"monster_hp = {mons_hp}")

    if mons_hp == 0 :
        break

    if mons_hp < 0 :
        print("monster_hp = 20")

    if mons_hp == 0 :
        print("WIN !")

    else :
        print("you lose !")

else :
    print("loser lol")
