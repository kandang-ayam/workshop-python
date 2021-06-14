
Sampai saat ini pesan kesalahan belum lebih dari disebutkan, tetapi jika kita telah mencoba contohnya, kita mungkin telah melihat beberapa. Ada (setidaknya) dua jenis kesalahan yang dapat dibedakan: kesalahan sintaks dan pengecualian.
A.	Kesalahan Syntaks
Kesalahan sintaks, juga dikenal sebagai kesalahan penguraian, mungkin adalah jenis keluhan paling umum yang kita dapatkan saat kita masih belajar Python:
 
Pengurai mengulangi baris yang menyinggung dan menampilkan 'panah' kecil yang menunjuk ke titik paling awal di baris tempat kesalahan terdeteksi. Kesalahan ini disebabkan oleh (atau setidaknya terdeteksi pada) token sebelum panah: dalam contoh, kesalahan terdeteksi pada fungsi print(), karena titik dua ( ':') tidak ada sebelumnya. Nama file dan nomor baris dicetak sehingga Anda tahu ke mana harus mencari jika masukan berasal dari skrip.
B.	Pengecualian
Meskipun pernyataan atau ekspresi benar secara sintaksis, hal itu dapat menyebabkan kesalahan saat ada upaya untuk mengeksekusinya. Kesalahan yang terdeteksi selama eksekusi disebut pengecualian dan tidak fatal tanpa syarat: kita akan segera belajar bagaimana menanganinya dalam program Python. Namun, kebanyakan pengecualian tidak ditangani oleh program, dan menghasilkan pesan kesalahan seperti yang ditunjukkan di sini:
 
Baris terakhir dari pesan kesalahan menunjukkan apa yang terjadi. Pengecualian tersedia dalam berbagai jenis, dan jenisnya dicetak sebagai bagian dari pesan: jenis dalam contoh adalah ZeroDivisionError, NameErrordan TypeError. String yang dicetak sebagai tipe pengecualian adalah nama pengecualian bawaan yang terjadi. Ini benar untuk semua pengecualian bawaan, tetapi tidak harus benar untuk pengecualian yang ditentukan pengguna (meskipun ini adalah konvensi yang berguna). Nama pengecualian standar adalah pengenal bawaan (bukan kata kunci yang dipesan).
Sisa baris lainnya memberikan detail berdasarkan jenis pengecualian dan penyebabnya.
Bagian sebelumnya dari pesan kesalahan menunjukkan konteks di mana pengecualian terjadi, dalam bentuk pelacakan balik tumpukan. Secara umum, ini berisi baris sumber daftar pelacakan balik tumpukan; namun, ini tidak akan menampilkan baris yang dibaca dari input standar.
Pengecualian Bawaan mencantumkan pengecualian bawaan dan artinya.

C.	Penanganan Pengeculian
Dimungkinkan untuk menulis program yang menangani pengecualian yang dipilih. Perhatikan contoh berikut, yang meminta input pengguna sampai integer yang valid telah dimasukkan, tetapi memungkinkan pengguna untuk menginterupsi program (menggunakan Control-Catau apa pun yang didukung sistem operasi); perhatikan bahwa gangguan buatan pengguna ditandai dengan memunculkan KeyboardInterrupt pengecualian.
 
Pernyataan try bekerja sebagai berikut.:
	Pertama, klausa try (pernyataan antara kata kunci trydan except) dijalankan.
	Jika tidak ada pengecualian yang terjadi, klausa pengecualian akan dilewati dan eksekusi trypernyataan selesai.
	Jika pengecualian terjadi selama eksekusi klausa coba, klausa lainnya akan dilewati. Kemudian jika jenisnya cocok dengan pengecualian yang dinamai setelah exceptkata kunci, klausa pengecualian dijalankan, dan kemudian eksekusi dilanjutkan setelah trypernyataan tersebut.
	Jika pengecualian terjadi yang tidak cocok dengan pengecualian yang disebutkan dalam klausa pengecualian, itu akan diteruskan ke trypernyataan luar ; jika tidak ada penangan yang ditemukan, itu adalah pengecualian yang tidak tertangani dan eksekusi berhenti dengan pesan seperti yang ditunjukkan di atas.
