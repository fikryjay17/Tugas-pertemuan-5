class Klub :
    def intro (self):
        print("Banyak liga besar top Eropa")

    def Jenis(self):
        print("Beberapa Liga seperti Inggris, Spanyol, Italia, Prancis")

class MU(Klub):
    def Jenis(self):
        print("MU Termasuk klub liga Inggris")

class Real_Madrid(Klub):
    def Jenis(self):
        print("Real Madrid Termasuk klub liga Spanyol")

class Juventus(Klub):
    def Jenis(self):
        print("Juventus Termasuk klub liga Italia")

class PSG(Klub):
    def Jenis(self):
        print("PSG Termasuk klub liga prancis")

obj_klub = Klub()
obj_mu = MU()
obj_real_madrid= Real_Madrid()
obj_juventus = Juventus()
obj_psg = PSG()

print("--------------------------------------------------------------------------")
obj_klub.intro()
obj_klub.Jenis()
print("--------------------------------------------------------------------------")

obj_mu.intro()
obj_mu.Jenis()
print("--------------------------------------------------------------------------")

obj_real_madrid.intro()
obj_real_madrid.Jenis()
print("--------------------------------------------------------------------------")

obj_juventus.intro()
obj_juventus.Jenis()
print("--------------------------------------------------------------------------")

obj_psg.intro()
obj_psg.Jenis()
print("--------------------------------------------------------------------------")