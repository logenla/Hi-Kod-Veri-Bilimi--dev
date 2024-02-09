#### Ödev 1
Kullanıcıdan pi değeri ve yarıçap bilgisi alarak dairenin alanını hesaplayan bir fonksiyon oluşturulur.
#%%
def dairenin_alanı(pi,yarıcap):
    alan=pi*yarıcap*yarıcap
    return alan
pi=float(input("pi degerini giriniz: "))
yarıcap=float(input("yarıcap degerini giriniz: "))

alan=pi*(yarıcap*yarıcap)
print("dairenin alanı: ",alan)
#%% md
#### Ödev 2

Faktöriyel adında fonksiyon oluşturulur. Döngü kullanarak parametre olarak girilen sayının faktöriyeli hesaplanır. Format metodunu kullanılarak ekrana yazdırılır.
#%%
sayı= int(input("lütfen bir sayi giriniz: "))
def faktoriyel_alma(sayı):
    faktoriyel=1
    for i in range(1,sayı+1):
        faktoriyel= faktoriyel*i
        sonuc=faktoriyel
        print(sonuc)
    return faktoriyel
faktoriyel_alma(sayı)
#%% md
#### Ödev 3
Kişinin fonksiyona doğum yılını vererek kaç yaşında olduğunu hesaplayan bir fonksiyon oluşturun. 
#%%
dogumyılı=int(input("dogum yılınızı giriniz: "))
def yashesaplama(dogumyılı):
    yas=2024-dogumyılı
    print("Yasınız: ",yas)
    return yas
yashesaplama(dogumyılı)
#%% md
#### Ödev 4

Doğum yılı ve isim bilgisi verilen fonksiyon kişinin emekli olup olmadığını söylesin.(Kişi 65 yaşında ise emekli olur.) Burada yaş hesabını yukarıdaki örnekteki fonksiyonu kullanarak yapsın.(Yani fonksiyon içinde fonksiyon kullanmanızı istiyorum :)) Kişi 65 yaşında ya da daha fazlaysa "Emekli oldunuz" yanıtını, 65 yaşından küçükse emekliliğine kaç yıl kaldığını da hesaplayarak "(isim) emekliliğine (yıl) kaldı." yanıtını versin.
#%%
ad=str(input("lütfen adınızı giriniz: "))
dogumyılı=int(input("lütfen dogum yılınızı giriniz: "))
def emeklilik_hesaplama(ad,dogumyılı):
    def yas_hesaplama(dogumyıl):
        yas=2024-dogumyıl
        print(yas)
        if yas<65:
            kalan_yıl=65-yas
            print(f"Sayın {ad} , emekliliğine kalan yıl {kalan_yıl}")
        else:
            print("Emekli oldunuz")
    return yas_hesaplama(dogumyılı)
emeklilik_hesaplama(ad,dogumyılı)
