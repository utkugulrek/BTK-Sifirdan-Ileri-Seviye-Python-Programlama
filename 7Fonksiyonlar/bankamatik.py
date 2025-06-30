# Bankamatik Uygulaması

UtkuHesap = {
    "ad": "Utku G",
    "hesapNo": "123456",
    "bakiye": 3000,
    "ekHesap": 2000
}

MertHesap = {
    "ad": "Mert D",
    "hesapNo": "654321",
    "bakiye": 2000,
    "ekHesap": 1000
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap["bakiye"] >= miktar):
        hesap["bakiye"] -= miktar
        print("Paranızı alabilirsiniz.")
    else:
        toplam = hesap["bakiye"] + hesap["ekHesap"]

        if (toplam >= miktar):
            ekHesapKullanimi = input("Ek Hesap kullanılsın mı?(e/h)")

            if ekHesapKullanimi == "e":
                ekHesapKullanilacakMiktar = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap["ekHesap"] -= ekHesapKullanilacakMiktar
                print("Paranızı alabilirsiniz.")
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap["hesapNo"]}'lu hesabınızda {hesap["bakiye"]} bulunmaktadır.")
        else:
            print("Üzgünüz bakiye yetersiz.")
            bakiyeSorgula(hesap)

def bakiyeSorgula(hesap):
    print(f"{hesap["hesapNo"]} nolu hesabınızda {hesap["bakiye"]} TL bulunmaktadır. Ek limitiniz ise {hesap["ekHesap"]} TL bulunmaktadır.")

paraCek(UtkuHesap, 3000)
print("****************")
paraCek(UtkuHesap, 2000)