Sebuah pernyataan try mungkin memiliki lebih dari satu kecuali klausa, untuk menentukan handler untuk pengecualian yang berbeda. Paling banyak satu penangan
akan dieksekusi. Penangan hanya menangani pengecualian yang terjadi di klausa percobaan yang sesuai, bukan di penangan lain dari pernyataan try yang sama . Klausa pengecualian dapat menyebutkan beberapa pengecualian sebagai tupel yang diberi tanda kurung, misalnya:
 
Sebuah kelas dalam klausa except kompatibel dengan pengecualian jika kelas yang sama atau kelas dasarnya (tetapi tidak sebaliknya - klausa pengecualian yang mencantumkan kelas turunan tidak kompatibel dengan kelas dasar). Misalnya, kode berikut akan mencetak B, C, D dalam urutan itu:
 
Perhatikan bahwa jika klausa pengecualian dibalik (dengan yang pertama), itu akan mencetak B, B, B - pencocokan pertama kecuali klausa dipicu.except B
Klausa pengecualian terakhir mungkin menghilangkan nama pengecualian, untuk berfungsi sebagai karakter pengganti. Gunakan ini dengan sangat hati-hati, karena mudah untuk menutupi kesalahan pemrograman yang sebenarnya dengan cara ini! Ini juga dapat digunakan untuk mencetak pesan kesalahan dan kemudian memunculkan kembali pengecualian (memungkinkan pemanggil untuk menangani pengecualian juga):
 
Pernyataan try... except memiliki opsional lain klausul , yang, ketika hadir, harus mengikuti semua kecuali klausa. Berguna untuk kode yang harus dijalankan jika klausa try tidak memunculkan eksepsi. Sebagai contoh:
 
Penggunaan elseklausa lebih baik daripada menambahkan kode tambahan ke tryklausa karena ini menghindari secara tidak sengaja menangkap pengecualian yang tidak dimunculkan oleh kode yang dilindungi oleh pernyataan try… except.
Ketika pengecualian terjadi, itu mungkin memiliki nilai terkait, juga dikenal sebagai argumen pengecualian . Kehadiran dan tipe argumen bergantung pada tipe pengecualian.
Klausa pengecualian dapat menentukan variabel setelah nama pengecualian. Variabel terikat ke contoh pengecualian dengan argumen yang disimpan di instance.args. Untuk kenyamanan, contoh pengecualian menentukan __str__()sehingga argumen dapat dicetak secara langsung tanpa harus merujuk .args. Seseorang juga dapat membuat contoh pengecualian terlebih dahulu sebelum meningkatkannya dan menambahkan atribut apa pun ke dalamnya sesuai keinginan.
 
Jika pengecualian memiliki argumen, mereka dicetak sebagai bagian terakhir ('detail') dari pesan untuk pengecualian yang tidak tertangani.
Penangan pengecualian tidak hanya menangani pengecualian jika pengecualian terjadi langsung di klausa coba, tetapi juga jika pengecualian terjadi di dalam fungsi yang dipanggil (bahkan secara tidak langsung) dalam klausa coba. Sebagai contoh:
 
D.	Meningkatkan Pengecualian
Pernyataan raise memungkinkan programmer untuk memaksa pengecualian tertentu terjadi. Sebagai contoh:
 
Satu-satunya argumen yang raisemenunjukkan pengecualian yang akan dimunculkan. Ini harus berupa contoh pengecualian atau kelas pengecualian (kelas yang diturunkan dari Exception). Jika kelas pengecualian diteruskan, itu akan secara implisit dibuat dengan memanggil konstruktornya tanpa argumen:
 
Jika kita perlu menentukan apakah pengecualian telah dimunculkan tetapi tidak bermaksud menanganinya, bentuk pernyataan raise yang lebih sederhana memungkinkan kita untuk memunculkan kembali pengecualian:
 

E.	Exceptions Chaining
Pernyataan raise memungkinkan opsional fromyang memungkinkan chaining pengecualian. Sebagai contoh:
 
Ini dapat berguna saat kita mengubah pengecualian. Sebagai contoh:
 
Rangkaian pengecualian terjadi secara otomatis saat pengecualian dimunculkan di dalam excep tatau finally bagian. Rantai pengecualian dapat dinonaktifkan dengan menggunakan idiom:from None.
 

