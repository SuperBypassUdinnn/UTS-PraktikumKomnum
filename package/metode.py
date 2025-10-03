from package.parsexpr import parse_expr


def regula_falsi(a, b, e, n, fungsi):
    # Fungsi F(x)
    fungsi = parse_expr(fungsi)
    def F(x, expr):
        return float(expr.subs('x', x))
    
    # List F(a), F(b), F(xr)
    iterasiList = []
    aList = []
    bList = []
    xrList = []
    FaList = []
    FbList = []
    FxrList = []
    FaFxrList = []
    mutlakFxrList = []

    xr = 0
    hasil = 0

    if n <= 0 :
        raise ValueError("Jumlah iterasi harus lebih dari 0")
    elif e <= 0 :
        raise ValueError("Toleransi harus lebih dari 0")
    elif a >= b :
        raise ValueError("Batas bawah harus lebih kecil dari batas atas")
    elif F(a, fungsi) * F(b, fungsi) > 0 :
        print("Tidak ada akar pada interval [a,b]")
        exit()
    elif F(a, fungsi) * F(b, fungsi) == 0 :
        hasil = a if F(a, fungsi) == 0 else b
    else :
        for i in range(n):
            Fa = F(a, fungsi)
            Fb = F(b, fungsi)
            xr = (Fb * a - Fa * b) / (Fb - Fa)
            Fxr = F(xr, fungsi)
            FaFxr = Fa * Fxr
            mutlakFxr = abs(Fxr)

            iterasiList.append(i + 1)
            aList.append(a)
            bList.append(b)
            xrList.append(xr)
            FaList.append(Fa)
            FbList.append(Fb)
            FxrList.append(Fxr) 
            mutlakFxrList.append(mutlakFxr)

            if FaFxr < 0 :
                # Mengecek toleransi
                FaFxrList.append(FaFxr)
                if mutlakFxr < e :
                    hasil = xr
                    break
                b = xr
            elif FaFxr > 0 :
                # Mengecek toleransi
                FaFxrList.append(FaFxr)
                if mutlakFxr < e :
                    hasil = xr
                    break
                a = xr
            else:
                hasil = xr
                break
    data = {
        "iterasi": iterasiList,
        "a": aList,
        "b": bList,
        "xr": xrList,
        "F(a)": FaList,
        "F(b)": FbList,
        "F(xr)": FxrList,
        "F(a)*F(xr)": FaFxrList,
        "|F(xr)|": mutlakFxrList
    }
    
    return hasil, data
