maas=int(input(print("lutfen maasını giriniz: ")))
print(maas)
if maas<=10000:
    kesinti=maas*5/100
    new_maas=maas-kesinti
    print("yeni maasiniz: ",new_maas)

elif maas<=25000:
    kesinti_1=maas*10/100
    new_maas_1=maas-kesinti_1
    print("yeni maasiniz:",new_maas_1)

elif maas<=4500:
    kesinti_2=maas*25/100
    new_maas_2=maas-kesinti_2
    print("yeni maasiniz: ",new_maas_2)

else:
    kesinti_3=maas*30/100
    new_maas_3=maas-kesinti_3
    print("yeni maasiniz: ", new_maas_3)