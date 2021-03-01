Workshop Python
Minggu 03

 


Disusun Oleh :
NAMA	: Irvan Maulana
NIM	: 185410004
JURUSAN	: Teknik Informatika
JENJANG	: S1


STMIK AKAKOM
YOGYAKARTA
2021

Struktur data
List
Ada beberapa method dalam tipe data list. Antara lain sebagai berikut:
1.	list.append(x) 
Menambahkan item pada akhir list. Sama dengan a[len(a):] = [x].
2.	list.extend(itterable) 
Memperluas list dengan menambahkan semua item dari iterable. Sama dengan a[len(a):] = iterable.
3.	list.insert(i,x) 
Menyisipkan item pada posisi tertentu didalam list. Argument pertama adalah indeks elemen yang akan disisipkan, jadi menyisipkan di depan list tersebut. a.insert(len(a), x) sama dengan a.append(x).
4.	list.remove(x) 
Menghapus item yang ditunjuk x. jika item yang dimaksud tidak ada, maka akan menghasilkan valueError.
5.	list.pop([i])
Digunakan untuk menghapus elemen dalam list (oleh bawaan elemen terakhir), dan mengembalikan nilai dari elemen.
6.	list.clear() 
Menghapus semua item dari list. Sama dengan del a[:].
7.	list.index(x[,start[,end]])
Mencari posisi suatu nilai
8.	list.count(x) 
Menghitung kemunculan nilai tertentu.
9.	list.sort(*, key=None, reverse=False) 
Mengurutkan list.
10.	list.reverse() 
Membalik urutan list.
11.	list.copy()
Untuk menduplikat/menyalin list











Contoh penggunaan method:
 

Menggunakan list sebagai stack
Metode list sangat cocok digunakan untuk sebagai stack, diamana elemen terakhir yang ditambahkan adalah elemen pertama yang diambil (terakhir-keluar, masuk-pertama). Untuk menambhkan item ke atas stack, gunakan append(). Untuk mengambil item dari atas stack, gunakan pop() tanpa menulis indeks. Contoh :
 

Menggunakan list sebagai antrian.
	List juga diperuntukkan untuk antrian, di mana elemen pertama yang ditambahkan adalah elemen pertama yang diambil (pertama-masuk, pertama-keluar). Namun, list tidak efisien untuk tujuan ini. Meskipun menambahkan dan muncul dari akhir list cepat, melakukan penyisipan atau pop dari awal list akan lambat (karena semua elemen lainnya harus digeser satu per satu). Untuk mengimplementasikan antrian, gunakan collections.dequeyang dirancang untuk memiliki penambahan cepat dan muncul dari kedua ujungnya. Contoh:
 

Pemahaman list.
Pemahaman list memberikan cara yang ringkas untuk membuat list. Aplikasi umum adalah membuat list baru di mana setiap elemen adalah hasil dari beberapa operasi yang diterapkan ke setiap anggota urutan lain atau dapat diulang, atau untuk membuat rangkaian elemen yang memenuhi kondisi tertentu. Misalnya, anggap kita ingin membuat list kotak, seperti:
 

Pemahaman list terdiri dari tanda kurung yang berisi ekspresi diikuti dengan forklausa, kemudian nol atau lebih for atau if klausa. Hasilnya adalah list baru yang dihasilkan dari evaluasi ekspresi dalam konteks klausa for dan if yang mengikutinya. Misalnya, listcomp ini menggabungkan elemen dari dua list jika tidak sama:
 
Sama dengan:
 

Nested List Comprehensions
Ekspresi awal dalam pemahaman list dapat berupa ekspresi sembarang apa pun, termasuk pemahaman list lainnya. Pertimbangkan contoh matriks 3x4 berikut yang diimplementasikan sebagai list 3 list panjang 4:
 
list comprehension berikut akan mengubah baris dan kolom:
 

