# Simulasi Pilkades Digital

Halaman demo statis: menampilkan dua calon, meminta konfirmasi pilihan, lalu menunjukkan konfirmasi lokal. Tidak ada suara yang dikirim atau disimpan sebagai hasil bersama.

## Terbitkan dengan GitHub Pages

1. Buat repositori GitHub baru, misalnya `pilkades-demo`.
2. Unggah `index.html` ke akar repositori (tombol **Add file → Upload files** di GitHub).
3. Buka **Settings → Pages**.
4. Pada **Build and deployment**, pilih **Deploy from a branch**.
5. Pilih branch `main`, folder `/(root)`, lalu tekan **Save**.
6. Tunggu alamat situs muncul. Biasanya berbentuk `https://USERNAME.github.io/pilkades-demo/`.
7. Buka alamat itu di browser, buka bagian **Buat QR**, lalu tekan **Buat QR**. Pindai QR dengan ponsel.

QR dibuat oleh library QRCode.js dari CDN, jadi pembuatan QR memerlukan koneksi internet. Halaman pilihan sendiri statis dan dapat dimuat lewat GitHub Pages.

## Pasang nama dan foto calon

Halaman sudah memakai siluet awal dari `siluet.svg`. Untuk menggantinya dengan foto:

1. Unggah foto ke repositori, misalnya `calon1.jpg` dan `calon2.jpg`.
2. Edit `index.html` di GitHub (ikon pensil).
3. Ganti `Nama Calon 1` dan `Nama Calon 2` pada judul dan tombol dengan nama calon.
4. Pada gambar pertama, ganti `src="siluet.svg"` menjadi `src="calon1.jpg"`; pada gambar kedua gunakan `src="calon2.jpg"`.
5. Ubah teks visi jika diperlukan, lalu simpan dengan **Commit changes**.

Saran: gunakan foto persegi dengan wajah di tengah agar tampil rapi dalam bingkai bulat. Nama, visi, dan foto harus diubah di judul, tombol, dan atribut `alt` gambar yang sesuai.

## Batas demo

Semua pengunjung melihat halaman yang sama, tetapi pilihan tidak dikirim ke GitHub Pages dan tidak tercatat sebagai rekap bersama. Jangan gunakan sebagai sistem pemungutan suara resmi.
