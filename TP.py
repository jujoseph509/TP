from random import randrange
nonb_odinate = randrange (0, 1000)
chans = 4

print("Byenvini nan jwet sa a, ki rele devineNonb  \n")
print("Wap gen pou ou chwazi yon nonb ki ant 0 rive nan 1000 \n")
print("Wap gen posibilite pou ou jwe pandan 5 fwa, sa a ka rive ou genyen depi nan premye fwa a. \n")
print("Ann komanse jwe \n")
nonb_chwazi = int(input("Antre nonb ou devine odinate a chwazi a \n "))
if nonb_chwazi == nonb_odinate:
    print("Bravo, ou genyen!")
while nonb_chwazi != nonb_odinate and chans > 0:
    if nonb_chwazi < nonb_odinate:
        print("Nonb odinate a pi gran ke nonb ou chwazi a \n" )
        nonb_chwazi=int(input("Antre yon lot nonb:  "))
    elif nonb_chwazi > nonb_odinate:
        print("Nonb odinate a pi piti ke nonb ou chwazi a. \n")
        nonb_chwazi=int(input("Antre yon lot nonb"))   
    else:
        print("Bravo, ou genyen! \n")
        print("Nonb odinatea se byen" ,nonb_odinate)   
        break
    chans-=1
if chans ==0:
    print("Dezole ou itilize tout chans ou yo, ou pap ka jwe anko \n")
    print("Nonb odinate a te chwazi a se" ,nonb_odinate, ".\n")
print("Mesi, paske ou te jwe. ")
