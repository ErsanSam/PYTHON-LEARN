print("Hello World");
print("Saya Ersan, Baru belajar PYTHON");

#perintah pada baris ini tidak mempengaruhi program
'''
perintah init tidak akan dieksekusi oleh Python
dan perintah ini juga tidak akan dieksekusi
perintah ini juga tidak akan dieksekusi
'''
print("jadi # digunakan untuk membuat comment pada Python")

#Tipe Data
print(int(5.3)) #Numerik
print(float(3))
print(bool(1)) #boolean
print(bool(0))
print(str(5.3))
print(str([1,'kamu'])) #Sequence
print(list('buku'))
print(list({1,3,6,3}))
print(tuple('buku'))
print(tuple({1,3,6,3}))
print(set("buku")) #Set, setiap elemen bernilai unik

text = "Belajar Python di DQLab."
print(list(text))
print(tuple(text))
print(set(text))

import math
import numpy as np
import pandas as pd
import seaborn as sns