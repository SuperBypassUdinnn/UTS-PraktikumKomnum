import numpy as np
import math
from tabulate import tabulate

# ANSI escape code untuk warna
YELLOW = "\033[43m"
RESET = "\033[0m"

"""
Fungsi untuk menampilkan data dalam format tabel dengan penyorotan pada baris tertentu.
Args:
    data (dict): Dictionary dengan kunci sebagai nama kolom dan nilai sebagai list data.
    highlight_row (str): Nama kolom yang ingin disorot.
    highlight (float): Nilai yang ingin disorot dalam kolom tersebut.
"""
def tabel(data: dict, highlight_row: str, highlight: float) -> None:
    # Panjang maksimal list
    panjang = max(len(v) for v in data.values())
    
    # Susun baris-baris tabel
    rows = []
    for i in range(panjang):
        row = []
        for key in data.keys():
            if i < len(data[key]):
                val = data[key][i]
                # Cek apakah nilai cocok dengan highlight dan berada di kolom yang ditentukan
                if key == highlight_row and isinstance(val, (float, int)) and val == highlight:
                    row.append(f"{YELLOW}{val}{RESET}")
                else:
                    row.append(val)
            else:
                row.append("")  # kosong jika list tidak sama panjang
        rows.append(row)
    
    # Tampilkan tabel dengan garis
    print(tabulate(rows, headers=list(data.keys()), tablefmt="grid"))
