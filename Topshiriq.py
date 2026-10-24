"""  'Talaba' classini yaratish (ism, yosh)  """

# class Talaba:
#     def __init__(self, name, age, group="Backend"):
#         print("Yangi guruh yaratildi!")
#         self.name = name
#         self.age = age
#         self.group = group
#
# t = Talaba("Ali", 18)
# print(f"{t.group} guruhi!")
# print(f"Talaba ismi {t.name}")
# print(f"Yoshi {t.age} da")

""" **QO'SHIMCHA MASHQ (ixtiyoriy)** """
""" - Oson: «Talaba» classini yarating (ism, yosh) va 2 ta obyekt yasang. """

# class Talaba:
#     def __init__(self, name, age, group="Backend"):
#         print("Yangi guruh yaratildi!")
#         self.name = name
#         self.age = age
#         self.group = group
#
# t1 = Talaba("Ali", 18)
# t2 = Talaba("Vali", 15)
# t3 = Talaba("Asal", 20)
# talabalar =[t1, t2, t3]
# print(f"{talabalar[0].group} guruhi!")
#
# for t in talabalar:
#     print(f"Talaba ismi {t.name}")
#     print(f"Yoshi {t.age} da")
#     print("---")

"""- O'rta: «Kitob» classini yarating (nom, muallif, yil) va ma'lumotini chiqaring."""

class Asar:
    def __init__(self, name, author, year):
        self.name = name
        self.age = author
        self.group = year

t = Asar("Tushda kechgan umrlar", "Oʻtkir Hoshimov", 1993)
print(f"{t.name} asari")
print(f"Yozuvchi ismi {t.age}")
print(f"{t.group}-yilda yozilgan")
