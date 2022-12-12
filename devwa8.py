mo_pou_dekripte= "0-25-25"
dekriptaj=lambda mo_pou_dekripte: "".join([chr(int(elt)+97) for elt in mo_pou_dekripte.split("-")])
print(dekriptaj(mo_pou_dekripte))
