#13010011040-BEYZA NUR ORUC
import random
class oyunIcerik()
    def __init__(self,satir,sutun):

        self.gemi = []
        self.oyunAlani = []
        self.satir = satır
        self.sutun = sutun
        self.atishakki = int((satir * sutun) / 3)
        self.atis = 0

        if (satir < 10 or sutun < 10):
            print("-" * 20)
            print("Oyun alanı 10*10 boyutlarından kucuk olamaz ! )
            print("-" * 20)
            return



    def atesEt(self,satir,sutun):

        if (satir > len(self.oyunAlani) or sutun > len(self.oyunAlani[0])):
            print("-" * 20)
            print("Lütfen oyun alanı içine atış yapınız !")
            print("-" * 20)
            return

        if (self.oyunAlani[satır][sutun].atis()):
            print("*" * 20)
            print("Tebrikler Vurdunuz ! ")
            print("*" * 20)
            self.atis += 1
        else:
            print("-" * 20)
            print("Ne Yazık ki Vuramadınız !")
            print("-" * 20)
            self.atishakki -= 1

        for i in range(len(self.gemi)):
            if(self.gemi[i][0]):
                continue

            else:
                for j in range(1,len(self.gemi[i])):
                    satir = self.gemi[i][j][0]
                    sutun = self.gemi[i][j][1]
                    if(j==len(self.gemi[i])-1):
                        print("*" * 20)
                        print("Amiral Battı !")
                        print("*" * 20)
                        self.gemi[i][0] = True
                    return

    def sonDurum(self):

        print("*"*20)
        print("İsabetli atış:",self.atis,"Atış Hakkınız:",self.atishakki)
        print("*"*20)



    def oyunSonucu(self):

        if(self.atishakki ==0):
            print("*" * 20)
            print("Üzgünüm Kaybettiniz..")
            print("*" * 20)
            return False

        elif(self.atishakki == 10):
            print("*" * 20)
            print("TEBRİKLER ! KAZANDINIZZZ! Puanınız:",self.atishakki)
            print("*" * 20)
            return False

        else:
            return True

    def gemiYerlesimi(self,boyut)
        self.gemi = gemi[boyut]

        while (True):
            yatay = random.randint(0, self.satir)
            dikey = random.randint(0, self.sutun)


class kareler():

    def __init__(self):
        self.acilmayankare= "?"


    def atis(self):
        self.isabetlikare= "X"
            return True
        else:
            self.isabetsizkare= "*"
            return False

while (True):

    satir = int(input("Lütfen satır sayısı giriniz"))

    sutun = int(input("Lütfen sütun sayısı giriniz"))

    alan = oyunIcerik(satir,sutun)


    gemiYerlesimi(1)
    gemiYerlesimi(2)
    gemiYerlesimi(3)
    gemiYerlesimi(4)

    secim1 = input("<1> için Açık Mod,<2> için Gizli Mod")

    if (secim1.lower() == "1"):
        continue
    elif (secim1.lower() == "2"):
        break

    while (True):

        if (alan.oyunSonucu()):
            alan.sonDurum()
            atesx = int(input("Hangi satira ateş etmek istersiniz?"))
            atesy = int(input("Hangi sütuna ateş etmek istersiniz?"))
            alan.atesEt(atesx - 1, atesy - 1)
        else:
            print("*" * 20)
            print("\nOYUN SONA ERDİ")
            print("*" * 20)
            break

    secim2 = input("Tekrar oynamak için <R> , Çıkış yapmak için <E> tuşunu kullanın.")
    if (secim2.lower() == "R"):
        continue
    elif (secim2.lower() == "E"):
        break