Seperti yang telah dijelaskan sebelumya, listcomp bersarang dievaluasi dalam konteks for yang mengikutinya, jadi contohnya sebagai berikut: 
 

Pada kenyataannya, kita harus lebih memilih fungsi bawaan daripada pernyataan aliran yang kompleks. The zip()fungsi akan melakukan pekerjaan yang besar untuk kasus penggunaan ini:
 

Statement del.
Untuk menghapus item dari list yang diberikan indeksnya alih-alih nilainya: pernyataan del. Ini berbeda dari pop() metode yang mengembalikan nilai. Pernyataan del juga dapat digunakan untuk menghapus irisan dari list atau menghapus seluruh list (yang kita lakukan sebelumnya oleh tugas dari list kosong untuk slice). Sebagai contoh:
 
Del juga dapat digunakan untuk menghapus seluruh variable
del a

	Tuples and squences
Kita melihat bahwa list dan string memiliki banyak properti umum, seperti operasi pengindeksan dan pemotongan. Mereka adalah dua contoh tipe data urutan (lihat Jenis Urutan - list, tupel, rentang ). Karena Python adalah bahasa yang berkembang, tipe data urutan lainnya dapat ditambahkan. Ada juga tipe data urutan standar lainnya: tupel . Tupel terdiri dari sejumlah nilai yang dipisahkan dengan koma, misalnya:
 
Seperti yang kita lihat, on output tuple selalu diapit tanda kurung, sehingga tupel bersarang diinterpretasikan dengan benar; mereka dapat dimasukkan dengan atau tanpa tanda kurung di sekitarnya, meskipun seringkali tanda kurung tetap diperlukan (jika tupel adalah bagian dari ekspresi yang lebih besar). Tidak mungkin untuk menetapkan ke masing-masing item dari sebuah tupel, namun dimungkinkan untuk membuat tupel yang berisi objek yang bisa berubah, seperti list.
Meskipun tuple mungkin tampak mirip dengan list, mereka sering digunakan dalam situasi yang berbeda dan untuk tujuan yang berbeda. Tupel tidak dapat diubah , dan biasanya berisi urutan elemen heterogen yang diakses melalui pembongkaran (lihat nanti di bagian ini) atau pengindeksan (atau bahkan berdasarkan atribut dalam kasus namedtuples). List dapat berubah, dan elemennya biasanya homogen dan diakses dengan mengulang list.
Masalah khusus adalah konstruksi tupel yang berisi 0 atau 1 item: sintaks memiliki beberapa kebiasaan tambahan untuk mengakomodasi ini. Tupel kosong dibuat oleh sepasang tanda kurung kosong; sebuah tupel dengan satu item dibuat dengan mengikuti nilai dengan koma (tidak cukup untuk menyertakan satu nilai dalam tanda kurung). Kurang bagus, tapi efektif. Sebagai contoh:
 
Pernyataan tersebut adalah contoh pengepakan tupel : nilai-nilai , dan dikemas bersama dalam sebuah tupel. Operasi kebalikannya juga dimungkinkan:t = 12345, 54321, 'hello!'1234554321'hello!'
>>> x, y, z = t
Ini disebut, cukup tepat, pembongkaran urutan dan berfungsi untuk setiap urutan di sisi kanan. Pembongkaran urutan mensyaratkan bahwa ada banyak variabel di sisi kiri tanda sama dengan karena jumlah elemen dalam urutan. Perhatikan bahwa multiple assignment sebenarnya hanya kombinasi dari tuple packing dan sequence unpacking.
Sets
Python juga menyertakan tipe data untuk set . Satu set adalah koleksi tidak berurutan tanpa elemen duplikat. Penggunaan dasar termasuk pengujian keanggotaan dan menghilangkan entri duplikat. Set objek juga mendukung operasi matematika seperti penyatuan, persimpangan, perbedaan, dan perbedaan simetris.
Tanda kurung kurawal atau set() fungsinya dapat digunakan untuk membuat set. Catatan: untuk membuat satu set kosong kita harus menggunakan set(), bukan {}; yang terakhir membuat kamus kosong, struktur data yang kita bahas di bagian selanjutnya.
Berikut adalah demonstrasi singkatnya:
	 
