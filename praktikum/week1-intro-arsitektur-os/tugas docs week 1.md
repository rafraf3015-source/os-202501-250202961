
#laporan

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