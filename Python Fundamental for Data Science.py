print(10*2+5)
print("Academy DQLab")

#comment
print (10*2+5) #fungsi matematika
print("Academy DQLab") #fungsi mencetak kalimat

#Printing data type
var_string = "Belajar Python DQLAB"
var_int=10
var_float=3.14
var_list=[1,2,3,4]
var_tuple=("satu","dua","tiga")
var_dict={"nama":"Ali","umur":20}

print(var_string)
print(var_int)
print(var_float)
print(var_list)
print(var_tuple)
print(var_dict)

print(type(var_string))
print(type(var_int))
print(type(var_float))
print(type(var_list))
print(type(var_tuple))
print(type(var_dict))

#If statement
i = 7 #inisialisasi variable i yang memiliki nilai 10

if(i==10): #pengecekan nilai i apakah sama dengan 10
	print("ini adalah angka 10") #jika TRUE maka akan mencetak kalimat ini

#IF ELSE
i = 5 #inisialisasi variable i yang memiliki nilai 10

if(i==10): #pengecekan nilai i apakah sama dengan 10
	print("ini adalah angka 10") #jika TRUE maka akan mencetak kalimat ini
else:
    print("bukan angka 10") #jika FALSE akan mencetak kalimat ini

#IF … ELIF … ELSE ….
i=3

if(i==5):
     print("ini adalah angka 5")
elif(i>5):
     print("lebih besar dari 5")
else:
     print("lebih kecil dari 5")

#NESTED IF
i=2
if(i<7):
	print("nilai i kurang dari 7")
	if(i<3):
		print("nilai i kurang dari 7 dan kurang dari 3")
	else:
		print("nilai i kurang dari 7 tapi lebih dari 3")

#Praktek operasi matematika
a=10
b=5
selisih = a-b
jumlah = a+b
kali = a*b
bagi = a/b
print("Hasil penjumlahan a dan b adalah",jumlah)
print("Selisih a dan b adalah :", selisih)
print("Hasil perkalian a dan b adalah :",kali)
print("Hasil pembagian a dan b adalah :",bagi)
#Operator modulus
c=10
d=3
modulus = c%d
print("Hasil modulus",modulus)
angka=5
if(angka%2 ==0):
    print("angka termasuk bilangan genap")
else:
    print("angka termasuk bilangan ganjil")

#Perulangan
#while
j=0 #nilai awal j =0
while j<6: #ketika j kurang dari 6 lakukan perulangan, jika tidak stop perulangan
	print("Ini adalah perulangan ke - ",j) #lakukan perintah ini ketika perulangan
	j=j+1 #setiap kali diakhir perulangan update nilai dengan ditambah 1.

#for
for i in range (1,6): #perulangan for sebagai inisialisasi dari angka 1 hingga angka yg lebih kecil daripada 6
	print("Ini adalah perulangan ke -",i) #perintah jika looping akan tetap berjalan
#for with access element
for i in range (1,11):
    if(i%2==0):
        print("Angka genap",i)
    else:
         print("Angka ganjil",i)

#fungsi
def salam(): #membuat fungsi
    print("Hello, Selamat Pagi")
salam() #pemanggilan fungsi
#fungsi sendiri
def luas_segitiga(alas,tinggi): #alas dan tinggi merupakan parameter yang masuk
	luas = (alas * tinggi)/2
	print("Luas segitiga: %f" %luas)
#pemanggilan fungsi
luas_segitiga(4,6)
#Return value
def luas_segitiga(alas, tinggi): #alas dan tinggi merupakan parameter yang masuk
    luas = (alas * tinggi) / 2
    return luas
# Pemanggilan fungsi
##4 dan 6 merupakan parameter yang diinputkan kedalam fungsi luas segitiga
print("Luas segitiga: %d" % luas_segitiga(4, 6))


#modul dan package
import math
print("Nilai pi adalah:", math.pi) #math.pi merupakan sintak untuk memanggil fungsi
#rename
import math as m
print("Nilai pi ADALAH:",m.pi)
#import sebagian fungsi
from math import pi
print("Nilai pi Adalah:",pi)
#import semua isi modul
from math import*
print("Nilai e adalah:",e)
#Membaca file teks CSV
import csv
# tentukan lokasi file, nama file, dan inisialisasi csv
f = open('penduduk_gender_head.csv', 'r')
reader = csv.reader(f)
# membaca baris per baris
for row in reader:
     print (row)
# menutup file csv
f.close()
#membaca file csv dengan menggunakan pandas
import pandas as pd
table = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv")
table.head()
print(table)
#BAR CHART
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
table = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv")
table.head()
x_label = table['NAMA KELURAHAN']
plt.bar(x=np.arange(len(x_label)),height=table['LAKI-LAKI WNI'])
plt.show()

#Parameter dalam Grafik (Memberikan Nilai Axis dari data CSV)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

table = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv")
table.head()
x_label = table['NAMA KELURAHAN']
plt.bar(x=np.arange(len(x_label)),height=table['LAKI-LAKI WNI'])
plt.xticks(np.arange(len(x_label)), table['NAMA KELURAHAN'], rotation=30)
plt.show()

#menambah title dan label
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


table = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv")
table.head()

x_label = table['NAMA KELURAHAN']
plt.bar(x=np.arange(len(x_label)),height=table['LAKI-LAKI WNI'])
plt.xticks(np.arange(len(x_label)), table['NAMA KELURAHAN'], rotation=90)
plt.xlabel('Keluarahan di Jakarta pusat')
plt.ylabel('Jumlah Penduduk Laki - Laki')
plt.title('Persebaran Jumlah Penduduk Laki- Laki di Jakarta Pusat')

plt.show()