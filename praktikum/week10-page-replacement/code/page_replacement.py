def print_table(header, data, title):
    """Print tabel rapi tanpa library eksternal"""
    print(f"\n=== {title} ===")
    print("-" * 50)
    print(f"{header[0]:^4} | {header[1]:^18} | {header[2]:^5}")
    print("-" * 50)
    for row in data:
        print(f"{row[0]:^4} | {row[1]:^18} | {row[2]:^5}")
    print("-" * 50)

def simulate_fifo(reference_string, num_frames):
    """FIFO Page Replacement"""
    memory = []
    fifo_queue = []
    faults = 0
    table_data = []
    
    for page in reference_string:
        memory_str = ' '.join(map(str, memory))
        
        if page not in memory:
            if len(memory) < num_frames:
                memory.append(page)
                fifo_queue.append(page)
            else:
                victim = fifo_queue.pop(0)
                memory.remove(victim)
                memory.append(page)
                fifo_queue.append(page)
            faults += 1
            table_data.append([page, memory_str, '✓'])
        else:
            table_data.append([page, memory_str, '-'])
    
    print_table(['Ref', 'Memory (3 frames)', 'Fault'], table_data, "FIFO Page Replacement")
    print(f"Total Page Faults: {faults}")
    return faults

def simulate_lru(reference_string, num_frames):
    """LRU Page Replacement"""
    memory = []
    faults = 0
    table_data = []
    
    for page in reference_string:
        memory_str = ' '.join(map(str, memory))
        
        if page not in memory:
            if len(memory) < num_frames:
                memory.append(page)
            else:
                # LRU: hapus paling lama tidak digunakan (index 0)
                memory.pop(0)
                memory.append(page)
            faults += 1
            table_data.append([page, memory_str, '✓'])
        else:
            # Update ke paling baru (pindah ke akhir)
            memory.remove(page)
            memory.append(page)
            table_data.append([page, memory_str, '-'])
    
    print_table(['Ref', 'Memory (3 frames)', 'Fault'], table_data, "LRU Page Replacement")
    print(f"Total Page Faults: {faults}")
    return faults

# Dataset uji
reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
num_frames = 3

print("SIMULASI PAGE REPLACEMENT")
print(f"Reference String: {reference_string}")
print(f"Number of Frames: {num_frames}\n")

# Eksekusi simulasi
fifo_faults = simulate_fifo(reference_string, num_frames)
lru_faults = simulate_lru(reference_string, num_frames)

# Tabel perbandingan
print("\n=== PERBANDINGAN ALGORITMA ===")
print("-" * 40)
print(f"{'Algoritma':^12} | {'Page Faults':^12} | {'Fault Rate':^10}")
print("-" * 40)
print(f"{'FIFO':^12} | {fifo_faults:^12} | {fifo_faults/13*100:.1f}%")
print(f"{'LRU':^12} | {lru_faults:^12} | {lru_faults/13*100:.1f}%")
print("-" * 40)
