
# Laporan Praktikum Minggu [X]
Topik: [Arsitektur Sistem Operasi]

---

## Identitas
- **Nama**  : [Rafi nurul fauzan]  
- **NIM**   : [250202961]  
- **Kelas** : [1IKRB]

---

## Tujuan
mengenal kernel, mempelajari arsitektur dasar sistem operasi,mampu membuat diagram di draw.oi dan linux.  
---

## Dasar Teori
- Sistem Operasi sebagai Pengelola Sumber Daya adalah Sistem operasi berfungsi sebagai pengelola sumber daya sistem, seperti memori, CPU, dan perangkat keras lainnya.
- Kernel sebagai Inti Sistem Operasi: Kernel adalah inti sistem operasi yang mengelola sumber daya sistem dan menyediakan layanan ke aplikasi.
- System Call sebagai Antarmuka: System call adalah antarmuka antara aplikasi dan kernel yang memungkinkan aplikasi membuat permintaan ke kernel.
- Arsitektur Sistem Operasi adalah Sistem operasi dapat memiliki beberapa model arsitektur, seperti monolithic kernel, microkernel, dan layered architecture.
- Komponen Sistem Operasi adalah Sistem operasi memiliki beberapa komponen, seperti device driver, file system, dan process management, yang bekerja sama untuk mengelola sumber daya sistem dan menyediakan layanan ke aplikasi.

## Langkah Praktikum
1. install viscode,gitbash,ubuntu
2. buat akun github
3. fork akun 
4. kasih nama dan clone dengan cara git clone link
5. untuk up klik kanan, klik terminal lalu ketik
6. git add . git commit -m "kata kata" git push -u origin main 
7. untuk linux ada syarat syaratnya 
8. os bulid 18362 ke atas
9. setting, lalu cari update lalu update semua nya
10. setting, lalu cari developer settings dan nyalakan developer mode
11. setting, lalu cari turn windows feature dan cari windowsubsystem for linux
12. dan juga virtual machine platfrom centang dua duanya lalu restart 
13. lalu cari cmd di windows lalu commend wsl
14. cek versi ketik wsl --version pastikan versi nya 2
15. untuk melihat distribusi linux ketik wsl --list --online
16. lalu buka ubuntu masukan username dan pasword
17. jika sudah nanti ada tulisan install succesful
18. lalu ke cmd ketik wsl --list --verbose pastikan version nya 2
19. untuk kembali ke akun mu ketik wsl
20. lalu untuk mengetahui versi ubuntu ketik lsb_release -a
21. untuk mengakses keseluruhan sistem nya di akses root ketik sudo su
22. lalu ketik apt update && apt full-upgrade -y
23. tunggu sabar sampai selesai dan sudah done
24. cari cmd di windows lalu ketik wsl
25. ketik seusai tugas uname -a, ismod | head, dmesg | head 
26. ada yang ketinggalan pastikan sebelum commit&push sudah git config --global user.name "Nama Anda" , git config --global user.email "email@contoh.com"
26. dan buatlah diagram di draw.oi
27. ketika semua sudah susun didalam file
28. lalu up ke github fork


---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a (code/uname-a.txt)

Linux LAPTOP-9I8L620V 6.6.87.2-microsoft-standard-WSL2 #1 SMP PREEMPT_DYNAMIC Thu Jun  5 18:30:46 UTC 2025 x86_64 x86_64 x86_64 GNU/Linux

lsmod | head (code/lsmodhead.txt)

Module                  Size  Used by
intel_rapl_msr         16384  0
intel_rapl_common      32768  1 intel_rapl_msr
kvm_amd               126976  0
kvm                   970752  1 kvm_amd
irqbypass              12288  1 kvm
battery                20480  0
crc32c_intel           16384  0
ac                     16384  0
sch_fq_codel           16384  1

dmesg | head   (code/dmesghead.txt)

