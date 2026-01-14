
# Laporan Praktikum Minggu [X]
Topik: [Penjadwalan CPU – FCFS dan SJF]

---

## Identitas
- **Nama**  : [Rafi nurul fauzan]  
- **NIM**   : [250202961]  
- **Kelas** : [1IKRB]

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
1. Menghitung *waiting time* dan *turnaround time* untuk algoritma FCFS dan SJF.  
2. Menyajikan hasil perhitungan dalam tabel yang rapi dan mudah dibaca.  
3. Membandingkan performa FCFS dan SJF berdasarkan hasil analisis. 

---

## Dasar Teori

- FCFS adalah algoritma penjadwalan CPU yang paling sederhana di mana proses dijalankan sesuai urutan kedatangan (arrival time), proses yang datang lebih dulu akan dieksekusi lebih dulu (non-preemptif). Kelemahannya adalah bisa menyebabkan waktu tunggu dan waktu penyelesaian yang lama terutama jika proses pertama memerlukan waktu lama (konsep antrian).

- SJF adalah algoritma penjadwalan yang memilih proses dengan waktu CPU burst terpendek terlebih dahulu. Ada dua jenis SJF: non-preemptive yang menyelesaikan proses yang sedang berjalan sampai selesai, dan preemptive (disebut juga Shortest Remaining Time First/SRTF) yang bisa mengganti proses berjalan jika ada proses baru yang lebih singkat waktunya. SJF secara teori memberikan rata-rata waktu tunggu dan turnaround time yang paling optimal dibanding FCFS.

- SJF termasuk kategori penjadwalan prioritas khusus di mana prioritas ditentukan oleh lama CPU burst, sehingga proses dengan waktu burst paling kecil memiliki prioritas tertinggi. Masalah yang muncul pada SJF adalah kemungkinan starvation untuk proses dengan burst panjang karena proses singkat terus didahulukan.

- FCFS bersifat mudah diimplementasikan dan adil karena berurutan sesuai datang, tetapi bisa membuat CPU tidak efisien saat ada proses panjang di depan. SJF mengoptimalkan efisiensi CPU dan waktu tunggu, tetapi memerlukan estimasi CPU burst yang akurat dan dapat menyebabkan starvation.

- Contoh perbandingan: rata-rata waiting time untuk SJF biasanya lebih rendah dari FCFS seperti yang ditunjukkan dalam praktikum dan simulasi dimana SJF menghasilkan waktu tunggu yang lebih minim dan turnaround time lebih kecil.

1. Implementasi CPU Scheduling dalam Multiprogramming ... https://informatika.stei.itb.ac.id/~rinaldi.munir/Stmik/2021-2022/Makalah/Makalah-IF2211-Stima-2022-K1%20(36).pdf

2. Makalah Sistem Operasi "Penjadwalan Cpu" https://id.scribd.com/document/613259045/6

3. perhitungan penjadwalan cpu fcfs dan sjf premtive dan non ... https://www.slideshare.net/slideshow/perhitungan-penjadwalan-cpu-fcfs-dan-sjf-premtive-dan-non-premtive/266583040

4. Praktikum 10 Penjadwalan CPU 2 https://spada.uns.ac.id/mod/resource/view.php?id=216919

5. Perbedaan Antara Algoritma Penjadwalan CPU FCFS dan ... https://translate.google.com/translate?u=https%3A%2F%2Fwww.geeksforgeeks.org%2Foperating-systems%2Fdifference-between-fcfs-and-sjf-cpu-scheduling-algorithms%2F&hl=id&sl=en&tl=id&client=srp

6. Penjadwalan CPU https://arna.lecturer.pens.ac.id/Diktat_SO/4.Penjadwalan%20CPU.pdf

7. Algoritma penjadwalan proses | PPT https://www.slideshare.net/slideshow/algoritma-penjadwalan-proses-150977782/150977782

8. Algoritma FCFS & SJF: Waktu Tunggu | PDF https://id.scribd.com/document/332540969/Menghitung-Average-Waiting-Time-Dalam-Algoritma-Penjadwalan-Proses-First-Come-First-Served

9. Sistem Operasi: Penjadwalan CPU https://translate.google.com/translate?u=https%3A%2F%2Fwww.cs.uic.edu%2F~jbell%2FCourseNotes%2FOperatingSystems%2F6_CPU_Scheduling.html&hl=id&sl=en&tl=id&client=srp


