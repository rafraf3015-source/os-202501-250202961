def simulate_fifo(ref_string, frames):
    memory = []
    queue = []
    faults = 0
    
    print("\n" + "="*55)
    print("FIFO PAGE REPLACEMENT")
    print("="*55)
    print(f"{'Ref':>3} | {'Memory':^20} | {'Fault':>5}")
    print("-"*55)
    
    for page in ref_string:
        if page not in memory:
            if len(memory) < frames:
                memory.append(page)
                queue.append(page)
            else:
                victim = queue.pop(0)
                memory.remove(victim)
                memory.append(page)
                queue.append(page)
            faults += 1
            print(f"{page:>3} | {' '.join(map(str,memory)):^20} | {'✓':>5}")
        else:
            print(f"{page:>3} | {' '.join(map(str,memory)):^20} | {'-':>5}")
    
    print("-"*55)
    return faults

def simulate_lru(ref_string, frames):
    memory = []
    faults = 0
    
    print("\n" + "="*55)
    print("LRU PAGE REPLACEMENT")
    print("="*55)
    print(f"{'Ref':>3} | {'Memory':^20} | {'Fault':>5}")
    print("-"*55)
    
    for page in ref_string:
        if page not in memory:
            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)  # Remove LRU
                memory.append(page)
            faults += 1
            print(f"{page:>3} | {' '.join(map(str,memory)):^20} | {'✓':>5}")
        else:
            memory.remove(page)
            memory.append(page)  # Move to MRU
            print(f"{page:>3} | {' '.join(map(str,memory)):^20} | {'-':>5}")
    
    print("-"*55)
    return faults

# Dataset uji
ref_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frames = 3

print("PAGE REPLACEMENT SIMULATION")
print(f"Reference: {ref_string}")
print(f"Frames: {frames}")
print()

fifo_faults = simulate_fifo(ref_string, frames)
lru_faults = simulate_lru(ref_string, frames)

# Tabel perbandingan
print("\n" + "="*40)
print("PERBANDINGAN")
print("="*40)
print(f"{'Algo':<8} {'Faults':<8} {'Rate':<8}")
print("-"*40)
print(f"{'FIFO':<8} {fifo_faults:<8} {fifo_faults/13*100:.1f}%")
print(f"{'LRU':<8} {lru_faults:<8} {lru_faults/13*100:.1f}%")
print("="*40)
