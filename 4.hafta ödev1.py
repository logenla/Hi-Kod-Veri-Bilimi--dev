#1-
x=3
x=float(x)
print(type(x)),print(x)

y=4.5
y=int(y)
print(type(y)) , print(y)

z="8"
z=int(z)
print(type(z),z)

a="12"
a=float(a)
print(type(a),a)

b=46.8
b=int(b)
print(type(b),b)

#2

ali_yas=24
ayse_yas=20
veli_yas=22
print(ali_yas<veli_yas)
print(veli_yas>ayse_yas)
print(ayse_yas==veli_yas)

#3
x=input(print("Lütfen ilk sayıyı giriniz: "))
y=input(print("Lütfen ikinci degeri giriniz: "))
x=float(x)
y=float(y)
islem_toplama=x+y
print(islem_toplama)
islem_cıkarma=x-y
print(islem_cıkarma)
islem_carpma=x*y
print(islem_carpma)
islem_bolme=x/y
print(islem_bolme)

#4
isim=input(print("Lutfen isminizi giriniz:"))
yas=input(print("Lutfen yasinizi giriniz: "))
sehir=input(print("Lütfen sehrinizi giriniz:  "))
meslek=input(print("Lütfen mesleginizi giriniz: "))
print(isim,yas,sehir,meslek)

#5
variable="Hi-Kod Veri Bilimi Atölyesi"
print(variable.split())
print(variable.upper())
print(variable.lower())

sayılar="0123456789"
print(sayılar[0:9:2])
print(sayılar[1:10:2])