
# Laporan Praktikum Minggu [X]
Topik: [Manajemen Proses dan User di Linux"]

---

## Identitas
- **Nama**  : [Rafi nurul fauzan]  
- **NIM**   : [250202961]  
- **Kelas** : [1IKRB]

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
- Mengelola user, group dan serta hak akses pengguna.  
- Menampilkan, menghentikan, dan mengontrol proses yang sedang berjalan. 
---

## Dasar Teori
- Sistem pengelolaan user dan grup: Linux mengelompokkan pengguna ke dalam user ID (UID) dan grup ID (GID). Setiap file dan proses memiliki kepemilikan (owner) dan grup, sehingga hak akses dapat dikendalikan secara granular melalui izin file dan ACL. Ini membantu menjaga keamanan serta pengelolaan akses secara terpusat melalui perintah seperti useradd/usermod/groupadd. [2][1]

- Hierarki hak akses dan autentikasi: Sistem menggunakan kombinasi user login, password, serta kemampuan sudo untuk memberikan hak istimewa sementara. Pengaturan sudoers memungkinkan pembatasan perintah yang bisa dijalankan sebagai root, sehingga akses administratif tidak diberikan secara langsung kepada semua pengguna. [2]

- Manajemen proses inti OS: Proses adalah unit eksekusi yang berjalan di kernel; Linux mendukung multiprogramming dan scheduling untuk membagi waktu CPU antar proses. Pemahaman dasar seperti status proses (running, sleeping, zombie), prioritas, dan penanganan I/O sangat penting untuk optimasi performa sistem. [9][7]

- Peran grup untuk manajemen hak akses: Grup memungkinkan menerapkan hak akses secara kolektif ke beberapa user tanpa menyetel izin satu per satu. Grup juga sering dipakai oleh layanan atau aplikasi (misalnya database/web server) untuk menjalankan layanan dengan hak akses yang sesuai.

sumber:

Manajemen User di Linux: Tips Aman yang Jarang Dipakai https://www.idn.id/manajemen-user-di-linux-tips-aman-yang-jarang-dipakai/

Manajemen User Linux: Perintah Penting yang Wajib Tahu https://www.idn.id/manajemen-user-linux-perintah-penting-yang-wajib-tahu/

Manajemen Paket dan User Permission di Linux - JocoDEV https://jocodev.id/manajemen-paket-dan-user-permission-di-linux/

Laporan Ke 2 Linux Command Dan User Manajemen ... https://id.scribd.com/doc/182274416/Laporan-Ke-2-Linux-Command-Dan-User-Manajemen-1107008-LUKMANUL-HAKIM-SOJ

Manajemen proses Linux dengan command line https://www.hostinger.com/id/tutorial/manajemen-proses-linux-dengan-command-line

Praktikum 4 Proses dan Manajemen Proses https://raniadwitry.blogspot.com/2020/10/blog-post.html

Analisis Manajemen Proses pada Sistem Operasi Linux https://journal.arteii.or.id/index.php/Merkurius/article/download/615/878/3305

Manajemen User dan Sistem linux - Berbagi Bersama https://irziqamdiken.wordpress.com/2012/04/18/manajemen-user-dan-sistem-linux/

Manajemen Proses Pada LINUX (Ubuntu) | PDF https://id.scribd.com/doc/309245462/Manajemen-Proses-Pada-LINUX-ubuntu

Praktikum 11 Manajemen User dan Group https://raniadwitry.blogspot.com/2020/12/praktikum-11-manajemen-user-dan-group.html

---

## Langkah Praktikum
1. gunakan linux
2. Jalankan perintah berikut:
   ```bash
   whoami
   id
   groups
   ```
   - Jelaskan setiap output dan fungsinya.  
   - Buat user baru (jika memiliki izin sudo):
     ```bash
     sudo adduser praktikan
     sudo passwd praktikan
     ```
   - Uji login ke user baru.
   ```bash
   ps aux | head -10
   top -n 1
   ```
   - Jelaskan kolom penting seperti PID, USER, %CPU, %MEM, COMMAND.

     ```bash
   sleep 1000 & ps aux | grep sleep
     ```
   - Catat PID proses `sleep`.  
   - Hentikan proses:
     ```bash
     kill <PID>
     ```
   - Pastikan proses telah berhenti dengan `ps aux | grep sleep`.

```bash
   pstree -p | head -20
   ```
   - Amati hierarki proses dan identifikasi proses induk (`init`/`systemd`).  
   - Catat hasilnya dalam laporan.

3. lalu up ke git hub 


---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
whoami
id
groups
sudo adduser praktikan
sudo passwd praktikan
ps aux | head -10
top -n 1
sleep 1000 &
 ps aux | grep sleep
kill <PID>
pstree -p | head -20

```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/whoami_id_groups_sudo_adduser_praktikan.png)
![Screenshot hasil](screenshots/sudo_passwd_praktikan.png)
![Screenshot hasil](screenshots/ps_aux_head10.png)
![Screenshot hasil](screenshots/top-n1.png)
![Screenshot hasil](screenshots/sleep%201000_&_ps_aux_repsleep.png)
![Screenshot hasil](screenshots/pstree-phead-20.png)

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
