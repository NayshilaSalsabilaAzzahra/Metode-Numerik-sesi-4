import math

def f(t):
    return 800 * math.exp(0.3 * t) - 2000 - 400 * t

def regula_falsi(a, b, toleransi=0.0001, max_iter=20):
    print("==========================================================================")
    print("                  TUGAS METODE NUMERIK - PERSAMAAN NON LINEAR             ")
    print("==========================================================================")
    print(" Nama  : NAYSHILA SALSABILA AZZAHRA")
    print(" NIM   : 20250040004")
    print(" Kelas : TI25G")
    print(" Metode: Regula Falsi")
    print("==========================================================================\n")
    
    # Header tabel
    print(f"{'Iterasi':<8} {'a':<10} {'b':<10} {'f(a)':<12} {'f(b)':<12} {'c':<10} {'f(c)':<12} {'|b-a|':<10}")
    print("-" * 86)
    
    for i in range(1, max_iter + 1):
        fa = f(a)
        fb = f(b)
        c = b - (fb * (b - a)) / (fb - fa)
        fc = f(c)
        galat = abs(b - a)
        
        print(f"{i:<8} {a:<10.4f} {b:<10.4f} {fa:<12.4f} {fb:<12.4f} {c:<10.4f} {fc:<12.4f} {galat:<10.4f}")
        
        if abs(fc) < toleransi:
            break
            
        if fa * fc < 0:
            b = c
        else:
            a = c
            
    print("-" * 86)
    print(f"\nTitik impas (akar persamaan) t ≈ {c:.4f} bulan")

a_awal = 3.0
b_awal = 5.0

regula_falsi(a_awal, b_awal)