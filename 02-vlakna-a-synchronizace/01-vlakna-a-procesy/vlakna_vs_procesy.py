# soubor: vlakna_vs_procesy.py
import time
from multiprocessing import Process
import threading

# --- úloha: CPU-bound úloha ---
def vypocet(n=10_000_000, start_opak=0, step=1, opakovani=20):
    """
    Každý proces nebo vlákno může počítat jen část opakování.
    - start_opak: první iterace pro tento proces/vlákno
    - step: přeskočí další 'step' opakování
    """
    for i in range(start_opak, opakovani, step):
        x = 0
        for _ in range(n):
            x += 1
    return x

# --- sekvenční běh ---
def sekvence():
    start = time.time()
    vypocet()  # celé 20 opakování počítá jeden proces
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

# --- běh s procesy, rozdělení 20 opakování mezi více procesů ---
def procesy(num_procesu=4):
    start = time.time()
    procs = []
    for i in range(num_procesu):
        # každý proces počítá své „kousky“ opakování
        p = Process(target=vypocet, args=(10_000_000, i, num_procesu, 4))
        procs.append(p)
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
    print("Hotovo")
