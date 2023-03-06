text=input('Введение исходного текста -- ')
key=[]
hash=[]
# преобразование букв их текста в цифры благодаря
# таюлице ASCII и переводу в восмиричную СС в последствии.
for i in range(len(text)):
    j=text[i]
    bb=oct(ord(j))[2:]
    key.append(bb)
print()
for i in range(len(key)):
    j=key[i]
    dd= int(j)% len(text)
    hash.append(dd)
print(key,hash)