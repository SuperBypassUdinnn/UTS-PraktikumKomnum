
# UTS PRAKTIKUM KOMPUTASI NUMERIK - METODE REGULA FALSI

Projek ini dibuat dengan tujuan untuk menyelesaikan Ujian Tengah Semester Praktikum Komputasi Numerik 2025. Repository ini berisi implementasi metode numerik Regula Falsi (false position) untuk mencari akar persamaan satu variabel F(x).

![Logo](https://upload.wikimedia.org/wikipedia/en/archive/c/c3/20181215082857%21Unsyiah-logo.svg)

## Tujuan
Memberikan alat sederhana berbasis terminal untuk menghitung akar persamaan non-linear menggunakan metode Regula Falsi. Cocok untuk keperluan pembelajaran metode numerik.

## Anggota Kelompok
1. Abdullah Asy-Syifawi - 2408107010042 ([@abdullahasfw](https://github.com/abdullahasfw))
2. Fadhlurrahman Alaudin - 2408107010053 ([@SuperBypassUdinnn](https://github.com/SuperBypassUdinnn))
3. Maulana Shidqi Albadawie - 2408107010047 ([@MasDiq18](https://github.com/MasDiq18))
4. Rahiqul Munadhil - 2408107010049 ([@LeMikayla](https://github.com/LeMikayla))
5. Sausan Irtiyaah - 2408107010048 ([@susanrtyh](https://github.com/susanrtyh))

## Contoh Penggunaan

#### Jalankan kode
Pastikan anda sudah menginstall python. Kemudian masuk dalam folder dan jalankan:
```bash
  python main.py
```

#### Tekan tombol bebas  

```bash
  ╔════════════════════════════════╗
  ║      METODE REGULA FALSI       ║
  ╚════════════════════════════════╝

  Press anykey to start
```
Tekan tombol apa saja yang anda inginkan untuk lanjut ke halaman selanjutnya

#### Masukkan data
Masukkan data batas atas, batas bawah, iterasi maksimum, dan fungsi f(x)
```bash
  Masukkan batas bawah (a)              : 2
  Masukkan batas atas (b)               : 4
  Masukkan toleransi (e)                : 0.001
  Masukkan jumlah iterasi maksimum (n)  : 10
  Masukkan fungsi F(x) dengan variabel x: x^2-4x+3

```


#### Output

Jika akar penyelesaian ditemukan, output tabelnya:
```bash
+-----------+---------+-----+---------+-------------+--------+--------------+--------------+-------------+
|  iterasi  |       a |   b |      xr |        F(a) |   F(b) |        F(xr) |   F(a)*F(xr) |     |F(xr)| |
+===========+=========+=====+=========+=============+========+==============+==============+=============+
|     1     |       2 |   4 |     2.5 |          -1 |      3 |        -0.75 |         0.75 |        0.75 |
+-----------+---------+-----+---------+-------------+--------+--------------+--------------+-------------+
|     2     |     2.5 |   4 |     2.8 |       -0.75 |      3 |        -0.36 |         0.27 |        0.36 |
+-----------+---------+-----+---------+-------------+--------+--------------+--------------+-------------+
|     3     |     2.8 |   4 | 2.92857 |       -0.36 |      3 |    -0.137755 |    0.0495918 |    0.137755 |
+-----------+---------+-----+---------+-------------+--------+--------------+--------------+-------------+
|     4     | 2.92857 |   4 | 2.97561 |   -0.137755 |      3 |   -0.0481856 |   0.00663781 |   0.0481856 |
+-----------+---------+-----+---------+-------------+--------+--------------+--------------+-------------+
|     5     | 2.97561 |   4 |  2.9918 |  -0.0481856 |      3 |   -0.0163263 |  0.000786691 |   0.0163263 |
+-----------+---------+-----+---------+-------------+--------+--------------+--------------+-------------+
|     6     |  2.9918 |   4 | 2.99726 |  -0.0163263 |      3 |  -0.00547195 |  8.93364e-05 |  0.00547195 |
+-----------+---------+-----+---------+-------------+--------+--------------+--------------+-------------+
|     7     | 2.99726 |   4 | 2.99909 | -0.00547195 |      3 |  -0.00182732 |  9.99899e-06 |  0.00182732 |
+-----------+---------+-----+---------+-------------+--------+--------------+--------------+-------------+
|     8     | 2.99909 |   4 |  2.9997 | -0.00182732 |      3 | -0.000609477 |  1.11371e-06 | 0.000609477 |
+-----------+---------+-----+---------+-------------+--------+--------------+--------------+-------------+

Akar aproksimasi setelah 8 iterasi: 2.9996952148735145

```
