
# Laporan Praktikum Minggu [X]
Topik: [Manajemen File, Permission di Linux "]

---

## Identitas
- **Nama**  : [Rafi nurul fauzan]  
- **NIM**   : [250202961]  
- **Kelas** : [1IKRB]

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Contoh:  
> 
1. Menggunakan perintah `ls`, `pwd`, `cd`, `cat` untuk navigasi file dan direktori.
2. Bisa menggunakan `chmod` dan `chown` untuk manajemen hak akses file.
3. Menjelaskan hasil output dari perintah Linux dasar.
memahami sistem izin (permission), dan mendokumentasikan hasilnya dalam format laporan Git.
---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

Linux mengelola berkas dengan konsep pemilik, grup, dan hak akses (read/write/execute) untuk pemilik, grup, dan lainnya.

Perintah utama: ls -l (lihat izin), chmod (ubah izin), chown (ubah pemilik/grup), chgrp (ubah grup saja).

Izin direpresentasikan secara simbolik (contoh: -rwxr-xr-- ) atau oktal (contoh: 755).

Ada hak istimewa khusus: SUID, SGID, sticky bit.ACL memungkinkan izin lebih granular selain tiga kategori dasar.

---

## Langkah Praktikum

1. **Yang dipakai**
   Gunakan Linux (Ubuntu/WSL).
   
2. **Navigasi Sistem File**
   Jalankan perintah berikut:
   ```bash
   pwd
   ls -l
   cd /tmp
   ls -a
   ```

3. **Membaca File**
   Jalankan perintah:
   ```bash
   cat /etc/passwd | head -n 5
   ```

4. **Permission**
   Buat file baru:
   ```bash
   echo "Hello <RAFI><250202961>" > percobaan.txt
   ls -l percobaan.txt
   chmod 600 percobaan.txt
   
   ls -l percobaan.txt
   sudo chown root percobaan.txt
   ls -l percobaan.txt
   ```
   

5. **Dokumentasi**
   - Ambil screenshot hasil terminal dan simpan di:SCRENSHOT
   - Tambahkan analisis hasil pada `laporan.md`.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 3"
   git push origin main
   ```
   
---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
pwd
ls -l
cd /tmp
ls -a
cat /etc/passwd | head -n 5
echo "Hello <RAFI><250202961>" > percobaan.txt
ls -l percobaan.txt
chmod 600 percobaan.txt
ls -l percobaan.txt
sudo chown root percobaan.txt
ls -l percobaan.txt
```
---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/cd.png)
![Screenshot hasil](screenshots/chmod-echo.png)
![Screenshot hasil](screenshots/echo.png)
![Screenshot hasil](screenshots/etcpswdhead.png)
![Screenshot hasil](screenshots/pwd-ls-l.png)

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
