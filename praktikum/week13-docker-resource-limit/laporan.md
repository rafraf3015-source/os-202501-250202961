
# Laporan Praktikum Minggu [X]
Topik: [Docker – Resource Limit (CPU & Memori]

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

---

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. [Pertanyaan 1]  
   **Jawaban:**  
2. [Pertanyaan 2]  
   **Jawaban:**  
3. [Pertanyaan 3]  
   **Jawaban:**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
