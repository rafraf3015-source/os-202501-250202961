import time

print("=== WEEK13 Docker Resource Limit Test ===")

# 1. CPU Stress Test (60 detik)
print("CPU Stress Test (60s)...")
start = time.time()
while time.time() - start < 60:
    _ = sum(i * i for i in range(1000000))
    elapsed = int(time.time() - start)
    if elapsed % 10 == 0:
        print(f"   CPU: {elapsed}s")

print("CPU test selesai")

# 2. Memory Stress Test (400MB bertahap)
print("🧠 Memory Stress Test...")
mem_blocks = []
try:
    for i in range(80):
        block = bytearray(5 * 1024 * 1024)  # 5MB
        mem_blocks.append(block)
        print(f"   MEM: {(i+1)*5}MB")
        time.sleep(0.2)
    print("Memory test SUKSES (400MB)")
except MemoryError:
    print("MEMORY LIMIT! OOM Killer aktif")
print("Test selesai")
