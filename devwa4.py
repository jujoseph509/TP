import random

alfabe = ["a", "b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w""x","y","z","0","1","2","3","4","5","6","7","8","9" ]


def aleyatwa(fwa):
    if fwa >=1 and fwa <=36:
        random.shuffle(alfabe)
        text = alfabe[0:fwa]
        print('-'.join(text))
    else:print("Erreur, antre yon nonb ant 1 rive 36")


aleyatwa(4)

    