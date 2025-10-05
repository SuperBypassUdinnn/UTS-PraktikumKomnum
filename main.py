import package
import os

def print_banner():
    banner = [
        "╔" + "═" * 32 + "╗",
        "║{:^32}║".format("METODE REGULA FALSI"),
        "╚" + "═" * 32 + "╝"
    ]
    for line in banner:
        print(line)
    print("\nPress Enter to start")

def main():
    print_banner()
    input()  # Wait for user to press Enter

    # Clear screen (Windows)
    os.system('cls')

    a      = float(input("Masukkan batas bawah (a)              : "))
    b      = float(input("Masukkan batas atas (b)               : "))    
    e      = float(input("Masukkan toleransi (e)                : "))
    n      = int(input("Masukkan jumlah iterasi maksimum (n)  : "))
    fungsi = input("Masukkan fungsi F(x) dengan variabel x: ")  
    
    (hasil, data) = package.regula_falsi(a, b, e, n, fungsi) 

    package.tabel(data, highlight_row="xr", highlight=hasil)

if __name__ == "__main__":
    main()