#1
kullanıcı_adı=input(print("lütfen kullanıcı adınızı giriniz: "))
sifre=input(print("lütfen sifrenizi giriniz: "))
if len(sifre)<=6:
    print("lütfen en az 6 haneli sifre olusturun!!!")
else:
    print("hesabınız oluşturuldu")

###################################
#
while True:
    sifre = input(print("lütfen sifrenizi giriniz: "))
    if 5 < len(sifre) < 10:
        print("sifreniz oluşturuldu")
        break
    else:
        print("sifreniz en az 5 en fazla 10 hane olsun")

################
#4kullanıcı=input("kullanıcı adınızı giriniz: ")
sifre=input(str("sifrenizi giriniz: "))
kayıtlı_sifre="ismail"
hata_sayisi=0
while hata_sayisi<3:
    if sifre==kayıtlı_sifre:
        print("giriş yapıldı")
        break
    else:
        print("sifreniz yanlis girildi.Tekrar deneyin")
        sifre=input("sifre: ")
        hata_sayisi +=1
        if hata_sayisi==3:
            print("deneme hakkınız kalmadı")