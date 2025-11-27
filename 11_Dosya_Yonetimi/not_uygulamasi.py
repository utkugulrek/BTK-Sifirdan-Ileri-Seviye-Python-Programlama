def ortalama_hesapla(satir):
    satir = satir.strip()
    isim_kisim, not_kisim = satir.split(":")
    notlar = [int(n.strip()) for n in not_kisim.split(",")]
    ortalama = sum(notlar) / len(notlar)
    harf = harf_notu(ortalama)
    return isim_kisim, notlar, ortalama, harf

def harf_notu(ortalama):
    if ortalama >= 90:
        return "AA"
    elif ortalama >= 85:
        return "BA"
    elif ortalama >= 80:
        return "BB"
    elif ortalama >= 75:
        return "CB"
    elif ortalama >= 70:
        return "CC"
    elif ortalama >= 65:
        return "DC"
    elif ortalama >= 60:
        return "DD"
    else:
        return "FF"
    
def ortalamalari_oku():
    print(f"{'İsim':<20} | {'Notlar':<25} | {'Ortalama':<10} | {'Harf Notu':<8}")
    print("-"*75)

    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        for satir in file:
            isim, notlar, ort, harf = ortalama_hesapla(satir)
            print(f"{isim:<20} | {str(notlar):<25} | {ort:<10.2f} | {harf:<8}")

def not_gir():
    ad = input("Öğrenci Adı: ")
    soyad = input("Öğrenci Soyadı: ")
    not1 = int(input("Not1: "))
    not2 = int(input("Not2: "))
    not3 = int(input("Not3: "))

    with open("sinav_notlari.txt","a",encoding="utf-8") as file:
        file.write(f"{ad} {soyad}: {not1}, {not2}, {not3}\n")

def not_kaydet():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        with open("sonuclar.txt", "w", encoding="utf-8") as file2:
            for i in file:
                isim, notlar, ort, harf = ortalama_hesapla(i)
                satir = f"{isim:<20} | {str(notlar):<25} | {ort:<10.2f} | {harf:<8}\n"
                file2.write(satir)

while True:
    islem = int(input("" \
    "1- Notları Oku\n" \
    "2- Not Gir\n" \
    "3- Notları Kaydet\n" \
    "4- Çıkış\n"))
    
    match(islem):
        case 1:
            ortalamalari_oku()
        case 2:
            not_gir()
        case 3:
            not_kaydet()
        case 4:
            break
