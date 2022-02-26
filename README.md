# Tucil-Stima-2

Divide and conquer algorithm (convex hull problem)  
Rizky Ramadhana P. K.  
13520151

## Deskripsi Singkat

Salah satu permasalahan yang bisa diselesaikan dengan strategi divide and conquer adalah permasalahan pembentukan convex hull dari kumpulan titik pada sebuah bidang. Pada tugas ini akan dibuat implementasi dari algoritma tersebut dan akan dibandingkan dengan metode pencarian convex hull yang dimiliki library scipy. Poligon convex hull tersebut akan diterapkan pada kumpulan dataset milik library sklearn. Akan diambil dua atribut dan dibentuk convex hull  untuk masing-masing kelompok data dengan nilai target yang sama. Kumpulan data tersebut beserta convex hull nya akan disimpan dalam bentuk gambar. Gambar inilah yang akan dibandingkan antara algoritma yang dibuat sendiri dengan algoritma milik library scipy.

## Requirement Program

1. Install sklearn
2. Install numpy
3. Install pandas
4. Intall matplotlib
5. Install scipy

Kelima langkah diatas dapat dilakukan dengan mengeksekusi perintah berikut
```
pip install sklearn
pip install numpy
pip install pandas
pip install matplotlib
pip install scipy
```

## Cara Menggunakan Program
1. Clone repository ini
2. Masuk ke folder Tucil-Stima-2
3. Jalankan perintah ```python src/main.py```
4. Hasil eksekusi program berupa gambar akan terdapat pada folder result
5. Bila ingin menggunakan data lain, pastikan data tersebut dalam bentuk Dataframe minimal terdiri dari 2 atribut dan 1 kolom bernama 'Target'. Program akan otomatis membuat 3 pasang kombinasi atribut bila memungkinkan,bila tidak memungkinkan maka program hanya akan mengembalikan convex hull untuk sepasang atribut. Program mengembalikan convex hull dalam format list of tuples [a,b] dimana a dan b adalah indeks dari titik yang membentuk salah satu segmen garis convex hull.

## Penjelasan Singkat Fungsi drawConvexHull
1. Fungsi ini dipanggil ketika ingin menggambar convex hull dari sebuah kumpulan titik
2. Fungsi ini dipanggil dengan cara drawConvexHull(df,target_names,filename,mode)
3. df adalah Dataframe berisi data dengan minimum 2 atribut untuk divisualisasikan sebagai kumpulan titik
4. target_names adalah list berisi nama dari setiap jenis target. Dalam data Iris, list ini berisi [setosa,versicolor,virginica]
5. Filename adalah nama file yang dikehendaki untuk menyimpan gambar (tanpa format). Gambar ini akan tersimpan pada folder 
6. Mode diisi dengan 1 apabila ingin menggunakan algoritma miliki scipy, diisi dengan 0 apabila ingin menggunakan algoritma yang dibuat pada tugas ini


