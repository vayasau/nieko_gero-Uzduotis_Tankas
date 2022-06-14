class Tankas:
    def __init__(self, kryptis, koordinates, suviai):
        self.kryptis = kryptis
        self.koordinates = koordinates
        self.suviai = suviai
        self.visi_suviai = {"Siaure" : 0, "Rytai" : 0, "Pietus" : 0, "Vakarai" : 0}
        self.kryptys = ["Siaure", "Rytai", "Pietus", "Vakarai"]
        
    def info(self):
        print(f"""        Tanko kryptis: {self.kryptis}
        koordinates: {self.koordinates}
        suviu i Siaure: {self.visi_suviai["Siaure"]}
        suviu i Rytus: {self.visi_suviai["Rytai"]}
        suviu i Pietus: {self.visi_suviai["Pietus"]}
        suviu i Vakarus {self.visi_suviai["Vakarai"]}
        is viso suviu: {self.suviai}""")

    def pirmyn(self):
        self.koordinates[0] += 1
        tankas.info()
       
    def atgal(self):
        self.koordinates[0] -= 1
        self.kryptis = self.kryptys[self.kryptys.index(self.kryptis)-2]
        tankas.info()
 
    def kairen(self):
        self.koordinates[1] -= 1
        self.kryptis = self.kryptys[self.kryptys.index(self.kryptis)-1]
        tankas.info()

    def desinen(self):
        self.koordinates[1] += 1
        if self.kryptis == "Vakarai":
            self.kryptis = self.kryptys[0]
        else:
            self.kryptis = self.kryptys[self.kryptys.index(self.kryptis)+1]
        tankas.info()
    
       
    def suvis(self):
        if self.kryptis in self.visi_suviai:
            self.visi_suviai[self.kryptis] = self.visi_suviai[self.kryptis]+1
        # else:
        #     self.visi_suviai[self.kryptis] = 1 

        self.suviai = sum(self.visi_suviai.values())
        # print(self.visi_suviai)
        tankas.info()


tankas = Tankas("Siaure", [5,5], 0)
tankas.info()

while True:
    pasirinkimas = int(input("1 - Pirmyn, \n2 - Atgal, \n3 - Kairen, \n4 - Desinen, \n5 - Suvis, \n6 - Info, \n9 - išeiti iš programos\n"))
    if pasirinkimas == 1:
        tankas.pirmyn()
    if pasirinkimas == 2:
        tankas.atgal()
    if pasirinkimas == 3:
        tankas.kairen()
    if pasirinkimas == 4:
        tankas.desinen()
    if pasirinkimas == 5:
        tankas.suvis()  
    if pasirinkimas == 6:
        tankas.info()
    if pasirinkimas == 9:
        print("Viso gero")
        break