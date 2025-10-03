import package

def main():
    a = int(input("Masukkan batas bawah (a): "))
    b = int(input("Masukkan batas atas (b): "))    
    e = float(input("Masukkan toleransi (e): "))
    n = int(input("Masukkan jumlah iterasi maksimum (n): "))
    fungsi = input("Masukkan fungsi F(x) dengan variabel x: ")  
    
    (hasil, data) = package.regula_falsi(a, b, e, n, fungsi) 

    package.tabel(data, highlight_row="xr", highlight=hasil)

if __name__ == "__main__":
    main()