import random

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uzunluk = int (input("şifreniz kaç karakterden oluşsun"))
sifre = ""

for i in range(uzunluk):
    sifre = random.choice(karakterler) + sifre
print(sifre)
if else:
    print("sadece sayi kullaniniz")



