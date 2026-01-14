# Simulasi Penjadwalan CPU - FCFS dan SJF Non-Preemptive
# Dataset: P1(0,6), P2(1,8), P3(2,7), P4(3,3)

processes = [
    {'pid': 'P1', 'arrival': 0, 'burst': 6},
    {'pid': 'P2', 'arrival': 1, 'burst': 8},
    {'pid': 'P3', 'arrival': 2, 'burst': 7},
    {'pid': 'P4', 'arrival': 3, 'burst': 3}
]

def fcfs(processes):
    """FCFS: First Come First Served"""
    proc = sorted(processes.copy(), key=lambda x: x['arrival'])
    current_time = 0
    
    for p in proc:
        start = max(current_time, p['arrival'])
        p['start_time'] = start
        p['completion_time'] = start + p['burst']
        p['turnaround_time'] = p['completion_time'] - p['arrival']
        p['waiting_time'] = p['turnaround_time'] - p['burst']
        current_time = p['completion_time']
    
    avg_waiting = sum(p['waiting_time'] for p in proc) / len(proc)
    avg_turnaround = sum(p['turnaround_time'] for p in proc) / len(proc)
    return proc, avg_waiting, avg_turnaround

def sjf_nonpreemptive(processes):
    """SJF Non-Preemptive: Shortest Job First"""
    proc = sorted(processes.copy(), key=lambda x: x['arrival'])
    current_time = 0
    ready_queue = []
    i = 0
    
    while i < len(proc) or ready_queue:
        # Masukkan proses yang sudah arrive ke ready queue
        while i < len(proc) and proc[i]['arrival'] <= current_time:
            ready_queue.append(proc[i])
            i += 1
        
        if ready_queue:
            # Pilih proses dengan burst time terpendek
            ready_queue.sort(key=lambda x: x['burst'])
            p = ready_queue.pop(0)
            
            start = max(current_time, p['arrival'])
            p['start_time'] = start
            p['completion_time'] = start + p['burst']
            p['turnaround_time'] = p['completion_time'] - p['arrival']
            p['waiting_time'] = p['turnaround_time'] - p['burst']
            current_time = p['completion_time']
        else:
            current_time += 1
    
    avg_waiting = sum(p['waiting_time'] for p in proc) / len(proc)
    avg_turnaround = sum(p['turnaround_time'] for p in proc) / len(proc)
    return proc, avg_waiting, avg_turnaround

# Eksekusi simulasi
print("=== SIMULASI PENJADWALAN CPU ===\n")

# FCFS
fcfs_procs, fcfs_avg_wt, fcfs_avg_tat = fcfs(processes)
print("1. FCFS (First Come First Served)")
print("| PID | AT | BT | ST  | CT  | WT  | TAT |")
print("|-----|----|----|-----|-----|-----|-----|")
for p in fcfs_procs:
    print(f"| {p['pid']:^3} | {p['arrival']:^2} | {p['burst']:^2} | {p['start_time']:^3} | {p['completion_time']:^3} | {p['waiting_time']:^3} | {p['turnaround_time']:^3} |")
print(f"| **Rata** |    |    |     |     | **{fcfs_avg_wt:.2f}** | **{fcfs_avg_tat:.2f}** |")
print()

# SJF
sjf_procs, sjf_avg_wt, sjf_avg_tat = sjf_nonpreemptive(processes)
print("2. SJF Non-Preemptive")
print("| PID | AT | BT | ST  | CT  | WT  | TAT |")
print("|-----|----|----|-----|-----|-----|-----|")
for p in sjf_procs:
    print(f"| {p['pid']:^3} | {p['arrival']:^2} | {p['burst']:^2} | {p['start_time']:^3} | {p['completion_time']:^3} | {p['waiting_time']:^3} | {p['turnaround_time']:^3} |")
print(f"| **Rata** |    |    |     |     | **{sjf_avg_wt:.2f}** | **{sjf_avg_tat:.2f}** |")
