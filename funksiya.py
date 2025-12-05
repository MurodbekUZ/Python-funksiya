# def yosh_hisoblash(t_yil):
#     natija = 2025 - t_yil
#     if natija <= 5:
#         return f"Siz juda yosh ekansiz, yoshingiz: {natija} yosh."
#     return f"Sizning yoshingiz: {natija} yosh."
# t_yil = int(input("Tug'ilgan yilingizni kiriting: "))
# print(yosh_hisoblash(t_yil))


# # Vazifa 1: Ikki sondan kattasini qaytaruvchi funksiya.
# def katta_son(a, b):
#     if a > b:
#         return f"Bu katta son {a}"
#     else:
#         return f"Bu katta son {b}"
#
#
# a = int(input("Birinchi sonni kiriting: "))
# b = int(input("Ikkinchi sonni kiriting: "))
#
# natija = katta_son(a, b)
# print(natija)

# # Vazifa 2: Matnni teskari qilib qaytaruvchi funksiya.
# def teskari_matn(matn):
#     return matn[::-1]

# matn = input("Matnni kiriting: ")
# natija = teskari_matn(matn)
# print(f"Teskari qilingan matn: {natija}")

# #  Vazifa 3: Matnning har bir so'zini katta harf bilan boshlaydigan funksiya.
# def katta_harf_boshla(matn):
#     return matn.title()

# matn = input("Matnni kiriting: ")
# natija = katta_harf_boshla(matn)
# print(f"Har bir so'z katta harf bilan: {natija}")

# # Vazifa 4: Matnning palindrom ekanligini tekshiruvchi funksiya.
# def palindrom_tekshir(matn):
#     tozalangan_matn = matn.replace(" ", "").lower()
#     if tozalangan_matn == tozalangan_matn[::-1]:
#        return f"'{matn}' palindrom!"
#     else:
#         return f"'{matn}' palindrom emas."

# matn = input("Matnni kiriting: ")
# natija = palindrom_tekshir(matn)
# print(natija)