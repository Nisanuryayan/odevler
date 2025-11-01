#Evcil hayvan takip sistemi
class Hayvanlar:
    def __init__(self,isim,tur,yas,sahip):
        self.isim=isim
        self.tur=tur
        self.yas=yas
        self.sahip=sahip
    
    def bilgileri_goster(self):
        print(f"Hayvan:{self.isim}-Tür:{self.tur}-Yaş:{self.yas}-Sahip:{self.sahip}")

class Barinak:
    def __init__(self):
       self.hayvanlar=[]
    def hayvan_ekle(self,hayvan):
        self.hayvanlar.append(hayvan)
        print(f"{hayvan.isim} barınağa eklendi.")
    def hayvanlari_listele(self):
        if not self.hayvanlar:
            print("Barınakta hayvan yok.")
        else:
            print("\n Barınaktaki Hayvanlar:")
            for hayvan in self.hayvanlar:
                hayvan.bilgileri_goster()
    def hayvan_sil(self,isim):
        for hayvan in self.hayvanlar:
            if hayvan.isim==isim:
                self.hayvanlar.remove(hayvan)
                print(f"{isim} barınaktan silindi.")
                return
        print(f"{isim} adlı hayvan bulunamadı")
    def hayvan_sayisi(self):
        toplam=len(self.hayvanlar)
        print(f"Barınakta toplam {toplam} hayvan var.")
    
barinak=Barinak()

while True:
    print("\n---BARİNAK MENÜSÜ---")
    print("1.Hayvan Ekle")
    print("2.Hayvanlari Listele")
    print("3.Hayvan Sil")
    print("4.Hayvan Sayisi")
    print("5.Çikiş")
    
    secim=input("Bir seçenek girin(1-5):")

    if secim=="1":
        isim=input("Hayvan ismi:")
        tur =input("Hayvanin türü (örnek:kedi,köpek):")
        yas=input("Hayvanin yaşi:")
        sahip=input("Sahibinin adi:")

        yeni_hayvan=Hayvanlar(isim,tur,yas,sahip)
        barinak.hayvan_ekle(yeni_hayvan)
    elif secim=="2":
        barinak.hayvanlari_listele()
    elif secim=="3":
        isim=input("Silmek istediğiniz hayvanin adi:")
        barinak.hayvan_sil(isim)
    elif secim=="4":
        barinak.hayvan_sayisi()
    elif secim=="5":
        print("Barinak sisteminden çikiş yapiliyor.. Görüşmek üzere!")
        break
    else:
        print("Geçersiz seçenek.Lütfen 1-5 arasinda bir sayi girin.")