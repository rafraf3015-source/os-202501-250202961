import time

print("Program uji resource dimulai...")

data = []

for i in range(1, 5000):
    # Simulasi beban CPU
    _ = i * i

    # Simulasi alokasi memori (±10 KB per iterasi)
    data.append("X" * 10_000)

    if i % 1000 == 0:
        print(f"Iterasi: {i}, Perkiraan memori terpakai: {i * 10} KB")

    time.sleep(0.01)

print("Program selesai.")