# -*- coding: utf-8 -*-
"""BelajarPython3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ycn2Gen4ou4hdQHUwBNy8anFC_DxyPuj

# Belajar Python 3
"""

# mau nyetak sesuatu pake print
print("Hello World!")

# mencetak baris baru
print("Hello")
print("World!")

# agar tidak mencetak garis baru
print("Hello",end=" ")
print("World!")

# variabel atau menyimpan nilai
a = 1
print(a)

a = 2
print(a)

# string adalah teks smentra 1 adalah angka
# 0,1,2,3,4,... , 9 Integer
# 1,3,4,0,9,0,34,3,14 float/ decimal
# a,b,c,d, aku , kamu, dia, string

# Cetak dengan Berita Baru
print("Hello")
print("World!")

 # Cetak tanpa Baris Baru
print("Hello", end=" ")
print("World!")

# Variabel
a = 1
print(a)

a = 2
print(a)

a = "Aku"
print(a)

# Math Operation
# + - * / %

# penjumlahan
print(1 + 1)

# pengurangan
print(1 - 1)

# perkalian
print(1 * 3)

# pembagian
print(10 / 5)
print(10 // 5)
print(9 / 2)
print(9 // 2)

# sisa hasil bagi / Modulus / Mod
print(9 % 2)

# Perulangan / Loop
for i in range(11): #range hanya akan mencetak smapai angka sebelumnya
  print(i)

for i in range(1,11):
  print(i)

# SALAH!!!
# for i in range(1) {
#    print(i):
# }


# Conditional
if (1 + 1) == 2:
  print("Benar")
else:
  print("Salah")

if (1 + 3) == 2:
  print("Hmm")
else:
  print("Wowo")


# Boolean
if (1 + 1) == 2 and (1 + 2) == 3 and False: #true
  print("Yes benar")
else:
  print("Hmm, coba lagi")

if False or False:
  print("Thfjiejns")
else:
  print("Rrhnnnndrhh")

# jika sama sma benar maka and dijalankan
# and adlah pembanding 2 keadaan


# Fungsi
def printHello(nama):
  print(nama)

printHello("Hello World")

def pHello(nama):
  print("Hello {}".format(nama))

pHello("Affan")
pHello("Tifan")
pHello("Nadia")

