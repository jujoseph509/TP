
non = "Jean-Baptiste Jean"
def fonksyon_non(non):
    non_separe=non.split(" ")
    non_separe_san_espas=[]
    inisyal_non=""
    for non in non_separe:
        non_separe_san_espas += non.split("-")
    for non in non_separe_san_espas:
        inisyal_non += non[0]

    print(inisyal_non)

fonksyon_non(non)
