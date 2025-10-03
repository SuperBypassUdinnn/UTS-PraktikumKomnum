import re
try:
    from sympy import sympify
except ImportError:
    import os
    os.system("pip install sympy")
    from sympy import sympify

def parse_expr(expr_input):
    expr_input = expr_input.lower()

    # Cek karakter legal
    if not re.fullmatch(r"[0-9x+\-*/^().\s]*", expr_input):
        raise ValueError("Ekspresi mengandung karakter tidak valid")

    expr = sympify(expr_input)
    vars = expr.free_symbols

    if len(vars) > 1:
        raise ValueError(f"Hanya boleh 1 variabel (x). Ditemukan: {', '.join(str(v) for v in vars)}")

    if len(vars) == 1 and str(list(vars)[0]) != 'x':
        raise ValueError(f"Variabel hanya boleh x")

    return expr
