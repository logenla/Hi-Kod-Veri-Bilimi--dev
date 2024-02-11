#%% md
### Ödev 1
#Bir sözlük oluşturulur ve bu sözlükte öğrencilerin isimleri ve Matematik, Fizik, Kimya notları tutulur.
#Kullanıcıdan isim ve ders ismi(Matematik, Fizik, Kimya) istenir ve bu bilgilere göre çıktı verilir.

ogrenciler={"Ali":{"matematik":80,
                 "fizik":70,
                 "kimya":90},
            "Merve":{"matematik":90,
                   "fizik":85,
                   "kimya":80
            },
            "Enes":{"matematik":75,
                  "fizik":70,
                  "kimya":50},
            "Aslı":{"matematik":70,
                  "fizik":65,
                  "kimya":75}}
print(ogrenciler["Ali"]["matematik"])




#%% md
### Ödev 2
#Sözlük üzerinde değerleri değiştirme, yeni değer ekleme, kullanıcıya ulaşmak istediği bilgileri sorma gibi uygulamalar yapın.
#%%
#yeni değer ekleme
ogrenciler["Irem"]={"matematik":85,
                    "fizik":75,
                    "kimya":80}
#degeri değiştirme
ogrenciler["Merve"]["matematik"]=ogrenciler["Merve"]["matematik"]+5
print(ogrenciler["Merve"])

#bilgilere ulaşma
x=input("Hangi ogrencinin bilgisini ulaşmak istiyorsunuz: ")
if x in ogrenciler:
    print(ogrenciler[x])
else:
    print("Ögrenci bilgisi bulunamadı")