---

## Langkah Praktikum

1. Siapkan Data Proses
   Gunakan tabel proses berikut sebagai contoh (boleh dimodifikasi dengan data baru):
   | Proses | Burst Time | Arrival Time |
   |:--:|:--:|:--:|
   | P1 | 6 | 0 |
   | P2 | 8 | 1 |
   | P3 | 7 | 2 |
   | P4 | 3 | 3 |

2. First Come First Served
   - Urutkan proses berdasarkan *Arrival Time*.  
   - Hitung nilai berikut untuk tiap proses:
     ```
     Waiting Time (WT) = waktu mulai eksekusi - Arrival Time
     Turnaround Time (TAT) = WT + Burst Time
     ```
   - Hitung rata-rata Waiting Time dan Turnaround Time.  
   - Buat Gantt Chart sederhana:  
     ```
     | P1 | P2 | P3 | P4 |
     0    6    14   21   24
     ```

3. Shortest Job First
   - Urutkan proses berdasarkan *Burst Time* terpendek (dengan memperhatikan waktu kedatangan).  
   - Lakukan perhitungan WT dan TAT seperti langkah sebelumnya.  
   - Bandingkan hasil FCFS dan SJF pada tabel berikut:

     | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
     |------------|------------------|----------------------|------------|-------------|
     | FCFS | ... | ... | Sederhana dan mudah diterapkan | Tidak efisien untuk proses panjang |
     | SJF | ... | ... | Optimal untuk job pendek | Menyebabkan *starvation* pada job panjang |

4. Visualisasi Spreadsheet (Opsional)
   - Gunakan Excel/Google Sheets untuk membuat perhitungan otomatis:
     - Kolom: Arrival, Burst, Start, Waiting, Turnaround, Finish.
     - Gunakan formula dasar penjumlahan/subtraksi.

5. Analisis
   - Bandingkan hasil rata-rata WT dan TAT antara FCFS & SJF.  
   - Jelaskan kondisi kapan SJF lebih unggul dari FCFS dan sebaliknya.  
   - Tambahkan kesimpulan singkat di akhir laporan.


---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
Belajar menghitung FCFS dan SJF
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)
![Screenshot hasil](screenshots/Screenshot%202025-11-02%201958555.png)
---

## Analisis

1. Data Proses  
| Proses | Burst Time | Arrival Time |  
|:------:|:----------:|:------------:|  
| P1     | 6          | 0            |  
| P2     | 8          | 1            |  
| P3     | 7          | 2            |  
| P4     | 3          | 3            |  



2. First Come First Served (FCFS)

- Urutkan berdasarkan Arrival Time: P1, P2, P3, P4  
- Gantt Chart:
```bash
 | P1 | P2 | P3 | P4 |  
 0    6    14   21   24  
 ```

| Proses | Arrival | Burst | Start | Waiting Time (WT) | Turnaround Time (TAT) |  
|--------|---------|-------|-------|-------------------|-----------------------|  
| P1     | 0       | 6     | 0     | 0 - 0 = 0         | 0 + 6 = 6             |  
| P2     | 1       | 8     | 6     | 6 - 1 = 5         | 5 + 8 = 13            |  
| P3     | 2       | 7     | 14    | 14 - 2 = 12       | 12 + 7 = 19           |  
| P4     | 3       | 3     | 21    | 21 - 3 = 18       | 18 + 3 = 21           |  

- Rata-rata Waiting Time = (0 + 5 + 12 + 18) / 4 = 8.75  
- Rata-rata Turnaround Time = (6 + 13 + 19 + 21) / 4 = 14.75  


3. Shortest Job First (SJF) Non-preemptive

- Proses dipilih berdasarkan Burst Time terpendek yang sudah tersedia (memperhatikan Arrival Time):  
  Jalannya:  
  - Waktu 0: P1 (6) → eksekusi 0-6  
  - Waktu 6: P2, P3, P4 sudah tersedia; pilih P4 (3) → eksekusi 6-9  
  - Waktu 9: P2 (8) dan P3 (7); pilih P3 (7) → eksekusi 9-16  
  - Waktu 16: P2 (8) akhir → eksekusi 16-24.

- Gantt Chart: 
```bash
  | P1 | P4 | P3 | P2 |   
  0    6    9    16   24  
  ```

