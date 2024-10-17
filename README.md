# Air Quality

## Deskripsi Proyek
Proyek ini adalah dashboard interaktif untuk menganalisis data kualitas udara berdasarkan parameter polutan seperti PM2.5, PM10, SO2, NO2, CO, O3, serta parameter cuaca seperti suhu (TEMP), tekanan (PRES), titik embun (DEWP), hujan (RAIN), arah angin (wd), dan kecepatan angin (WSPM). Dashboard menyediakan filter berdasarkan tahun, bulan, dan mode MTD (Month-To-Date) atau YTD (Year-To-Date).

### Fitur Utama
- Filter berdasarkan tahun dan bulan.
- Analisis dengan mode:
  - **MTD (Month-To-Date)**: Analisis data pada bulan dan tahun yang dipilih.
  - **YTD (Year-To-Date)**: Analisis data dari Januari hingga bulan yang dipilih pada tahun yang dipilih.
- Visualisasi perbandingan nilai polutan dengan standar WHO:
  - **PM2.5_Above_WHO**: Menunjukkan apakah kadar PM2.5 di atas standar WHO.
  - **PM10_Above_WHO**: Menunjukkan apakah kadar PM10 di atas standar WHO.

### Kolom Data
Dataset memiliki kolom sebagai berikut:
- **No**: Nomor urut.
- **PM2.5**, **PM10**, **SO2**, **NO2**, **CO**, **O3**: Kadar polutan di udara.
- **TEMP**: Suhu (dalam derajat Celsius).
- **PRES**: Tekanan udara (dalam hPa).
- **DEWP**: Titik embun.
- **RAIN**: Curah hujan (dalam mm).
- **wd**: Arah angin.
- **WSPM**: Kecepatan angin.
- **station**: Nama stasiun pengamatan.
- **date_time**: Tanggal dan waktu pengamatan.
- **PM2.5_Above_WHO**, **PM10_Above_WHO**: Indikator apakah nilai polutan melebihi standar WHO.

## Instalasi

1. Clone repository ini:
   ```bash
   git clone https://github.com/sltns22/suhu.git
   cd suhu

## Env

-Python
- python -m venv env
    - source env/bin/activate  # Untuk pengguna Mac/Linux
    - .\env\Scripts\activate  # Untuk pengguna Windows
- Install Requirement.txt
    - pip install -r requirements.txt
- jalankan ipynb
    - jupyter notebook notebook.ipynb
- Jalan dasboard via streamlit
    - streamlit run Dashboard/Dashboard.py

-Conda
- conda create --name suhu_env python=3.8
    - conda activate suhu_env
- Install Requirement.txt
    - pip install -r requirements.txt
- jalankan ipynb
    - jupyter notebook notebook.ipynb
- Jalan dasboard via streamlit
    - streamlit run Dashboard/Dashboard.py

## Koontribusi
Kontribusi terbuka untuk siapapun. Silakan fork repo ini, buat branch baru untuk fitur atau perbaikan, dan buat pull request.

## Lisensi
Proyek ini dilisensikan di bawah lisensi MIT. Silakan lihat file LICENSE untuk detail lebih lanjut.

## Kontak
gmail : onsltns@gmail.com