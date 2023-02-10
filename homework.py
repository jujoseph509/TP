import re

text = "Je mange du #pain, de la #banane, et des #oeufs #"
result= re.sub("#\w+", lambda x : "<a href="">{}</a>".format(x), text)
print(result)


