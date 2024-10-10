
# Backdoor Hunter v1.0

Backdoor Hunter adalah alat pemindaian keamanan yang dirancang untuk mencari dan mendeteksi file backdoor yang tersembunyi di dalam direktori website. Alat ini juga dapat memindai metadata dari file gambar, video, dan GIF untuk mendeteksi adanya kode shell yang disisipkan.

## Fitur

- **Pemindaian Direktori**: Memindai semua file di direktori tempat alat ini dijalankan.
- **Deteksi Backdoor**: Mencocokkan konten file dengan pola-pola backdoor yang telah ditentukan.
- **Pemindaian Metadata**: Menggunakan `pyexiftool` untuk memindai metadata dari file gambar, video, dan GIF.
- **Pengabaian File**: Secara otomatis mengabaikan file `wordlist.txt` dan `hunt.py` selama pemindaian.
- **Laporan Deteksi**: Menampilkan hasil deteksi dengan format yang mudah dibaca, termasuk memberi warna pada pesan deteksi.

## Instalasi

1. Pastikan Anda memiliki Python 3 dan pip terinstal di sistem Anda.
2. Instal dependensi yang diperlukan:
   ```bash
   sudo pip3 install pyexiftool
   ```

## Penggunaan

Untuk menggunakan alat ini, cukup jalankan perintah berikut di terminal saat berada di direktori yang sama dengan `hunt.py` dan `wordlist.txt`:

```bash
python3 hunt.py
```

Alat ini akan memindai direktori dan melaporkan setiap file yang terdeteksi memiliki pola backdoor.

## Wordlist

Pola-pola backdoor yang digunakan untuk pemindaian disimpan dalam file `wordlist.txt`. Anda dapat menambahkan atau mengedit pola-pola tersebut sesuai kebutuhan.

## Kontribusi

Jika Anda ingin berkontribusi pada proyek ini, silakan buat fork dari repositori ini dan ajukan pull request dengan perubahan Anda.

## Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE).