[    0.000000] Linux version 6.6.87.2-microsoft-standard-WSL2 (root@439a258ad544) (gcc (GCC) 11.2.0, GNU ld (GNU Binutils) 2.37) #1 SMP PREEMPT_DYNAMIC Thu Jun  5 18:30:46 UTC 2025
[    0.000000] Command line: initrd=\initrd.img WSL_ROOT_INIT=1 panic=-1 nr_cpus=8 hv_utils.timesync_implicit=1 console=hvc0 debug pty.legacy_count=0 WSL_ENABLE_CRASH_DUMP=1
[    0.000000] KERNEL supported cpus:
[    0.000000]   Intel GenuineIntel
[    0.000000]   AMD AuthenticAMD
[    0.000000] BIOS-provided physical RAM map:
[    0.000000] BIOS-e820: [mem 0x0000000000000000-0x000000000009ffff] usable
[    0.000000] BIOS-e820: [mem 0x00000000000e0000-0x00000000000e0fff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000000100000-0x00000000001fffff] ACPI data
[    0.000000] BIOS-e820: [mem 0x0000000000200000-0x00000000e8dfffff] usable


```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/tugasweek1.png)
![Screenshot hasil](screenshots/code.png)

---

## Analisis


- jelaskan makna hasil percobaan


1. uname -a

uname -a menampilkan informasi tentang sistem operasi dan kernel yang sedang berjalan. Hasilnya:

- Nama sistem operasi (Linux)
- Versi kernel (misalnya 5.10.102.1-microsoft-standard-WSL2)
- Arsitektur prosesor (x86_64)
- Tipe prosesor (x86_64)
- Tipe sistem (GNU/Linux)

Hasil ini memberitahu bahwa kernel Linux yang sedang berjalan adalah kernel yang disediakan oleh Microsoft, yang dioptimalkan untuk berjalan di atas Windows (WSL).

2. lsmod | head

lsmod menampilkan daftar modul kernel yang sedang dimuat. Hasilnya menunjukkan beberapa modul kernel yang sedang dimuat, seperti:

- Modul kernel untuk mengelola perangkat keras (misalnya nvidia, intel)
- Modul kernel untuk mengelola sistem file (misalnya ext4,fuse)
- Modul kernel untuk mengelola jaringan (misalnya tcp, udp)

ini menunjukkan kernel Linux memiliki kemampuan untuk memuat modul kernel secara dinamis untuk mengelola berbagai aspek sistem operasi.

3. dmesg | head

dmesg menampilkan log kernel yang berisi informasi tentang proses boot dan kejadian sistem. Hasilnya menunjukkan beberapa informasi tentang:

- Proses boot kernel
- Deteksi perangkat keras
- Inisialisasi sistem file
- Inisialisasi jaringan

Hasil ini menunjukkan kernel Linux memiliki kemampuan untuk mengelola proses boot dan kejadian sistem, serta menyediakan log untuk debugging dan analisis.



- Hubungan dengan teori


Hasil percobaan menunjukkan beberapa aspek penting dari kernel Linux:

- Fungsi kernel: Kernel Linux memiliki fungsi untuk mengelola sumber daya sistem, seperti memori, CPU, dan perangkat keras.
- System call: Kernel Linux menyediakan system call untuk aplikasi untuk berinteraksi dengan kernel dan mengelola sumber daya sistem.
- Arsitektur OS: Kernel Linux memiliki arsitektur yang modular, dengan kemampuan untuk memuat modul kernel secara dinamis untuk mengelola berbagai aspek sistem operasi.




- Perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)


Hasil percobaan di atas menunjukkan beberapa perbedaan antara Linux dan Windows:

- Kernel Linux memiliki kemampuan untuk memuat modul kernel secara dinamis, sedangkan Windows memiliki kernel yang lebih monolitik.
- Linux memiliki sistem file yang lebih fleksibel dan dapat di-custom, sedangkan Windows memiliki sistem file yang lebih terstruktur dan terbatas.
- Linux memiliki kemampuan untuk mengelola jaringan yang lebih luas dan dapat di-custom, sedangkan Windows memiliki kemampuan jaringan yang lebih terbatas.

tapi perbedaan antara Linux dan Windows tidak hanya terletak pada kernel, tetapi juga pada aplikasi, sistem file, dan arsitektur sistem operasi secara keseluruhan. 

---

## Kesimpulan
Kernel Linux memiliki kemampuan yang luar biasa dalam mengelola sumber daya sistem, seperti memori, CPU, dan perangkat keras. linux lebih cocok bagi mereka yang ingin mengontrol sistem operasinya dan memiliki kemampuan untuk mengelola jaringan yang lebih luas.

jangan menanggap kita paling tau semuanya karena itu lah sebuah penyakit bagi ilmu pengetahuan.





**mengenal microkernel,monolitik dan layered architecture**

*Apa itu Micro-Kernel*

Kernel mengelola operasi komputer. Dalam mikrokernel , layanan pengguna dan layanan kernel diimplementasikan dalam ruang alamat yang berbeda. Layanan pengguna berada di ruang alamat pengguna, dan layanan kernel berada di bawah ruang alamat kernel.

Mikrokernel adalah pendekatan minimalis untuk merancang sistem operasi. Dalam arsitektur mikrokernel, hanya fungsi-fungsi terpenting yang disertakan dalam kernel, seperti komunikasi dasar antara perangkat keras dan perangkat lunak, serta manajemen proses yang sederhana. Layanan lain seperti driver perangkat, sistem berkas, dan protokol jaringan dijalankan di ruang pengguna sebagai proses terpisah.

Keuntungan Mikro-Kernel

1. Ukuran Micro-Kernel lebih kecil, sehingga mudah digunakan.
2. Mudah untuk memperluas Mikro-Kernel
3. Mudah untuk di-porting Micro-Kernel
Mikro-Kernel lebih kecil kemungkinannya mengalami kesalahan dan bug. Salah satu contohnya adalah Mac OS.

Kekurangan Mikro-Kernel

1. Eksekusi Micro-Kernel lebih lambat.
2. Hanya layanan yang paling penting saja yang ada di dalam kernel, sedangkan layanan sistem operasi lainnya ada di dalam program aplikasi sistem.
3. Komunikasi antara proses klien & layanan yang berjalan di ruang alamat pengguna dibuat melalui pesan yang selanjutnya mengurangi kecepatan eksekusi.


*Apa itu Kernel Monolitik*

Dalam kernel Monolitik , seluruh sistem operasi berjalan sebagai satu program dalam mode kernel. Layanan pengguna dan layanan kernel diimplementasikan dalam ruang alamat yang sama.

Kernel monolitik adalah jenis arsitektur sistem operasi di mana seluruh sistem operasi, termasuk fungsi-fungsi inti seperti manajemen memori, manajemen proses, driver perangkat, dan sistem berkas, terintegrasi ke dalam satu blok kode besar yang berjalan dalam satu ruang alamat. Desain ini dapat mempercepat sistem karena semua komponen dapat berinteraksi secara langsung, tetapi juga dapat membuat sistem lebih kompleks dan lebih sulit dipelihara, karena bug di satu bagian kernel berpotensi memengaruhi seluruh sistem.

Keuntungan Kernel Monolitik

1. Kernel Monolitik merupakan kesatuan utuh di mana layanan pengguna dan layanan kernel diimplementasikan di bawah ruang alamat yang sama.
2. Ia memiliki kecepatan eksekusi yang lebih cepat.
3. Salah satu contohnya adalah Linux. Desainnya sederhana dan performanya sangat tinggi.

Kekurangan Kernel Monolitik

1. Kernel monolitik memiliki ukuran yang lebih besar karena layanan pengguna & layanan kernel diimplementasikan dalam ruang yang sama.
2. Karena ukurannya lebih besar, Kernel Monolitik menjadi sulit untuk diperluas.
3. Sulit untuk mengekspor dan mem-porting kernel monolitik
4. Berbeda dengan kernel mikro, kernel Monolitik lebih rentan terhadap kesalahan dan bug. Akibatnya, sistem mengalami lebih banyak kesalahan daripada kernel biasa.

*apa itu layered architecture*

Layered Architecture adalah pendekatan desain sistem operasi yang membagi fungsi OS menjadi beberapa lapisan, dengan tiap lapisan masing-masing memiliki fungsinya sendiri.

Keuntungan Arsitektur Berlapis

1. Desain Sistem yang Modular dan Terorganisir = sistem lebih mudah dipahami, dikembangkan, dan diuji.
2. Isolasi Kesalahan = kesalahan di satu lapisan tidak akan langsung mempengaruhi setiap lapisan.
3. Pemeliharaan yang Lebih Mudah = perubahan pada satu lapisan memungkinkan lapisan lain berfungsi tanpa modifikasi.

Kerugian Arsitektur Berlapis

1. Keterlambatan = waktu yang dibutuhkan untuk mengeksekusi tugas meningkat karena komunikasi antar lapisan.
2. Desain yang Sulit di Awal = setiap lapisan harus didefinisikan untuk menghindari tumpang tindih fungsi, yang menantang.
3. Kurang Fleksibilitas = jika aplikasi memerlukan akses langsung ke perangkat keras, hal itu dapat dibatasi oleh aturan lapisan.



**-perbedaan monolithic kernel, microkernel, dan layered architecture**

Struktur  

Kernel Monolitik = Semua layanan OS dalam satu kernel besar  
Mikrokernel = Hanya fungsi inti dalam kernel, layanan lainnya di ruang pengguna  
Arsitektur Berlapis = OS dibagi menjadi beberapa lapisan bertingkat  

Contoh OS  

Kernel Monolitik = Linux, Unix, MS-DOS  
Mikrokernel = Minix, QNX, macOS (semi)  
Arsitektur Berlapis = THE OS, OS/2, beberapa UNIX  

Performa  

Kernel Monolitik = Cepat dan efisien  
Mikrokernel = Lebih lambat karena lebih banyak komunikasi IPC  
Arsitektur Berlapis = Dapat lambat karena harus melewati setiap lapisan  

Keamanan  

Kernel Monolitik = Rendah, bug dapat mempengaruhi seluruh sistem  
Mikrokernel = Tinggi, layanan terisolasi  
Arsitektur Berlapis = Sedang, tergantung pada desain lapisan  

Pemeliharaan  

Kernel Monolitik = Sulit karena kode yang besar dan kompleks  
Mikrokernel = Mudah karena modularitas  
Arsitektur Berlapis = Mudah karena setiap lapisan bersifat independen  

Kerumitan Desain  

Kernel Monolitik = Sedang  
Mikrokernel = Tinggi  
Arsitektur Berlapis = Tinggi, harus jelas fungsi dari setiap lapisan



**-Contoh OS nyata yang menggunakan masing-masing model**

1. PC DOS (Personal Computer Disk Operating System)
Sistem operasi ini merupakan sistem operasi yang paling banyak dipakai sebelum munculnya sistem operasi windows buatan Microsoft. Sistem operasi ini dibuat oleh Microsoft untuk mesin IBM. IBM mengedarkan PC DOS bersama dengan komputer yang dijualnya.

2. MS DOS (Microsoft Disk Operating System)
Sistem operasi ini merupakan kembaran dan versi lain PC DOS yang dikeluarkan oleh Microsoft.

3. OS/2 (Operating System 2)
Sistem operasi ini merupakan kelanjutan dari PC DOS dan MS DOS yang dibuat untuk keluarga komputer PS/2. Sistem Operasi ini didesain agar dapat menggunakan kemampuan penuh Mikroprosessor Intel 80286, termasuk di antaranya adalah modus terproteksi.
Selain itu mampu menjalankan tugas secara simultan, serta mendukung memori virtual, dengan tetap mempertahankan kompatibilitas dengan banyak perangkat lunak MS-DOS yang beredar saat itu.

4. UNIX
Sistem operasi ini pada mulanya hanya diperuntukkan bagi komputer-komputer besar. Namun oleh AT&T Bell Laboratory digunakan pula untuk PC. Sistem operasi ini ditulis dalam bahasa pemograman C.
UNIX didesain sebagai sistem operasi yang portabel, multi-tasking dan multi-user. Sistem operasi UNIX lebih menekankan diri pada workstation dan srver,

5. XENIX
XENIX merupakan kembaran dari UNIX yang dikeluarkan oleh Microsoft dan digunakan pada IBM PC/AT.

6. AIX (Advance Interactive Executive)
AIX merupakan kembaran lainnya dari UNIX yang dikeluarkan oleh IBM. AIX pertama kali diciptakan untuk mendukung secara penuh RT-PC. AIX juga dapat dioperasikan dalam komputer keluarga PS/2.

7. Mirosoft Windows
Dengan munculnya microsoft windows, sistem operasi DOS mulai banyak ditinggalkan. Sistem operasi ini mengalami perkembangan begitu pesat dikarenakan sistem operasi ini memberikan fasilitas yang lebih mudah dipakai oleh pengguna.
Pemakaiannya sudah berbasiskan pada grafik sehingga penggunanya tidak perlu mengetikkan berapa perintah untuk berinteraksi dengan komputer. Pengguna cukup menggunakan mouse untuk mengoperasikan komputernya.

8. Linux
Sistem operasi ini merupakan turunan dari UNIX. Dikembangkan oleh seorang mahasiswa Finlandia, Linus Torvalds. Sistem operasi ini pada awalnya masih berbasiskan teks, dan kemudian mulai menggunakan tampilan berbasiskan grafik.



**-Analisis: model mana yang paling relevan untuk sistem modern?**

Kernel Monolitik

Relevan untuk server & superkomputer.

Misalnya, Linux mendukung Android, server web, cloud, superkomputer.
Keuntungan: cepat, efisien, stabil untuk beban kerja berat.
Kerugian: kompleks & bug dapat membuat seluruh sistem down.

Mikrokernel

Relevan untuk sistem waktu nyata & perangkat tertanam.
Contoh: QNX (di mobil, pesawat terbang), Minix, dan bagian dari macOS/iOS.
Keuntungan: sistem yang aman, modular, dan ideal untuk situasi yang memerlukan keandalan sistem tinggi.
Kerugian: kinerja lebih rendah karena overhead komunikasi antara layanan yang terisolasi.

Arsitektur Berlapis

Lebih sesuai untuk teori dan pendidikan, jarang digunakan secara murni dalam sistem modern.
Namun, konsep "pelapisan" masih digunakan di banyak sistem operasi modern untuk modularitas.
Contoh: Windows NT menggabungkan pelapisan dengan kernel hibrida.


Kesimpulan

Model yang paling relevan untuk sistem modern adalah Kernel Hibrida
Karena menggabungkan kecepatan kernel monolitik dan keamanan mikrokernel

apa itu hybridkernel 
Hybrid Kernel adalah jenis yang merupakan campuran dari Monolithic Kernel dan Microkernel.

Contoh dalam kehidupan nyata:
Windows NT/10/11 → kernel hibrida
macOS & iOS → XNU (semi-mikrokernel)



*SUMBER* =
https://www.geeksforgeeks.org/operating-systems/difference-between-microkernel-and-monolithic-kernel/

https://kumparan.com/ragam-info/8-contoh-sistem-operasi-yang-biasa-digunakan-pada-komputer-211u4469u9H/full

https://www.sekawanmedia.co.id/blog/apa-itu-kernel/



---

## Quiz
1. [sebutkan tiga fungsi utama sistem operasi.]  
   **mengelola dan mengatur perangkat keras komputer,menyediakan layanan,mengelola sumberdaya seperti CPU,memori dan output,input**  
2. [jelaskan perbedaan antara kernel mode dan usermode]  
   **mode kernel adalah mode sistem operasi memiliki akses penuh kesemua intruksi mode user adalah mode dengan hak terbatas dibatasi agar tidak merusak sistem**  
3. [Sebutkan contoh OS dengan arsitektur monolithic dan mikrokernel.]  
   **monolitic kernel : linux,BSD,OS/360VMX, microkernel : QNX,Symbian, L4 Linux**  

---

## Refleksi Diri
Tuliskan secara singkat:
- mengoprasikan linux sangat menantang karna berpotensi merusak laptop   
- dan cara mengatasi nya dengan melihat versi laptop dan ubuntu   

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_

_https://course-net.com/blog/pengertian-sistem-operasi-dan-arsitektur-komputer/_


