oyuncular = {"bjk": ["rafa", "cengiz", "salin"],
          "gs"   : ["osimhen", "sane", "icardi"],
          "fener"    : ["talisca", "fred", "asensio"]}
print(oyuncular["bjk"])
print(oyuncular["gs"])
print(oyuncular["fener"])
for takim in oyuncular:
    print(takim)
#    print(oyuncular[i])
    #print(i,"takımının oyuncuları : ",oyuncular[i])
    for oyuncu in oyuncular[takim]:
        print("\t",oyuncu)