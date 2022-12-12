import random

alfabe = ["a", "b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w""x","y","z"]


def aleyatwa(fwa):
    if fwa >=1 and fwa <=26:
        random.shuffle(alfabe)
        text = alfabe[0:fwa]
        print(''.join(text))
    else:print("Erreur, antre yon nonb ant 1 rive 26")


aleyatwa(4)

    