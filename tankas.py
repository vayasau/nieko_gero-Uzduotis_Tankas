from random import randint


class Tankas:
    def __init__(self, kryptis, koordinates, suviai):
        self.kryptis = kryptis
        self.koordinates = koordinates
        self.suviai = suviai
        self.visi_suviai = {"Siaure" : 0, "Rytai" : 0, "Pietus" : 0, "Vakarai" : 0}
        self.kryptys = ["Siaure", "Rytai", "Pietus", "Vakarai"]
        self.t_koordinates = [randint(1, 10), randint(1, 10)]
        # self.t_koordinates = [5,3]
        self.taskai = 100
        
    def info(self):
        print(f"""        Tanko kryptis: {self.kryptis}
        koordinates: {self.koordinates}
        suviu i Siaure: {self.visi_suviai["Siaure"]}
        suviu i Rytus: {self.visi_suviai["Rytai"]}
        suviu i Pietus: {self.visi_suviai["Pietus"]}
        suviu i Vakarus {self.visi_suviai["Vakarai"]}
        is viso suviu: {self.suviai}
        taikinys yra {self.t_koordinates}
        tasku: {self.taskai}""")

    def pirmyn(self):
        if self.kryptis == "Siaure":
            self.koordinates[1] += 1
        elif self.kryptis == "Pietus":
            self.koordinates[1] -= 1
        elif self.kryptis == "Vakarai":
            self.koordinates[0] -= 1
        elif self.kryptis == "Rytai":
            self.koordinates[0] += 1
        self.taskai -= 10
        tankas.info()
       
    def atgal(self):
        if self.kryptis == "Siaure":
            self.koordinates[1] -= 1
        elif self.kryptis == "Pietus":
            self.koordinates[1] += 1
        elif self.kryptis == "Vakarai":
            self.koordinates[0] += 1
        elif self.kryptis == "Rytai":
            self.koordinates[0] -= 1
        self.kryptis = self.kryptys[self.kryptys.index(self.kryptis)-2]
        self.taskai -= 10
        tankas.info()
 
    def kairen(self):
        if self.kryptis == "Siaure":
            self.koordinates[0] -= 1
        elif self.kryptis == "Pietus":
            self.koordinates[0] += 1
        elif self.kryptis == "Vakarai":
            self.koordinates[1] -= 1
        elif self.kryptis == "Rytai":
            self.koordinates[1] += 1
        self.kryptis = self.kryptys[self.kryptys.index(self.kryptis)-1]
        self.taskai -= 10
        tankas.info()

    def desinen(self):
        if self.kryptis == "Siaure":
            self.koordinates[0] += 1
        elif self.kryptis == "Pietus":
            self.koordinates[0] -= 1
        elif self.kryptis == "Vakarai":
            self.koordinates[1] += 1
        elif self.kryptis == "Rytai":
            self.koordinates[1] -= 1
 
        if self.kryptis == "Vakarai":
            self.kryptis = self.kryptys[0]
        else:
            self.kryptis = self.kryptys[self.kryptys.index(self.kryptis)+1]
        self.taskai -= 10
        tankas.info()
           
    def suvis(self):
        self.visi_suviai[self.kryptis] = self.visi_suviai[self.kryptis]+1
        if (
            self.koordinates[0] == self.t_koordinates[0] and self.koordinates[1] > self.t_koordinates[1] and self.kryptis == "Pietus" or
            self.koordinates[0] == self.t_koordinates[0] and self.koordinates[1] < self.t_koordinates[1] and self.kryptis == "Siaure" or
            self.koordinates[1] == self.t_koordinates[1] and self.koordinates[0] < self.t_koordinates[0] and self.kryptis == "Rytai" or
            self.koordinates[1] == self.t_koordinates[1] and self.koordinates[0] > self.t_koordinates[0] and self.kryptis == "Vakarai"
        ):
            print("==== Pataikymas ====")
            self.taskai += 100
            self.t_koordinates = [randint(1, 10), randint(1, 10)]
 
        self.suviai = sum(self.visi_suviai.values())
        tankas.info()

def tasku_top():
    vardas = input("Vardas: ")
    with open("high_scores.txt", "a") as failas:
        failas.write(f"{vardas} {tankas.taskai}")

with open("high_scores.txt", "w") as failas:
    failas.write("High scores\n")

tankas = Tankas("Siaure", [5,5], 0)
tankas.info()

while True:
    pasirinkimas = int(input("8 - Pirmyn, \n2 - Atgal, \n4 - Kairen, \n6 - Desinen, \n5 - Suvis, \n1 - Info, \n0 - išeiti iš programos\n"))
    if pasirinkimas == 8:
        tankas.pirmyn()
    if pasirinkimas == 2:
        tankas.atgal()
    if pasirinkimas == 4:
        tankas.kairen()
    if pasirinkimas == 6:
        tankas.desinen()
    if pasirinkimas == 5:
        tankas.suvis()  
    if pasirinkimas == 1:
        tankas.info()
    if pasirinkimas == 0:
        tasku_top()
        print("Iki")
        break