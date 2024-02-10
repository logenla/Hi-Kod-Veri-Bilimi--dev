### Ödev 1

liste = ["Python",True,9,"3",8.4,"Hi-Kod","False",4.7]

1. Aşağıdaki işlemleri indexing ve slicing kullanarak liste üzerinde uygulayın.

   - "3" değerine ulaşmak için indexleme yapın.
   - "Hi-Kod" değerine ulaşmak için indexleme yapın.
   - 4.7 değerine ulaşmak için indexleme yapın.
   - 9,"3",8.4,"Hi-Kod" değerlerine ulaşmak için slicing yapın.
   - 8.4,"Hi-Kod","False",4.7 değerlerine ulaşmak için slicing yapın.
#%%

#%% md
### Ödev 2

Verilen listede bulunan string veri tipindeki öğeleri yeni_liste isimli listeye eklenir.

liste = ["Python",True,9,"3",8.4,"Hi-Kod","False",4.7]
#%%
liste = ["Python", True, 9, "3", 8.4, "Hi-Kod", False, 4.7]
yeni_liste = []
for i in liste:
    if isinstance(i, str):
        yeni_liste.append(i)
print(yeni_liste)

#%% md
### Ödev 3

Enumerate methodunu araştırın ve aşağıdaki örneği enumerate methodu ile yapın.
meyveler = ['elma', 'armut', 'muz', 'çilek', 'ayva']
for index in range(len(meyveler)):
    print("{}. indexte bulunan meyve: {}".format(index,meyveler[index]))
#%%
meyveler = ['elma', 'armut', 'muz', 'çilek', 'ayva']
for index,değer in enumerate(meyveler):
    print(f"{index} indexde bulunan meyve{değer}")