Mirip dengan pemahaman list, pemahaman himpunan juga didukung :
 
	
Kamus/Dictionary
Tipe data berguna lainnya yang dibangun ke dalam Python adalah kamus. Kamus terkadang ditemukan dalam bahasa lain sebagai "ingatan asosiatif" atau "larik asosiatif". Tidak seperti urutan, yang diindeks oleh serangkaian angka, kamus diindeks oleh kunci , yang bisa berupa tipe yang tidak dapat diubah; string dan angka selalu bisa menjadi kunci. Tupel dapat digunakan sebagai kunci jika hanya berisi string, angka, atau tupel; jika tupel berisi objek yang bisa berubah baik secara langsung maupun tidak langsung, itu tidak bisa digunakan sebagai kunci. Anda tidak dapat menggunakan list sebagai kunci, karena list dapat dimodifikasi di tempatnya menggunakan penetapan indeks, penetapan irisan, atau metode seperti append()dan extend().
Cara terbaik untuk menganggap kamus sebagai sekumpulan pasangan kunci: nilai , dengan persyaratan bahwa kunci tersebut unik (dalam satu kamus). Sepasang kawat gigi menciptakan kamus kosong: {}. Menempatkan list pasangan kunci: nilai yang dipisahkan koma dalam tanda kurung kurawal menambahkan pasangan kunci: nilai awal ke kamus; ini juga cara kamus dituliskan pada keluaran.
Operasi utama pada kamus adalah menyimpan nilai dengan beberapa kunci dan mengekstrak nilai yang diberikan kunci tersebut. Dimungkinkan juga untuk menghapus key: value pair with del. Jika Anda menyimpan menggunakan kunci yang sudah digunakan, nilai lama yang terkait dengan kunci itu dilupakan. Merupakan kesalahan untuk mengekstrak nilai menggunakan kunci yang tidak ada.
Tampil list(d)di kamus mengembalikan list semua kunci yang digunakan dalam kamus, dalam urutan penyisipan (jika Anda ingin menyortir, gunakan sorted(d)saja). Untuk memeriksa apakah satu kunci ada di kamus, gunakan inkata kunci.
Berikut adalah contoh kecil menggunakan kamus:
	 
dict()konstruktor membangun kamus langsung dari urutan pasangan kunci-nilai:
 
Selain itu, pemahaman dict dapat digunakan untuk membuat kamus dari ekspresi kunci dan nilai yang berubah-ubah:
 
Jika kuncinya adalah string sederhana, terkadang lebih mudah untuk menentukan pasangan menggunakan argumen kata kunci:
 

Teknik looping
Saat mengulang kamus, kunci dan nilai terkait dapat diambil pada saat yang sama menggunakan items()metode.
 
Saat melakukan perulangan melalui suatu urutan, indeks posisi dan nilai terkait dapat diambil pada saat yang sama menggunakan enumerate()fungsi tersebut.
 
Untuk mengulang lebih dari dua atau lebih urutan pada saat yang sama, entri dapat dipasangkan dengan zip()fungsi tersebut.
 
Untuk mengulang urutan secara terbalik, pertama-tama tentukan urutan dalam arah maju dan kemudian panggil reversed()fungsinya.
 
Untuk mengulang urutan dalam urutan terurut, gunakan sorted()fungsi yang mengembalikan daftar terurut baru sambil membiarkan sumber tidak berubah.
 
Menggunakan set()secara berurutan menghilangkan elemen duplikat. Penggunaan sorted()kombinasi dengan set()lebih dari satu urutan adalah cara idiomatik untuk mengulang elemen unik dari urutan dalam urutan yang diurutkan.
 