| Proses | Arrival | Burst | Start | WT = Start - Arrival | TAT = WT + Burst |  
|--------|---------|-------|-------|----------------------|------------------|  
| P1     | 0       | 6     | 0     | 0 - 0 = 0            | 0 + 6 = 6        |  
| P4     | 3       | 3     | 6     | 6 - 3 = 3            | 3 + 3 = 6        |  
| P3     | 2       | 7     | 9     | 9 - 2 = 7            | 7 + 7 = 14       |  
| P2     | 1       | 8     | 16    | 16 - 1 = 15          | 15 + 8 = 23      |  

- Rata-rata Waiting Time = (0 + 3 + 7 + 15) / 4 = 6.25  
- Rata-rata Turnaround Time = (6 + 6 + 14 + 23) / 4 = 12.25  


4. Perbandingan FCFS dan SJF  

| Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan                         | Kekurangan                      |  
|-----------|------------------|---------------------|----------------------------------|--------------------------------|  
| FCFS      | 8.75             | 14.75               | Sederhana dan mudah diterapkan   | Tidak efisien untuk proses panjang, waktu tunggu bisa lama  |  
| SJF       | 6.25             | 12.25               | Optimal untuk job pendek          | Bisa menyebabkan starvation pada job panjang               |  



5. Analisis & Kesimpulan

- SJF menghasilkan rata-rata waktu tunggu dan turnaround lebih rendah dibanding FCFS pada data ini, artinya lebih efisien meminimalkan waktu keseluruhan proses menunggu dan selesai.
- FCFS sederhana tapi bisa menyebabkan penundaan besar untuk proses yang datang kemudian tapi memiliki burst time kecil karena harus menunggu proses panjang yang datang lebih awal.
- SJF unggul jika waktu burst bisa diperhitungkan dan sistem ingin optimasi efisiensi, namun rawan starvation pada pekerjaan panjang.
- Pemilihan algoritma tergantung karakteristik aplikasi dan sistem; FCFS lebih cocok untuk sistem dengan proses yang memiliki burst time seragam dan kedatangan reguler, SJF cocok untuk sistem yang menginginkan efisiensi maksimum dan dapat mengestimasi burst time.

TUGAS

Data Proses  
| Proses | Burst Time | Arrival Time |  
|:------:|:----------:|:------------:|  
| P1     | 6          | 0            |  
| P2     | 8          | 1            |  
| P3     | 7          | 2            |  
| P4     | 3          | 3            |  


1. Skenario FCFS (First Come First Served)

- Urutan proses berdasarkan Arrival Time: P1, P2, P3, P4
- Gantt Chart: | P1 | P2 | P3 | P4 |  
  Waktu: 0    6    14   21   24  

| Proses | Waktu Mulai | Waktu Tunggu (WT) | Turnaround Time (TAT) |  
|:-------:|:------------:|:-----------------:|:---------------------:|  
| P1      | 0            | 0 - 0 = 0       | 6 - 0 = 6             |  
| P2      | 6            | 6 - 1 = 5       | 14 - 1 = 13           |  
| P3      | 14           | 14 - 2 = 12     | 21 - 2 = 19           |  
| P4      | 21           | 21 - 3 = 18     | 24 - 3 = 21           |  

Rata-rata WT = (0 + 5 + 12 + 18) / 4 = 8.75
Rata-rata TAT = (6 + 13 + 19 + 21) / 4 = 14.75


2. Skenario SJF (Shortest Job First, Non-preemptive)

- Urutan proses berdasarkan Burst Time terpendek dengan memperhatikan waktu kedatangan:
- Proses dieksekusi sebagai berikut:
  - Waktu 0: P1 (6) → selesai 6
  - Waktu 6: P4 (3) karena yang tersedia adalah P2 dan P3, tetapi P4 adalah yang paling kecil (3) → selesai 9
  - Waktu 9: P3 (7) → selesai 16
  - Waktu 16: P2 (8) → selesai 24

- Gantt Chart: | P1 | P4 | P3 | P2 |  
  Waktu: 0    6    9    16   24

