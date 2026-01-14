
# Laporan Praktikum Minggu [X]
Topik: [Penjadwalan CPU – Round Robin (RR) dan Priority Scheduling]

---

## Identitas
- **Nama**  : [Rafi nurul fauzan]  
- **NIM**   : [250202961]  
- **Kelas** : [1IKRB]

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Contoh:  
1. Membandingkan performa algoritma RR dan Priority.  
2. Menjelaskan pengaruh *time quantum* dan prioritas terhadap keadilan eksekusi proses.  
3. Menarik kesimpulan mengenai efisiensi dan keadilan kedua algoritma.

---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

Penjadwalan CPU Round Robin (RR):
- Round Robin adalah algoritma penjadwalan preemptive yang memberikan jatah eksekusi CPU secara bergiliran kepada setiap proses dengan interval waktu tetap yang disebut quantum time.
- Quantum time biasanya antara 10 hingga 100 milisekon; penentuan waktu ini penting karena jika terlalu kecil menyebabkan banyak context switching, sedangkan jika terlalu besar algoritma berperilaku mirip FCFS.
- Algoritma ini bebas dari starvation karena semua proses mendapat giliran eksekusi secara adil tanpa prioritas tertentu.
- Round Robin cocok digunakan untuk sistem time-sharing dan meningkatkan respons time secara umum.

Priority Scheduling:
- Algoritma Priority Scheduling memberikan CPU kepada proses yang memiliki prioritas tertinggi terlebih dahulu.
- Prioritas dapat bersifat statis (tetap) atau dinamis (berubah sesuai kondisi).
- Jika ada proses dengan prioritas sama, biasanya ditangani dengan metode FCFS atau Round Robin.
- Priority Scheduling bisa menyebabkan proses dengan prioritas rendah mengalami starvation jika prioritas tinggi selalu muncul.
- Prioritas dapat dihitung berdasarkan beberapa kriteria seperti waktu pembuatan tugas, batas waktu pengerjaan, atau faktor lain sesuai kebijakan sistem.

Kutipan:
1. IMPLEMENTASI ALGORITMA PRIORITY SCHEDULING https://repository.mercubuana.ac.id/61657/1/01%20Cover.pdf

2. Sistem Operasi (Priority Scheduling) http://pietrajayaramadhan.blogspot.com/2013/04/sistem-operasi-priority-scheduling.html

3. Pengertian Priority Scheduling https://rifqimulyawan.com/literasi/priority-scheduling/

4. ROUND-ROBIN SCHEDULING https://binus.ac.id/malang/2021/11/round-robin-scheduling/

5. Perbedaan antara Penjadwalan Prioritas dan ... https://translate.google.com/translate?u=https%3A%2F%2Fwww.geeksforgeeks.org%2Foperating-systems%2Fdifference-between-priority-scheduling-and-round-robin-rr-cpu-scheduling%2F&hl=id&sl=en&tl=id&client=srp

6. Penjadwalan Prioritas dalam Sistem Operasi https://translate.google.com/translate?u=https%3A%2F%2Fwww.geeksforgeeks.org%2Foperating-systems%2Fpriority-scheduling-in-operating-system%2F&hl=id&sl=en&tl=id&client=srp

7. Algoritma Penjadwalan CPU Round-Robin Berbasis Prioritas ... https://translate.google.com/translate?u=https%3A%2F%2Fchiraggoyaliit.medium.com%2Fpriority-based-round-robin-cpu-scheduling-algorithm-f9aa8517a844&hl=id&sl=en&tl=id&client=srp

---

## Langkah Praktikum
1. **Siapkan Data Proses**
   Gunakan contoh data berikut (boleh dimodifikasi sesuai kebutuhan):
   | Proses | Burst Time | Arrival Time | Priority |
   |:--:|:--:|:--:|:--:|
   | P1 | 5 | 0 | 2 |
   | P2 | 3 | 1 | 1 |
   | P3 | 8 | 2 | 4 |
   | P4 | 6 | 3 | 3 |

