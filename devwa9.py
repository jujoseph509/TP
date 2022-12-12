vale1= 10
vale2= 20
def pemitasyon(vale1, vale2):
    temp  = vale1
    vale1 = vale2
    vale2 = temp
    return (vale1, vale2)

print(pemitasyon (vale1, vale2))