| Proses | Waktu Mulai | WT = Mulai - Arrival | TAT = WT + Burst |  
|:-------:|:------------:|:---------------------:|:----------------:|  
| P1     | 0            | 0 - 0 = 0            | 6 - 0 = 6       |  
| P4     | 6            | 6 - 3 = 3            | 9 - 3 = 6       |  
| P3     | 9            | 9 - 2 = 7            | 16 - 2 = 14     |  
| P2     | 16           | 16 - 1 = 15          | 24 - 1 = 23     |

Rata-rata WT = (0 + 3 + 7 + 15) / 4 = 6.25
Rata-rata TAT = (6 + 6 + 14 + 23) / 4 = 12.25



3. Tabel Perbandingan Hasil

| Algoritma | Rata-rata Waiting Time | Rata-rata Turnaround Time | Kelebihan                                   | Kekurangan                                        |  
|:-----------|:------------------------:|:------------------------:|:-------------------------------------------|:--------------------------------------------------|  
| FCFS       | 8.75                     | 14.75                    | Sederhana dan mudah diimplementasikan     | Tidak efisien jika proses panjang datang duluan |  
| SJF        | 6.25                     | 12.25                    | Optimal untuk proses pendek                 | Rawan starvation proses panjang                |


 4. Analisis Singkat
- SJF lebih unggul karena menghasilkan waktu tunggu dan waktu penyelesaian yang lebih rendah, cocok untuk sistem yang ingin efisiensi maksimum.
- FCFS lebih simpel dan adil berdasarkan urutan kedatangan, tetapi sering menyebabkan antrian panjang dan waktu tunggu yang lama jika ada proses besar terlebih dahulu.

---

## Kesimpulan

1. Algoritma SJF lebih efisien daripada FCFS dalam mengurangi rata-rata waktu tunggu (waiting time) dan waktu penyelesaian (turnaround time) proses, sehingga meningkatkan performa sistem secara keseluruhan.

2. FCFS lebih sederhana dan adil karena mengikuti urutan kedatangan proses, namun berpotensi menyebabkan penundaan signifikan (konvoi effect) jika ada proses dengan waktu eksekusi lama yang datang lebih dulu.

3. Pemilihan algoritma penjadwalan harus disesuaikan dengan karakteristik beban kerja dan tujuan sistem operasi, dengan SJF cocok untuk proses dengan durasi beragam yang memerlukan efisiensi maksimum, sementara FCFS cocok untuk aplikasi dengan proses yang lebih seragam dan kedatangan berurutan.

Kesimpulan ini sesuai dengan teori dasar pengelolaan sumber daya oleh kernel OS yang melakukan penjadwalan CPU melalui system call untuk memaksimalkan utilisasi CPU, dan implementasi algoritma ini dapat berbeda di tiap kernel OS seperti Linux dan Windows karena perbedaan arsitektur dan kebijakan manajemen proses.

---

## Quiz
1. [Apa perbedaan utama antara FCFS dan SJF?]  

   Perbedaan utama antara FCFS dan SJF terletak pada kriteria penjadwalannya: FCFS menjalankan proses berdasarkan urutan kedatangan (arrival time) tanpa memandang durasi proses, sedangkan SJF menjalankan proses dengan durasi eksekusi (burst time) terpendek terlebih dahulu. FCFS bersifat non-preemptive dan sederhana, sedangkan SJF bisa non-preemptive atau preemptive dan mengoptimalkan rata-rata waktu tunggu.


2. [Mengapa SJF dapat menghasilkan rata-rata waktu tunggu minimum?]  

   SJF menghasilkan rata-rata waktu tunggu minimum karena selalu memprioritaskan proses dengan waktu burst paling singkat, sehingga mengurangi idle time CPU dan meminimalkan waktu total proses menunggu dalam antrian. Dengan melayani proses pendek lebih dulu, proses panjang tidak terlalu lama menunggu yang secara matematis menurunkan rata-rata waktu tunggu.
 
3. [Apa kelemahan SJF jika diterapkan pada sistem interaktif?]  
   
   Kelemahan SJF pada sistem interaktif adalah potensi terjadinya starvation bagi proses dengan waktu burst panjang, karena proses pendek terus diprioritaskan sehingga proses panjang bisa terlambat diproses tanpa batas waktu yang jelas. Ini tidak cocok untuk sistem interaktif di mana respons waktu nyata penting dan semua proses harus mendapatkan waktu CPU secara adil

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
memahami dan belajar
- Bagaimana cara Anda mengatasinya?  
tetap mengerjakan tugas dengan tepat waktu.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
