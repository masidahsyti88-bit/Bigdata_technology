# Big Data Technology - Praktikum 1

## 📌 Informasi Project

- Nama Project : bigdata_baru
- Mata Kuliah  : Big Data Technology
- Semester     : 6
- Teknologi     : Python, PySpark, MongoDB Atlas, Git

---

## 🎯 Tujuan Praktikum

Praktikum ini bertujuan untuk:

1. Menginstall dan mengkonfigurasi Apache Spark (PySpark)
2. Menghubungkan Python dengan MongoDB Atlas
3. Mengelola project menggunakan Git
4. Menjalankan Spark Job sederhana untuk pemrosesan data

---

## 🛠️ Tools & Teknologi

- Python 3.x
- Apache Spark (PySpark)
- MongoDB Atlas (Cloud Database)
- Visual Studio Code
- Git & GitHub
- Cloudflare WARP (untuk mengatasi DNS SRV issue)

---

## 📂 Struktur Project

bigdata_baru/
│
├── data/
├── cloud_storage/
├── scripts/
│ ├── test_mongo.py
│ └── simple_job.py
├── notebooks/
├── reports/
├── requirements.txt
└── README.md

---

## ⚙️ Setup Environment

### 1️⃣ Install Dependencies

```bash
pip install pyspark pymongo
2️⃣ Test Koneksi MongoDB

File: scripts/test_mongo.py

Fungsi:

Menghubungkan ke MongoDB Atlas

Menampilkan daftar database

Menjalankan:

python scripts/test_mongo.py

Jika berhasil akan muncul:

Koneksi berhasil!
List database:
['admin', 'local', ...]
3️⃣ Spark Simple Job

File: scripts/simple_job.py

Program ini:

Membuat SparkSession

Membuat DataFrame

Melakukan groupBy dan sum

Menampilkan hasil agregasi

Menjalankan:

python scripts/simple_job.py

Output:

+--------+----------+
|category|sum(value)|
+--------+----------+
|       A|        40|
|       B|        20|
+--------+----------+
🔥 Kendala & Solusi
1. DNS SRV Timeout saat koneksi MongoDB

Solusi:

Mengaktifkan VPN (Cloudflare WARP)

Menambahkan IP 0.0.0.0/0 di Network Access MongoDB Atlas

2. Python Worker Failed to Connect Back

Solusi:

Memastikan Python terdaftar di PATH

Restart VS Code

Menjalankan ulang Spark Job

3. winutils.exe Warning

Tidak berpengaruh terhadap eksekusi program.
Hanya warning di Windows.

✅ Hasil Akhir

Spark berhasil dijalankan

MongoDB Atlas berhasil terkoneksi

DataFrame dan agregasi berhasil ditampilkan

Project berhasil diupload ke GitHub

📌 Kesimpulan

Praktikum ini berhasil dijalankan dengan baik.
Mahasiswa memahami dasar instalasi dan konfigurasi Big Data Environment menggunakan PySpark serta integrasi dengan MongoDB Atlas.

👨‍💻 Author

Nama : (Syti Masidah)
NIM : (230104040060)
Kelas: (TI23B)