F.	User-defined Exceptions
Program dapat memberi nama pengecualian mereka sendiri dengan membuat kelas pengecualian baru (lihat Kelas untuk lebih lanjut tentang kelas Python). Pengecualian biasanya harus diturunkan dari Exceptionkelas, baik secara langsung maupun tidak langsung.
Kelas pengecualian dapat didefinisikan yang melakukan apa pun yang dapat dilakukan kelas lain, tetapi biasanya dibuat sederhana, seringkali hanya menawarkan sejumlah atribut yang memungkinkan informasi tentang kesalahan diekstraksi oleh penangan untuk pengecualian. Saat membuat modul yang dapat memunculkan beberapa kesalahan berbeda, praktik umum adalah membuat kelas dasar untuk pengecualian yang ditentukan oleh modul itu, dan subkelas yang membuat kelas pengecualian khusus untuk kondisi kesalahan yang berbeda:
 
Sebagian besar pengecualian ditentukan dengan nama yang diakhiri dengan "Kesalahan", mirip dengan penamaan pengecualian standar.
Banyak modul standar menetapkan pengecualian mereka sendiri untuk melaporkan kesalahan yang mungkin terjadi dalam fungsi yang mereka tetapkan. Informasi lebih lanjut tentang kelas disajikan dalam Kelas bab .
G.	Defining Clean-up Actions
Pernyataan try memiliki klausul opsional lain yang dimaksudkan untuk menentukan tindakan bersih-bersih yang harus dijalankan dalam semua keadaan. Sebagai contoh:
 
Jika ada klausa finally, klausa finally tersebut akan dijalankan sebagai tugas terakhir sebelum try pernyataan selesai. The finallyklausul berjalan atau tidaknya trypernyataan menghasilkan pengecualian. Poin-poin berikut membahas kasus yang lebih kompleks ketika pengecualian terjadi:
•	Jika pengecualian terjadi selama eksekusi try klausa, pengecualian dapat ditangani oleh except klausa. Jika pengecualian tidak ditangani oleh except klausa, pengecualian dimunculkan kembali setelah finally klausa dijalankan.
•	Pengecualian dapat terjadi selama eksekusi klausa except atau else. Sekali lagi, pengecualian dimunculkan kembali setelah finallyklausa dijalankan.
•	Jika pernyataan try mencapai break, continueatau returnpernyataan, finallyklausul akan dieksekusi tepat sebelum break, continueatau return eksekusi pernyataan.
•	Jika klausa finally menyertakan return pernyataan, nilai yang dikembalikan akan menjadi nilai dari pernyataan finallyklausa return, bukan nilai dari pernyataan tryklausa return .
Contoh: 
 
Contoh yang lebih rumit:
 
Seperti yang kita lihat, klausul finally dijalankan di acara apa pun. The TypeErrormengangkat dengan membagi dua string tidak ditangani oleh exceptklausa dan karena itu kembali mengangkat setelah finally klausul telah dieksekusi.
Dalam aplikasi dunia nyata, finallyklausul berguna untuk melepaskan sumber daya eksternal (seperti file atau koneksi jaringan), terlepas dari apakah penggunaan sumber daya berhasil atau tidak.
H.	Predefined Clean-up Actions
Beberapa objek menentukan tindakan pembersihan standar yang harus dilakukan saat objek tidak lagi diperlukan, terlepas dari berhasil atau tidaknya operasi yang menggunakan objek. Perhatikan contoh berikut, yang mencoba membuka file dan mencetak isinya ke layar.
 
Masalah dengan kode ini adalah ia membiarkan file terbuka untuk waktu yang tidak ditentukan setelah bagian kode ini selesai dijalankan. Ini bukan masalah pada skrip sederhana, tetapi bisa menjadi masalah untuk aplikasi yang lebih besar. The withPernyataan memungkinkan objek seperti file yang akan digunakan dengan cara yang menjamin mereka selalu dibersihkan segera dan benar.
 
Setelah pernyataan dijalankan, file f selalu ditutup, bahkan jika terjadi masalah saat memproses baris. Objek yang, seperti file, menyediakan tindakan pembersihan standar akan menunjukkan hal ini dalam dokumentasinya.
