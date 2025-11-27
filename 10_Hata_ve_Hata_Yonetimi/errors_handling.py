# 1: Liste elemanları içindeki sayısal değerleri bulunuz.

liste = ["1", "2", "5a", "10b", "abc", "10", "50"]

# for x in liste:
#     try:
#         result = int(x)
#         print(result)
#     except ValueError:
#         continue

# 2: Kullanıcı "q" değerini girmedikçe aldığınız her inputun sayı
# olduğundan emin olunuz aksi halde hata mesajı yazınız.

# while True:
#     sayi = input("sayi: ")
#     if sayi == "q":
#         break

#     try:
#         result = int(sayi)
#         print("Girdiğiniz sayı: ",result)
#     except:
#         print("Geçersiz sayı girdiniz!")

# 3: Girilen parola içinde Türkçe karakter hatası veriniz.

# def check_password(parola):
#     turkce_karakterler = "çşğüöİıÜĞÇŞÖ"

#     for i in parola:
#         if i in turkce_karakterler:
#             raise TypeError("Parola, Türkçe karakter içeremez!")
#     print("Parola geçerlidir.")

# parola = input("Parola: ")

# try:
#     check_password(parola)
# except TypeError as err:
#     print(err)

# 4: Faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için
# hata mesajı oluşturunuz.

# def faktoriyel(x):
#     if not str(x).lstrip("-").isdigit():
#         raise ValueError("Tam sayı olmayan bir değer girdiniz.")

#     x = int(x)

#     if x < 0:
#         raise ValueError("Negatif değer girdiniz.")

#     result= 1

#     for i in range(1, x+1):
#         result*= i
#     return result

# for x in [5, 10, 20, "21a", -21, "21-"]:
#     try:
#         y = faktoriyel(x)
#     except ValueError as err:
#         print(err)
#         continue
#     print(y)
