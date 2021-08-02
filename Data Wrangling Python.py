#membaca file dengan menggunakan pandas
import pandas as pd
csv_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/shopping_data.csv")
print(csv_data)
print(csv_data.head()) #Membaca file dengan menggunakan head()
print(csv_data['Age']) #Melakukan akses data kolom
print(csv_data.iloc[5]) #Melakukan akses data melalui baris, index dimulai dari 0
print(csv_data['Age'].iloc[1]) #Menampilkan suatu data dari baris dan kolom tertentu
print("Cuplikan Dataset :")
print(csv_data.head())
print("Menampilkan data ke 5 sampai kurang dari 10 dalam satu baris:")
print(csv_data.iloc[5:10]) #Menampilkan data dalam range tertentu
print(csv_data.describe(include='all'))
print(csv_data.describe(exclude=['O'])) #Menampilkan informasi statistik dengan Numpy. mengabaikan element string(hanya numerik)


#Handling Missing Value
#Pada suatu dataset, ada kalanya data yang kita akan kita kelola tidak lengkap.
# Hal ini tentunya akan menyulitkan atau membuat hasil analisa tidak akurat.
# Penanggulangan akan data yang hilang ini biasa disebut Handling Missing Value.
# Penanganan dari nilai yang kosong ini banyak caranya.
# Sebagai seorang data science yang berhubungan dengan data yang real,
# solusi pertama yang benar-benar kita anjurkan untuk kasus seperti ini adalah melakukan trace kembali ke sumber data atau memerika ulang record.
# Terutama jika data itu berasal dari human record.
# Sangat disarankan untuk menelusuri kembali agar tidak terjadi kesalahan ketika sudah mencapai titik analisa.
# Selain solusi untuk melakukan penelusuran kembali ke sumberdata, pada ilmu data science juga ada beberapa metode yang bisa dijadikan solusi untuk menangani kasus ini.
csv_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/shopping_data_missingvalue.csv")
print(csv_data.isnull().values.any()) #melakukan pengecekan nilai null, jika TRUE, maka ada null
    #mengisi dengan mean <- jika sedikit outlier/noisy/anomaly
print(csv_data.mean()) #menampilkan mean (rata-rata tiap kolom)
print('Dataset yg masih terdapat nilai kosong :!')
print(csv_data.head(10))
csv_data = csv_data.fillna(csv_data.mean())
print('Dataset yang sudah diproses handling missing value dengan mean!')
print(csv_data.head(10))
    #mengisi dengan median <- median merupakan nilai tengah, dimana bukan hasil perhitungan yg melibatkan nilai outlier
    #terdapat outlier yg bisa mempengaruhi distribusi kelas dan mengganggu analisa pada klasterisasi (clustering).
csv_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/shopping_data_missingvalue.csv")
print(csv_data.isnull().values.any())
print(csv_data.median())
print("Dataset yg masih terdapat missing value:")
print(csv_data.head(10))
csv_data=csv_data.fillna(csv_data.median())
print("Dataset yg sudah diproses Handling Missing Value dengan median:")
print(csv_data.head(10))


#Praktek Normalisasi menggunakan Scikit Learn
import pandas as pd
import numpy as np
from sklearn import preprocessing

csv_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/shopping_data.csv")
array = csv_data.values
X = array[:,2:5] #memisahkan fitur dari dataset.
Y = array[:,0:1]  #memisahkan class dari dataset

dataset=pd.DataFrame({'Customer ID':array[:,0],
                      'Gender':array[:,1],
                      'Age':array[:,2],
                      'Income':array[:,3],
                      'Spending Score':array[:,4]})
print("dataset sebelum dinormalisasi :")
print(dataset.head(10))

min_max_scaler = preprocessing.MinMaxScaler(feature_range=(0,1)) #inisialisasi normalisasi MinMax
data = min_max_scaler.fit_transform(X) #transformasi MinMax untuk fitur
dataset = pd.DataFrame({'Age':data[:,0],
                        'Income':data[:,1],
                        'Spending Score':data[:,2],
                        'Customer ID':array[:,0],
                        'Gender':array[:,1]})

print("dataset setelah dinormalisasi :")
print(dataset.head(10))