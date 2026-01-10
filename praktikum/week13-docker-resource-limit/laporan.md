
# Laporan Praktikum Minggu [X]
Topik: [Docker – Resource Limit (CPU & Memori)]

---

## Identitas
- **Nama**  : [Rafi nurul fauzan]  
- **NIM**   : [(250202961)]  
- **Kelas** : [1IKRB]

---

## Tujuan
1. Membuat **Dockerfile sederhana** untuk menjalankan aplikasi/skrip.
2. Menjalankan container dengan **pembatasan resource** (CPU dan memori).
3. Mengamati dampak pembatasan resource melalui output program dan monitoring sederhana.

---

## Dasar Teori
Control Groups (Cgroups)
Kernel Linux memanfaatkan cgroups untuk membagi dan membatasi resource proses. Docker menggunakan --cpus dan --memory via cgroup v1/v2 untuk mengalokasikan resource host secara proporsional antar container.

Pembatasan CPU (CFS Scheduler)
Opsi --cpus="0.5" membatasi container pada 50% kapasitas CPU host melalui Completely Fair Scheduler. Container mendapat jatah waktu CPU terbatas, sehingga loop komputasi berat melambat signifikan.


Batas Memori & OOM Killer
Parameter --memory="256m" menetapkan batas keras memori; ketika alokasi melebihi limit, kernel memicu OOM Killer. Program tes gagal dengan MemoryError setelah alokasi ~250MB.


Isolasi Resource
Tiap container memiliki namespace dan cgroup sendiri, memastikan limit tidak memengaruhi container lain atau sistem host. docker stats menunjukkan statistik real-time dari cgroup.


Manfaat DevOps & Keamanan
Pembatasan resource menghalau satu container menguasai sistem (Noisy Neighbor) dan menjamin performa stabil di lingkungan multi-container.


---

## Langkah Praktikum

1. **Persiapan Lingkungan**

   - Pastikan Docker terpasang dan berjalan.
   - Verifikasi:
     ```bash
     docker version
     docker ps
     ```

2. **Membuat Aplikasi/Skrip Uji**

   Buat program sederhana di folder `code/` (bahasa bebas) yang:
   - Melakukan komputasi berulang (untuk mengamati limit CPU), dan/atau
   - Mengalokasikan memori bertahap (untuk mengamati limit memori).

3. **Membuat Dockerfile**

   - Tulis `Dockerfile` untuk menjalankan program uji.
   - Build image:
     ```bash
     docker build -t week13-resource-limit .
     ```

4. **Menjalankan Container Tanpa Limit**

   - Jalankan container normal:
     ```bash
     docker run --rm week13-resource-limit
     ```
   - Catat output/hasil pengamatan.

5. **Menjalankan Container Dengan Limit Resource**

   Jalankan container dengan batasan resource (contoh):
   ```bash
   docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit
   ```
   Catat perubahan perilaku program (mis. lebih lambat, error saat memori tidak cukup, dll.).

6. **Monitoring Sederhana**

   - Jalankan container (tanpa `--rm` jika perlu) dan amati penggunaan resource:
     ```bash
     docker stats
     ```
   - Ambil screenshot output eksekusi dan/atau `docker stats`.

7. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 13 - Docker Resource Limit"
   git push origin main
   ```

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
1. Buat Dockerfile sederhana dan program uji di folder `code/`.
2. Build image dan jalankan container **tanpa limit**.
3. Jalankan container dengan limit **CPU** dan **memori**.
4. Sajikan hasil pengamatan dalam tabel/uraian singkat di `laporan.md`.

```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)
![Screenshot hasil](screenshots/bulid%20docker.png)
![Screenshot hasil](screenshots/docker%20stats.png)
![Screenshot hasil](screenshots/run%20cpu%20memory.png)
![Screenshot hasil](screenshots/run%20docker.png)

---

## Analisis

| Aspek          | Tanpa Limit                          | Dengan Limit (--cpus=0.5 --memory=256m)          |
|----------------|--------------------------------------|--------------------------------------------------|
| CPU Test       | Selesai 60s normal (~100% CPU host)  | Lambat >120s (throttled ~50% CPU) [docker stats] |
| Memory Test    | Selesai 400MB OK                     | Crash ~250MB ("❌ MEMORY LIMIT!") OOM killer      |
| docker stats   | CPU 100%+, MEM unlimited             | CPU ~50%, MEM 256MiB/256MiB (100% lalu crash)    |
| Perilaku       | Full resource host                   | Terbatas, aman multi-container                   |



---

## Kesimpulan

Docker memungkinkan pengaturan batas CPU dan memori container agar tidak mengganggu sistem host atau container lain. Tanpa limit, container bebas pakai semua resource; dengan limit aktif, CPU dibatasi dan memori diblokir saat mencapai batas. Praktikum membuktikan Docker efektif mengisolasi resource untuk lingkungan multi-container yang stabil dan aman.

CPU Fairness - CFS quota batasi container seperti proses biasa, cegah dominasi core

Memory Safety - Hard limit + OOM killer proteksi host dari leak tak terkendali

Production Ready - Wajib untuk multi-tenant, hilangkan Noisy Neighbor problem

---

## Quiz
1. [Mengapa container perlu dibatasi CPU dan memori?]  
   Jawaban: Container perlu dibatasi untuk mencegah Noisy Neighbor problem - satu container boros resource bisa ganggu container lain dan host. Tanpa limit, container bisa pakai 100% CPU host (bottleneck semua aplikasi) dan memori unlimited (swap habis → crash sistem). Limit jamin fairness dan stabilitas multi-container environment.

2. [Apa perbedaan VM dan container dalam konteks isolasi resource?]  
   Jawaban: VM punya Guest OS terpisah dengan hypervisor yang alokasi resource statis (overhead tinggi 10-20%, boot lambat). Container share host kernel dengan isolasi process-level via cgroups+namespace (overhead <5%, boot detik). Container lebih efisien tapi butuh cgroups untuk batasi resource karena tidak ada OS boundary alami.

3. [Apa dampak limit memori terhadap aplikasi yang boros memori?]  
   Jawaban: Aplikasi coba alokasi melebihi --memory="256m" → OOM Killer potong paksa → container crash dengan MemoryError. Efeknya predictable (batas jelas) bukan host crash chaotic. Docker proaktif bunuh proses boros sebelum host kehabisan RAM, lindungi sistem keseluruhan.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  memahami materi baru yang belum di ajarkan yaitu docker 
- Bagaimana cara Anda mengatasinya? mencari tutorial di youtube atau minta bantuan teman

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
