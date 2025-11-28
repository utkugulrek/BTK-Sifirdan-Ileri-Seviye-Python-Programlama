def islem(islem_adi):
    def topla(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam

    def carpma(*args):
        carpim = 1
        for i in args:
            carpim *= i
        return carpim

    match islem_adi:
        case "topla":
            return topla
        case "carpma":
            return carpma
        case _:
            raise ValueError("Yanlış işlem girdiniz.")


toplama = islem("topla")
print(f"Toplam: {toplama(1, 2, 3, 4, 6, 7, 9, 10)}")

carpma = islem("carpma")
print(f"Çarpım: {carpma(1,4,8)}")

yanlis = islem("123123")
print(yanlis)
