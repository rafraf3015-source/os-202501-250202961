


1. Mengapa system call penting untuk keamanan OS?

System call merupakan elemen penting dalam sistem operasi modern yang berperan sebagai jembatan aman antara aplikasi di ruang pengguna (user space) dan kernel sistem operasi yang memiliki akses penuh terhadap sumber daya perangkat keras dan memori sistem. Fungsi utama system call adalah memberikan layanan yang dibutuhkan oleh aplikasi, seperti pengelolaan file, proses, dan memori, tanpa memberikan akses langsung ke bagian kernel yang rawan. Hal ini sangat penting untuk menjaga keamanan sistem operasi karena aplikasi tidak dapat mengakses perangkat keras atau data kernel secara langsung, sehingga mengurangi risiko akses ilegal, manipulasi data, atau kerusakan sistem yang dapat disebabkan oleh aplikasi yang berjalan dengan hak akses terbatas.

2. Bagaimana OS memastikan transisi user–kernel berjalan aman?

Keamanan yang diberikan oleh system call dimulai dari mekanisme proteksi mode pada CPU. Sistem operasi membedakan dua mode eksekusi utama, yaitu user mode dan kernel mode. Aplikasi berjalan di user mode dengan hak akses terbatas. Ketika sebuah aplikasi membutuhkan layanan kernel, aplikasi tersebut harus melakukan permintaan melalui system call, yang akan memicu perpindahan CPU dari user mode ke kernel mode. Selama transisi ini, sistem operasi menyimpan konteks lengkap aplikasi yang memanggil system call, termasuk register dan program counter, sehingga setelah layanan kernel selesai, aplikasi dapat dilanjutkan tanpa kehilangan data atau mengalami kerusakan. Selain itu, kernel hanya dapat mengakses memori dan sumber daya yang telah diatur oleh sistem operasi, menjaga isolasi antara kernel space dan user space. Isolasi ini memastikan keamanan sistem dengan mencegah kode di user mode mengakses atau memodifikasi data kernel secara ilegal.

System call juga melakukan validasi dan pemeriksaan keamanan atas setiap permintaan. Misalnya, ketika aplikasi ingin membuka sebuah file menggunakan system call open(), sistem operasi akan memeriksa apakah aplikasi tersebut memiliki izin akses yang sesuai sebelum membuka file. Proses serupa berlaku untuk operasi baca tulis file dengan read() dan write(), pembuatan proses baru dengan fork(), penggantian program yang dijalankan dengan exec(), dan pemetaan memori menggunakan mmap(). Semua panggilan ini dikontrol untuk memastikan bahwa kebijakan keamanan sistem ditaati sehingga tidak ada operasi yang membahayakan sistem atau proses lain.

3. Sebutkan contoh system call yang sering digunakan di Linux.

Contoh umum system call di Linux yang banyak digunakan adalah:
- open(): Membuka file atau perangkat dan mengembalikan file descriptor untuk akses lebih lanjut.
- read(): Membaca data dari file ke buffer aplikasi.
- write(): Menulis data dari buffer aplikasi ke file.
- close(): Menutup file descriptor dan membebaskan sumber daya terkait.
- fork(): Membuat proses baru dengan menduplikasi proses yang sedang berjalan.
- exec(): Menjalankan program baru dengan mengganti image proses saat ini.
- mmap(): Memetakan file atau perangkat ke memori virtual proses untuk akses yang efisien.

Selain menjaga keamanan, system call juga memfasilitasi multitasking dan komunikasi antar proses serta manajemen sumber daya secara efisien. Dengan system call, sistem operasi dapat mendukung eksekusi aplikasi yang kompleks dan beragam tanpa mengorbankan integritas dan keamanan sistem.

Secara keseluruhan, system call dan mekanisme transisi aman antara user mode dan kernel mode membentuk fondasi utama keamanan sistem operasi. Mereka memungkinkan kontrol ketat terhadap akses ke perangkat keras dan memori sistem, memastikan bahwa aplikasi hanya dapat melakukan operasi yang diizinkan, serta menjaga kestabilan sistem dari ancaman internal maupun eksternal. Tanpa mekanisme ini, sistem operasi akan rentan terhadap berbagai serangan dan kerusakan yang dapat mengganggu fungsi sistem secara keseluruhan.