2. **Eksperimen 1 – Round Robin (RR)**
   - Gunakan *time quantum (q)* = 3.  
   - Hitung *waiting time* dan *turnaround time* untuk tiap proses.  
   - Simulasikan eksekusi menggunakan Gantt Chart (manual atau spreadsheet).  
     ```
     | P1 | P2 | P3 | P4 | P1 | P3 | ...
     0    3    6    9   12   15   18  ...
     ```
   - Catat sisa *burst time* tiap putaran.

3. **Eksperimen 2 – Priority Scheduling (Non-Preemptive)**
   - Urutkan proses berdasarkan nilai prioritas (angka kecil = prioritas tinggi).  
   - Lakukan perhitungan manual untuk:
     ```
     WT[i] = waktu mulai eksekusi - Arrival[i]
     TAT[i] = WT[i] + Burst[i]
     ```
   - Buat tabel perbandingan hasil RR dan Priority.

4. **Eksperimen 3 – Analisis Variasi Time Quantum (Opsional)**
   - Ubah *quantum* menjadi 2 dan 5.  
   - Amati perubahan nilai rata-rata *waiting time* dan *turnaround time*.  
   - Buat tabel perbandingan efek *quantum*.

5. **Eksperimen 4 – Dokumentasi**
   - Simpan semua hasil tabel dan screenshot ke:
     ```
     praktikum/week6-scheduling-rr-priority/screenshots/
     ```
   - Buat tabel perbandingan seperti berikut:

     | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
     |------------|------------------|----------------------|------------|-------------|
     | RR | ... | ... | Adil terhadap semua proses | Tidak efisien jika quantum tidak tepat |
     | Priority | ... | ... | Efisien untuk proses penting | Potensi *starvation* pada prioritas rendah |

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 6 - CPU Scheduling RR & Priority"
   git push origin main
   ```


---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
   - Gunakan *time quantum (q)* = 3.  
   - Hitung *waiting time* dan *turnaround time* untuk tiap proses.  
   - Simulasikan eksekusi menggunakan Gantt Chart (manual atau spreadsheet).
   - Ubah *quantum* menjadi 2 dan 5.  
   - Amati perubahan nilai rata-rata *waiting time* dan *turnaround time*.  
   - Buat tabel perbandingan efek *quantum*.
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)
![Screenshot hasil](screenshots/Screenshot%202025-11-06%20205324.png)

---

## Analisis


1. Data Proses (Burst Time, Arrival Time, Priority)

| Proses | Burst Time | Arrival Time | Priority |
|--------|------------|--------------|----------|
| P1     | 5          | 0            | 2        |
| P2     | 3          | 1            | 1        |
| P3     | 8          | 2            | 4        |
| P4     | 6          | 3            | 3        |

*

2. Eksperimen 1 – Round Robin (q=3)

Gantt Chart simulasi RR:

| P1 | P2 | P3 | P4 | P1 | P3 | P4 | P3 |
|----|----|----|----|----|----|----|----|
0    3    6    9   12   14   17   20   22  

- Proses dieksekusi selama quantum 3 atau sisa burst time jika kurang.
- Sisa burst time dialami setelah masing-masing putaran.

Perhitungan sisa burst time per putaran:

- Putaran 1: P1(5-3=2), P2(3-3=0), P3(8-3=5), P4(6-3=3)
- Putaran 2: P1(2-2=0), P3(5-3=2), P4(3-3=0)
- Putaran 3: P3(2-2=0)

Menghitung Waiting Time (WT) dan Turnaround Time (TAT):

| Proses | Burst | Arrival | Finish Time | TAT = Finish - Arrival | WT = TAT - Burst |
|--------|-------|---------|-------------|------------------------|------------------|
| P1     | 5     | 0       | 14          | 14 - 0 = 14            | 14-5=9           |
| P2     | 3     | 1       | 6           | 6 - 1 = 5              | 5-3=2            |
| P3     | 8     | 2       | 22          | 22 - 2 = 20            | 20-8=12          |
| P4     | 6     | 3       | 17          | 17 - 3 = 14            | 14-6=8           |



3. Eksperimen 2 – Priority Scheduling (Non-Preemptive)

Proses diurutkan berdasarkan prioritas terkecil dulu: P2(1), P1(2), P4(3), P3(4).

Urutan eksekusi sesuai Arrival dan prioritas:

- P1 tiba duluan pada waktu 0 tapi P2 dengan prioritas lebih tinggi tiba pada 1, jadi jika non-preemptive, yang eksekusi duluan mulai dari 0 adalah P1 (karena P2 belum hadir).
- Kita eksekusi P1 dulu (waktu 0-5).
- Selanjutnya P2 sudah hadir saat P1 selesai (waktu 5), jalankan P2 (5-8).
- Kemudian P4 (8-14).
- Terakhir P3 (14-22).

Hitung WT dan TAT:

| Proses | Burst | Arrival | Start Time | Finish Time | TAT = Finish - Arrival | WT = Start - Arrival |
|--------|-------|---------|------------|-------------|------------------------|----------------------|
| P1     | 5     | 0       | 0          | 5           | 5 - 0 = 5              | 0 - 0 = 0            |
| P2     | 3     | 1       | 5          | 8           | 8 - 1 = 7              | 5 - 1 = 4            |
| P4     | 6     | 3       | 8          | 14          | 14 - 3 = 11            | 8 - 3 = 5            |
| P3     | 8     | 2       | 14         | 22          | 22 - 2 = 20            | 14 - 2 = 12          |



4. Perbandingan Hasil RR dan Priority

| Proses | WT RR | TAT RR | WT Priority | TAT Priority |
|--------|-------|--------|-------------|--------------|
| P1     | 9     | 14     | 0           | 5            |
| P2     | 2     | 5      | 4           | 7            |
| P3     | 12    | 20     | 12          | 20           |
| P4     | 8     | 14     | 5           | 11           |

Rata-rata WT dan TAT:

| Algoritma       | Avg WT       | Avg TAT     |
|-----------------|--------------|-------------|
| Round Robin (q=3) | (9+2+12+8)/4 = 7.75 | (14+5+20+14)/4 = 13.25 |
| Priority (Non-Preemptive) | (0+4+12+5)/4 = 5.25 | (5+7+20+11)/4 = 10.75 |



5. Dokumentasi Tabel Kelebihan & Kekurangan

| Algoritma       | Avg Waiting Time | Avg Turnaround Time | Kelebihan                       | Kekurangan                          |
|-----------------|------------------|---------------------|---------------------------------|-----------------------------------|
| Round Robin (q=3) | 7.75             | 13.25               | Adil terhadap semua proses      | Tidak efisien jika quantum tidak tepat (context switch banyak atau respons lambat)  |
| Priority (Non-Preemptive) | 5.25             | 10.75               | Efisien untuk proses penting    | Potensi starvation pada prioritas rendah, tidak preemptive                    |

Jika ingin, langkah 3 (variasi quantum) dapat dilakukan untuk lebih analisis.

Semua hasil ini bisa disimpan dan didokumentasikan sesuai direktori yang diinginkan. Jika ingin bantuan membuat Gantt Chart visual, bisa dibantu juga.


1. Perhitungan Waiting Time dan Turnaround Time

Round Robin (Quantum = 3)

| Proses | Burst Time | Arrival Time | Finish Time | Turnaround Time (TAT) | Waiting Time (WT) |
|--------|------------|--------------|-------------|-----------------------|-------------------|
| P1     | 5          | 0            | 14          | 14 - 0 = 14           | 14 - 5 = 9        |
| P2     | 3          | 1            | 6           | 6 - 1 = 5             | 5 - 3 = 2         |
| P3     | 8          | 2            | 22          | 22 - 2 = 20           | 20 - 8 = 12       |
| P4     | 6          | 3            | 17          | 17 - 3 = 14           | 14 - 6 = 8        |

Priority Scheduling (Non-Preemptive)

| Proses | Burst Time | Arrival Time | Start Time | Finish Time | Turnaround Time (TAT) | Waiting Time (WT) |
|--------|------------|--------------|------------|-------------|-----------------------|-------------------|
| P1     | 5          | 0            | 0          | 5           | 5 - 0 = 5             | 0 - 0 = 0         |
| P2     | 3          | 1            | 5          | 8           | 8 - 1 = 7             | 5 - 1 = 4         |
| P4     | 6          | 3            | 8          | 14          | 14 - 3 = 11           | 8 - 3 = 5         |
| P3     | 8          | 2            | 14         | 22          | 22 - 2 = 20           | 14 - 2 = 12       |

*

2. Gantt Chart Simulasi

```bash
Round Robin (Quantum=3):

