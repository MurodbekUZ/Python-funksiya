# # Masala 1: Salomlashish funksiyasi
# ism = input("Ismingizni kiriting: ")
# def salomlash(ism):
#     print(f"Assalomu alaykum, {ism}!")
# salomlash(ism)

# # Masala 2: Katta sonni topish
# son1 = float(input("Birinchi sonni kiriting: "))
# son2 = float(input("Ikkinchi sonni kiriting: "))
# def katta_son(son1, son2):
#     if son1 > son2:
#         return son1
#     else:
#         return son2
# natija = katta_son(son1, son2)
# print(f"Katta son: {natija}")

# # Masala 3: Teskari matn
# matn = input("Matn kiriting: ")
# def teskari_matn(matn):
#     return matn[::-1]
# natija = teskari_matn(matn)
# print(f"Teskari matn: {natija}")

# # Masala 4: Ro'yxat yig'indisi
# def royxat_yigindisi(sonlar):
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son
#     return yigindi
# sonlar = [1, 2, 3, 4, 5]
# natija = royxat_yigindisi(sonlar)
# print(f"Ro'yxat yig'indisi: {natija}")

# # Masala 5: Katta harfga o'girish
# def katta_harf(matn):
#     return matn.title()
# matn = input("Matn kiriting: ")
# natija = katta_harf(matn)
# print(f"Katta harf: {natija}")

# # Masala 6: Tubmi yoki yo'qmi
# son = float(input("Son kiriting: "))
# def tubson(son):
#     if son <2:
#         return f"{son} - Bu son tub emas!"
#     for x in range(2, int(son ** 0.5) + 1):
#         if son % x == 0:
#             return f"{son} - Bu son tub emas!"
#     return f"{son} - Bu son tub!"
# print(tubson(son))

# # Masala 7: Takrorlanuvchi harflar
# def takrorlanuvchi_harflar(matn):
#     harf_soni = {}
#     for harf in matn:
#         if harf.isalpha():  # Faqat harflarni hisoblash
#             harf = harf.lower()
#             if harf in harf_soni:
#                 harf_soni[harf] += 1
#             else:
#                 harf_soni[harf] = 1
#     takrorlanuvchi = {harf: son for harf, son in harf_soni.items() if son > 1}
#     return takrorlanuvchi
# matn = input("Matn kiriting: ")
# natija = takrorlanuvchi_harflar(matn)
# print(f"Takrorlanuvchi harflar: {natija}")

# Masala 8: Palindrom tekshiruvi