Penjelasan ini merangkum konsep dan fungsi system call yang sering dibahas dalam literatur akademik dan teknis mengenai keamanan dan desain sistem operasi modern.System call adalah elemen penting dalam sistem operasi modern yang berfungsi sebagai jembatan aman antara aplikasi di ruang pengguna dengan kernel yang memiliki hak akses penuh terhadap perangkat keras dan berbagai sumber daya sistem. System call memungkinkan aplikasi untuk meminta layanan dari kernel, seperti pengelolaan file, proses, dan memori, tanpa memberikan akses langsung ke kernel. Dengan demikian, system call menjaga keamanan OS dengan mencegah aplikasi mengakses perangkat keras atau memori kernel secara langsung, yang dapat menyebabkan kerusakan sistem atau kebocoran data.

Keamanan yang dijamin oleh system call berawal dari pemisahan antara mode pengguna (user mode) dan mode kernel (kernel mode) pada CPU. Aplikasi berjalan di user mode dengan hak akses terbatas, sehingga tidak dapat langsung mengakses hardware atau data sensitif. Ketika aplikasi membutuhkan layanan kernel, system call memicu perpindahan CPU ke kernel mode secara aman melalui interrupt atau trap. OS kemudian menyimpan konteks proses aplikasi saat itu secara lengkap, termasuk register dan program counter, sehingga aplikasi dapat dilanjutkan tanpa kehilangan kondisi ketika kembali ke user mode. Isolasi ketat antara kernel space dan user space mencegah kode di user mode mengakses atau memodifikasi bagian kernel secara ilegal.

Selain itu, setiap permintaan via system call melewati proses validasi oleh kernel. Misalnya, untuk membuka file dengan system call open(), kernel akan memeriksa izin aplikasi atas file tersebut sebelum mengizinkan akses. Sistem operasi juga memeriksa parameter dan memastikan bahwa operasi yang dilakukan sesuai kebijakan keamanan. Sistem seperti ini menjaga agar aplikasi tidak dapat melakukan tindakan yang merusak sistem atau mengganggu proses lain.

Contoh system call yang sering digunakan di Linux antara lain:
- open(): membuka file dan mengembalikan file descriptor,
- read(): membaca data dari file,
- write(): menulis data ke file,
- close(): menutup file descriptor,
- fork(): membuat proses baru dengan menggandakan proses induk,
- exec(): menjalankan program baru dengan mengganti image proses yang sedang berjalan,
- mmap(): memetakan file atau perangkat langsung ke memori virtual proses.

System call ini tidak hanya menjaga keamanan tetapi juga memungkinkan manajemen multitasking, komunikasi antar proses, serta pengalokasian sumber daya yang efisien dan aman.

Secara keseluruhan, system call dan mekanisme transisi user–kernel yang terproteksi membentuk fondasi utama keamanan sistem operasi modern. Mereka menjamin bahwa akses ke perangkat keras dan memori sistem dilakukan secara terkendali dan diawasi, sehingga melindungi sistem dari akses ilegal atau penyalahgunaan oleh aplikasi. Tanpa system call dan mekanisme proteksi ini, OS akan rentan terhadap kerusakan dan serangan yang dapat mengganggu stabilitas dan keamanan sistem secara keseluruhan.

Sumber:
https://id.scribd.com/document/787630166/SYSTEM-CALLS-23A-KELOMPOK-3
https://id.scribd.com/doc/196387080/System-Call
https://translate.google.com/translate?u=https%3A%2F%2Fphoenixnap.com%2Fkb%2Fsystem-call&hl=id&sl=en&tl=id&client=srp
https://thesolidsnake.wordpress.com/2013/12/04/system-call-di-windows/
https://translate.google.com/translate?u=https%3A%2F%2Fwww.ionos.com%2Fdigitalguide%2Fserver%2Fknow-how%2Fwhat-are-system-calls%2F&hl=id&sl=en&tl=id&client=srp
https://translate.google.com/translate?u=https%3A%2F%2Fwww.theknowledgeacademy.com%2Fblog%2Fsystem-calls-in-os%2F&hl=id&sl=en&tl=id&client=srp
https://translate.google.com/translate?u=https%3A%2F%2Fwww.lenovo.com%2Fca%2Fen%2Fglossary%2Fwhat-is-system-call%2F&hl=id&sl=en&tl=id&client=srp
https://translate.google.com/translate?u=https%3A%2F%2Fjumpcloud.com%2Fit-index%2Fwhat-is-a-system-call&hl=id&sl=en&tl=id&client=srp
https://repository.unimal.ac.id/4073/1/BUKU%20sistem%20operasi%20PDF.pdf
https://translate.google.com/translate?u=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FSystem_call&hl=id&sl=en&tl=id&client=srp