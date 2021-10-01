class domba:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def bersuara(self):
        print("mbeee")

class katak:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def bersuara(self):
        print("krok..krok..")

domba1 = domba("domba", 3)
katak1 = katak("katak", 5)

for hewan in (domba1, katak1): 
    hewan.bersuara()