Terkadang Anda tergoda untuk mengubah daftar saat Anda mengulanginya; naTerkadang Anda tergoda untuk mengubah daftar saat Anda mengulanginya; namun, seringkali lebih sederhana dan lebih aman untuk membuat daftar baru.mun, seringkali lebih sederhana dan lebih aman untuk membuat daftar baru.
 

Lebih lanjut tentang kondisi
Kondisi yang digunakan dalam pernyataan whiledan ifdapat berisi operator apa pun, tidak hanya perbandingan.
Operator pembanding indan memeriksa apakah suatu nilai terjadi (tidak terjadi) secara berurutan. Operator dan membandingkan apakah dua objek benar-benar objek yang sama; ini hanya penting untuk objek yang bisa berubah seperti daftar. Semua operator pembanding memiliki prioritas yang sama, yang lebih rendah daripada semua operator numerik.not inisis not
Perbandingan bisa dirantai. Misalnya, menguji apakah kurang dari dan terlebih lagi sama, a < b == cabbc
Perbandingan dapat digabungkan menggunakan operator Boolean anddan or, dan hasil perbandingan (atau ekspresi Boolean lainnya) dapat dinegasikan dengan not. Ini memiliki prioritas lebih rendah daripada operator pembanding; di antara mereka, notmemiliki prioritas tertinggi dan orterendah, sehingga setara dengan . Seperti biasa, tanda kurung dapat digunakan untuk menyatakan komposisi yang diinginkan.A and not B or C(A and (not B)) or C
Operator Boolean anddan ordisebut juga operator hubung singkat : argumen mereka dievaluasi dari kiri ke kanan, dan evaluasi berhenti segera setelah hasilnya ditentukan. Misalnya, jika Adan Cbenar tetapi Bsalah, tidak mengevaluasi ekspresi tersebut . Ketika digunakan sebagai nilai umum dan bukan sebagai Boolean, nilai kembalian dari operator hubung singkat adalah argumen evaluasi terakhir.A and B and CC
Hal ini dimungkinkan untuk menetapkan hasil perbandingan atau ekspresi Boolean lainnya ke variabel. Sebagai contoh:
 
Pada pemrograman Python, penugasan di dalam ekspresi harus dilakukan secara eksplisit dengan operator walrus := . Ini menghindari kelas umum masalah yang dihadapi dalam program C: mengetikkan = ekspresi saat ==dimaksudkan.

	
Membandingkan squences dengan tipe lain
Objek urutan biasanya dapat dibandingkan dengan objek lain dengan tipe urutan yang sama. Perbandingannya menggunakan leksikografismemesan: pertama, dua item pertama dibandingkan, dan jika berbeda, hal ini menentukan hasil perbandingan; jika keduanya sama, dua item berikutnya dibandingkan, dan seterusnya, hingga salah satu urutan habis. Jika dua item yang akan dibandingkan itu sendiri merupakan urutan dari jenis yang sama, maka perbandingan leksikografis dilakukan secara rekursif. Jika semua item dari dua urutan dibandingkan sama, urutan dianggap sama. Jika satu urutan adalah sub-urutan awal dari yang lain, urutan yang lebih pendek adalah yang lebih kecil (lebih kecil). Pengurutan leksikografis untuk string menggunakan nomor poin kode Unicode untuk mengurutkan karakter individual. Beberapa contoh perbandingan antara urutan dengan tipe yang sama:
 

Note: membandingkan objek dari tipe yang berbeda dengan <atau >legal asalkan objek tersebut memiliki metode perbandingan yang sesuai. Misalnya, tipe numerik campuran dibandingkan menurut nilai numeriknya, jadi 0 sama dengan 0,0, dll. Jika tidak, alih-alih memberikan urutan arbitrer, interpreter akan memunculkan TypeErrorpengecualian.

