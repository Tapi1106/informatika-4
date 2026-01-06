# soubor: vlakna_vs_procesy.py
import time
from multiprocessing import Process
import threading

# --- úloha: CPU-bound úloha ---
def vypocet(n=10_000_000):
    x = 0
    for _ in range(n):
        x += 1
    return x

# --- sekvenční běh ---
def sekvence():
    start = time.time()
    for _ in range(4):
        vypocet()
    print(f"[Sekvence] Čas: {time.time()-start:.2f} s")

# --- běh s vlákny ---
def vlakna():
    start = time.time()
    threads = [threading.Thread(target=vypocet) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(f"[Vlákna] Čas: {time.time()-start:.2f} s")

# --- běh s procesy ---
def procesy():
    start = time.time()
    procs = [Process(target=vypocet) for _ in range(4)]
    for p in procs:
        p.start()
    for p in procs:
        p.join()
    print(f"[Procesy] Čas: {time.time()-start:.2f} s")

# --- hlavní menu ---
if __name__ == "__main__":
    print("=== Test výkonu: Sekvence vs Vlákna vs Procesy ===")
    sekvence()
    vlakna()
    procesy()
    print("Hotovo! 🚀")
