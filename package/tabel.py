try:
    from tabulate import tabulate
except ImportError:
    raise ImportError("Please install the 'tabulate' package: pip install tabulate")

# ANSI escape codes
YELLOW = "\033[33m"  # Yellow text
CYAN   = "\033[36m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

def tabel(data: dict[str, list], highlight_row: str, highlight: float) -> None:
    # Panjang maksimal list
    panjang = max(len(v) for v in data.values())

    rows = []
    highlight_index = None
    highlight_value = None

    for i in range(panjang):
        row = []
        for key in data.keys():
            if i < len(data[key]):
                val = data[key][i]
                if key == highlight_row and isinstance(val, (float, int)) and val == highlight:
                    row.append(f"{YELLOW}{val}{RESET}")
                    highlight_index = i + 1  # simpan iterasi (mulai dari 1)
                    highlight_value = f"{YELLOW}{val}{RESET}"
                else:
                    row.append(val)
            else:
                row.append("")
        rows.append(row)

    # Header berwarna cyan tebal
    headers = [f"{BOLD}{CYAN}{h}{RESET}" for h in data.keys()]

    # Tentukan alignment per kolom
    # Misal: iterasi (center), sisanya (right)
    colalign = []
    for h in data.keys():
        if h.lower() == "iterasi":
            colalign.append("center")
        else:
            colalign.append("right")

    # Tampilkan tabel dengan alignment
    print(tabulate(rows, headers=headers, tablefmt="grid", colalign=colalign))

    # Tampilkan hasil akhir jika ada highlight
    if highlight_index is not None and highlight_value is not None:
        print(f"\nAkar aproksimasi setelah {highlight_index} iterasi: {highlight_value}")