| P1 | P2 | P3 | P4 | P1 | P3 | P4 | P3 |  
0    3    6    9   12   14   17   20   22  

Priority Scheduling (Non-Preemptive):

| P1 | P2 | P4 | P3 |  
0    5    8   14   22  
```


3. Perbandingan Performa dan Pengaruh Time Quantum & Prioritas

- Algoritma *Round Robin* memberikan fairness dengan membagi waktu CPU secara bergilir, menghindari starvation, tetapi waktu tunggu bisa lebih lama tergantung ukuran quantum. Quantum kecil meningkatkan respons tetapi menaikkan overhead context switch, quantum besar mengurangi overhead tapi mengorbankan fairness.  
- Algoritma *Priority Scheduling* memproses sesuai prioritas sehingga proses penting lebih cepat selesai, mengurangi rata-rata waiting time, tetapi proses dengan prioritas rendah bisa mengalami starvation jika tidak ada mekanisme aging.  
- Pengaruh time quantum pada RR sangat signifikan untuk performa sistem, dan pengaturan prioritas pada algoritma priority menentukan keadilan dan efektivitas sistem.


---

## Kesimpulan

1. Algoritma Round Robin efektif dalam memberikan alokasi CPU yang adil ke semua proses, menghindari starvation, dan cocok digunakan di sistem time-sharing. Namun, performanya sangat tergantung pada pemilihan quantum waktu; quantum yang terlalu kecil menyebabkan overhead context switching banyak, sedangkan quantum yang terlalu besar menurunkan responsivitas.

2. Priority Scheduling sangat efisien untuk mengutamakan proses dengan prioritas tinggi sehingga mempercepat penyelesaian tugas penting, tetapi berisiko menyebabkan starvation pada proses prioritas rendah jika tidak diimbangi mekanisme aging.

---

## Quiz
1. [Apa perbedaan utama antara Round Robin dan Priority Scheduling?] 

   Round Robin (RR) memberikan waktu CPU secara bergilir kepada semua proses dengan interval waktu tetap (quantum), sehingga semua proses mendapat kesempatan eksekusi secara adil tanpa memprioritaskan proses tertentu. Sedangkan Priority Scheduling memberikan CPU berdasarkan prioritas proses, dimana proses dengan prioritas lebih tinggi (nilai prioritas lebih kecil) dieksekusi lebih dulu, yang berarti proses dengan prioritas rendah harus menunggu lebih lama.

2. [Apa pengaruh besar/kecilnya time quantum terhadap performa sistem?]

   Time quantum yang kecil menyebabkan proses lebih sering bergantian (context switch terjadi lebih sering), sehingga overhead CPU untuk switching tinggi dan performa bisa menurun. Sedangkan time quantum yang besar mengurangi frekuensi context switch, tapi menyebabkan proses lama mendapatkan CPU selama waktu lama sehingga proses lain harus menunggu, membuat respons sistem menurun dan berperilaku seperti First-Come-First-Served (FCFS). 

3. [Mengapa algoritma Priority dapat menyebabkan starvation?]  
   Pada Priority Scheduling, proses dengan prioritas rendah dapat terus-menerus menunggu jika ada banyak proses dengan prioritas lebih tinggi yang terus masuk dan dieksekusi, sehingga proses prioritas rendah tersebut berpotensi tidak pernah mendapatkan kesempatan eksekusi, keadaan ini dikenal sebagai starvation atau indefinite blocking.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
memahami cara menghitung Round robin (bergilir) dan Priority Scheduling(berdasarkan nilai prioritas)
- Bagaimana cara Anda mengatasinya?  
belajar memahami dan mencari cara menghitungnya di internet
---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
