import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(
    page_title="Air Quality",  # Judul halaman
    page_icon="🌬️",  # Ikon terkait udara
    # layout="wide",  # Menggunakan layout lebar 
    initial_sidebar_state="expanded"  # Sidebar dalam keadaan terbuka
)

def pollutan_trend_by_month(df):
    # Menghitung rata-rata bulanan
    df['month'] = df['date_time'].dt.month  # Menambahkan kolom 'month'
    overall_monthly_avg = df.groupby('month')[['PM2.5', 'PM10']].mean().reset_index()

    # Plot rata-rata keseluruhan PM10 dari semua stasiun
    plt.figure(figsize=(10,5))
    plt.fill_between(overall_monthly_avg['month'], 0, overall_monthly_avg['PM10'], color='gray', alpha=0.2)
    sns.lineplot(data=overall_monthly_avg, x='month', y='PM10', color='blue', label='Rata-rata Semua Stasiun')
    plt.title('Rata-rata Bulanan PM10 Semua Stasiun (2013-2017)')
    plt.xlabel('Bulan')
    plt.ylabel('PM10')
    plt.xticks(rotation=45)
    plt.legend()
    st.pyplot(plt)

    # Highlight bulan kritis dengan lonjakan PM10
    critical_months = [1, 12]  # Contoh bulan dengan kualitas udara buruk

    # Plot dengan highlight pada bulan kritis
    plt.figure(figsize=(10,5))
    plt.fill_between(overall_monthly_avg['month'], 0, overall_monthly_avg['PM10'], color='gray', alpha=0.2)
    sns.lineplot(data=overall_monthly_avg, x='month', y='PM10', color='blue', label='Rata-rata Semua Stasiun')

    # Highlight bulan kritis dengan warna yang berbeda
    for month in critical_months:
        plt.axvspan(month-0.5, month+0.5, color='red', alpha=0.3)

    plt.title('Rata-rata Bulanan PM10 dengan Highlight Bulan Kritis (2013-2017)')
    plt.xlabel('Bulan')
    plt.ylabel('PM10')
    plt.xticks(rotation=45)
    plt.legend()
    st.pyplot(plt)

# Fungsi untuk membuat pivot table suhu per station dan wd
def create_station_temp_wind_df(df):
    temp_station_wind = df.pivot_table(values='TEMP', index='station', columns='wd', aggfunc='mean')
    return temp_station_wind

# Fungsi untuk mengelompokkan data dan melakukan agregasi suhu
def create_aggregate_and_visualize(df):
    grouped_df = df.groupby(by=['station', 'wd']).agg({
        'TEMP': ['max', 'mean', 'min']
    }).sort_values(by='station', ascending=False)
    return grouped_df

def plot_who_threshold_breach(df):
   # Menambahkan kolom boolean untuk mengecek apakah nilai PM2.5 dan PM10 melebihi ambang batas WHO
    df['PM2.5_Above_WHO'] = df['PM2.5'] > 25
    df['PM10_Above_WHO'] = df['PM10'] > 50

    # Plotting frekuensi pelampauan ambang batas WHO untuk PM2.5
    plt.figure(figsize=(8, 5))  # Memperbesar plot agar lebih jelas
    sns.countplot(x='station', hue='PM2.5_Above_WHO', data=df, palette=['#FF69B4', 'blue'])  # Pink untuk True, Blue untuk False
    plt.title('Frekuensi Pelampauan Batas WHO untuk PM2.5 di Setiap Stasiun', fontsize=14, color='white')

    # Mengatur rotasi x-axis dan warna ticks
    plt.xticks(rotation=45, color='white', fontsize=10)
    plt.yticks(color='white', fontsize=10)
    plt.xlabel('Stasiun', color='white', fontsize=12)
    plt.ylabel('Jumlah', color='white', fontsize=12)

    # Mengatur posisi legend dan label
    plt.legend(title='Pelampauan Batas WHO', loc='upper left', bbox_to_anchor=(1, 1), title_fontsize='10', fontsize=8, labelcolor='white', frameon=False)

    plt.tight_layout()
    st.pyplot(plt)

    # Plotting frekuensi pelampauan ambang batas WHO untuk PM10
    plt.figure(figsize=(8, 5))
    sns.countplot(x='station', hue='PM10_Above_WHO', data=df, palette=['#FF69B4', 'blue'])  # Pink untuk True, Blue untuk False
    plt.title('Frekuensi Pelampauan Batas WHO untuk PM10 di Setiap Stasiun', fontsize=14, color='white')

    # Mengatur rotasi x-axis dan warna ticks
    plt.xticks(rotation=45, color='white', fontsize=10)
    plt.yticks(color='white', fontsize=10)
    plt.xlabel('Stasiun', color='white', fontsize=12)
    plt.ylabel('Jumlah', color='white', fontsize=12)

    # Mengatur posisi legend dan label
    plt.legend(title='Pelampauan Batas WHO', loc='upper left', bbox_to_anchor=(1, 1), title_fontsize='10', fontsize=8, labelcolor='white', frameon=False)

    plt.tight_layout()
    st.pyplot(plt)

def scatter_plot_rain_polutan(df):
    Suhu_V_PM25 , Angin_V_pm25, Hujan_V_PM25 = st.tabs(['Suhu v PM2.5', 'Angin v PM2.5', 'Hujan v PM2.5'])
    
    with Suhu_V_PM25 :
        # Scatter plot between Temperature and PM2.5
        plt.figure(figsize=(8,5))  # Memperbesar ukuran plot agar lebih jelas
        sns.scatterplot(x='TEMP', y='PM2.5', hue='station', data=df, alpha=0.6, s=50)  # s untuk memperbesar ukuran marker

        # Mengatur rotasi x-axis dan warna ticks
        plt.xticks(rotation=45, color='white', fontsize=10)
        plt.yticks(color='white', fontsize=10)
        plt.xlabel('Suhu (°C)', color='white', fontsize=12)  # Menambahkan satuan suhu untuk memperjelas
        plt.ylabel('Konsentrasi PM2.5 (µg/m³)', color='white', fontsize=12)  # Menambahkan satuan PM2.5

        # Mengatur posisi legend di luar plot
        plt.legend(title='Station', loc='upper left', bbox_to_anchor=(1, 1), title_fontsize='10', labelcolor='white', fontsize=8, frameon=False)

        # Judul plot yang lebih informatif
        plt.title('Pengaruh Suhu terhadap Konsentrasi PM2.5', color='white', fontsize=14)

        # Mengatur layout agar lebih rapi
        plt.tight_layout()

        # Tampilkan plot di Streamlit
        st.pyplot(plt)


    with Angin_V_pm25 :
        # Scatter plot between Wind Speed and PM2.5
        plt.figure(figsize=(8, 5))  # Memperbesar ukuran plot agar lebih jelas
        sns.scatterplot(x='WSPM', y='PM2.5', hue='station', data=df, alpha=0.6, s=50)  # s untuk memperbesar ukuran marker

        # Mengatur judul, label, dan warna teks
        plt.title('Pengaruh Kecepatan Angin terhadap Konsentrasi PM2.5', fontsize=14, color='white')
        plt.xlabel('Kecepatan Angin (WSPM)', fontsize=12, color='white')
        plt.ylabel('Konsentrasi PM2.5 (µg/m³)', fontsize=12, color='white')

        # Mengatur rotasi x-axis dan warna ticks
        plt.xticks(rotation=45, fontsize=10, color='white')
        plt.yticks(fontsize=10, color='white')

        # Mengatur posisi legend di luar plot
        plt.legend(title='station', loc='upper left', bbox_to_anchor=(1, 1), title_fontsize='10', fontsize=8, labelcolor='white', frameon=False)

        # Mengatur layout agar lebih rapi
        plt.tight_layout()

        # Tampilkan plot di Streamlit
        st.pyplot(plt)

    with Hujan_V_PM25 :
         # Scatter plot between Rain and PM2.5
        plt.figure(figsize=(8, 5))  # Memperbesar ukuran plot agar lebih jelas
        sns.scatterplot(x='RAIN', y='PM2.5', hue='station', data=df, alpha=0.6, s=50)  # s untuk memperbesar ukuran marker

        # Mengatur judul, label, dan warna teks
        plt.title('Pengaruh Curah Hujan terhadap Konsentrasi PM2.5', fontsize=14, color='white')
        plt.xlabel('Curah Hujan (mm)', fontsize=12, color='white')
        plt.ylabel('Konsentrasi PM2.5 (µg/m³)', fontsize=12, color='white')

        # Mengatur rotasi x-axis dan warna ticks
        plt.xticks(rotation=45, fontsize=10, color='white')
        plt.yticks(fontsize=10, color='white')

        # Mengatur posisi legend di luar plot dan memperbaiki typo
        plt.legend(title='Station', loc='upper left', bbox_to_anchor=(1, 1), title_fontsize='10', fontsize=8, labelcolor='white', frameon=False)

        # Mengatur layout agar lebih rapi
        plt.tight_layout()

        # Tampilkan plot di Streamlit
        st.pyplot(plt)

def box_plot_station(df):

    # Membuat custom flierprops untuk memberi warna pada outliers (lingkaran)
    flierprops = dict(marker='o', markerfacecolor='white', markersize=4  , linestyle='none')
    
    # Boxplot untuk melihat distribusi PM2.5 di setiap stasiun
    plt.figure(figsize=(5,3))
    sns.boxplot(x='station', y='PM2.5', data=df, palette='Set3', flierprops=flierprops)
    plt.title('Perbandingan Distribusi PM2.5 Antar Station', fontsize=10)
    # Mengatur rotasi x-axis dan warna ticks
    plt.xticks(rotation=45, color='white', fontsize=5)
    plt.yticks(color='white', fontsize=5)
    plt.xlabel('station', color='white', fontsize=7)
    plt.ylabel('PM2.5', color='white', fontsize=7)

    # Mengatur posisi legend di luar plot
    plt.xticks(rotation=45)
    st.pyplot(plt)

    # Boxplot untuk melihat distribusi PM10 di setiap stasiun
    plt.figure(figsize=(5,3))
    sns.boxplot(x='station', y='PM10', data=df, palette='Set3', flierprops=flierprops)
    plt.title('Perbandingan Distribusi PM10 Antar Station', fontsize = 10)
    # Mengatur rotasi x-axis dan warna ticks
    plt.xticks(rotation=45, color='white', fontsize=5)
    plt.yticks(color='white', fontsize=5)
    plt.xlabel('station', color='white', fontsize=7)
    plt.ylabel('PM10', color='white', fontsize=7)

    # Mengatur posisi legend di luar plot
    plt.xticks(rotation=45)
    st.pyplot(plt)

# Membaca file CSV
all_df = pd.read_csv('https://raw.githubusercontent.com/sltns22/suhu/master/Dashboard/all_df.csv')

# Konversi kolom 'date_time' menjadi tipe datetime
all_df['date_time'] = pd.to_datetime(all_df['date_time'])

# Fungsi untuk filter data berdasarkan MTD (Month-to-Date)
def filter_mtd(df, selected_year, selected_month):
    mtd_df = df[
        (df['date_time'].dt.year == selected_year) & 
        (df['date_time'].dt.month == selected_month)
    ]
    return mtd_df

# Fungsi untuk filter data berdasarkan YTD (Year-to-Date)
def filter_ytd(df, selected_year, selected_month):
    ytd_df = df[
        (df['date_time'].dt.year == selected_year) & 
        (df['date_time'].dt.month <= selected_month)
    ]
    return ytd_df

# Judul
with st.sidebar:
    st.header('Welcome Analysis Air Quality')

# Sidebar untuk memilih year dan month
with st.sidebar:
    st.image('https://raw.githubusercontent.com/sltns22/suhu/master/Dashboard/logo.png')

st.sidebar.title("Filter Data")

# Mengambil tahun dan bulan unik dari dataset
years = all_df['date_time'].dt.year.unique()
selected_year = st.sidebar.selectbox("Year :", sorted(years))

# Filter month hanya menampilkan bulan dari tahun yang dipilih
months = all_df[all_df['date_time'].dt.year == selected_year]['date_time'].dt.month.unique()
selected_month = st.sidebar.selectbox("Month :", sorted(months))

# Dropdown untuk memilih filter MTD atau YTD
filter_option = st.sidebar.radio("Period :", ('MTD', 'YTD'))

# Jika MTD, filter berdasarkan month terpilih
if filter_option == 'MTD':
    filtered_df = filter_mtd(all_df, selected_year, selected_month)
    
# Jika YTD, filter dari bulan 1 hingga bulan terpilih
elif filter_option == 'YTD':
    filtered_df = filter_ytd(all_df, selected_year, selected_month)
    
# Memilih range tanggal dari filter
start_date = filtered_df['date_time'].min().strftime('%Y-%m-%d')
end_date = filtered_df['date_time'].max().strftime('%Y-%m-%d')

# Menu di Side Bar
menu = st.sidebar.selectbox(
   'Menu', options=['Temperature & Wind Direction', 'Pollutan Trend By Month', 'PM2.5', 'Station', 'Treshold Breach']
)

# Bagian utama untuk visualisasi dan tabel
if menu == 'Temperature & Wind Direction':
    # Membuat DataFrame dengan station_wd
    station_wd = create_station_temp_wind_df(filtered_df)

    # Judul utama dashboard
    st.subheader("🌡️ Dashboard Suhu dan Arah Angin per Stasiun 🌬️")
    
    # Keterangan di bawah judul
    st.markdown(f"**Tabel suhu rata-rata berdasarkan stasiun dan arah angin dari** {start_date} **hingga** {end_date}")

    # Menampilkan tabel suhu per stasiun dengan format yang lebih rapi
    st.dataframe(station_wd)

    # 2. Agregasi suhu maksimum, rata-rata, dan minimum per stasiun dan arah angin
    grouped_df = create_aggregate_and_visualize(filtered_df)
    grouped_df.columns = ['Max TEMP', 'Mean TEMP', 'Min TEMP']
    grouped_df = grouped_df.reset_index()

    # Menampilkan keterangan untuk agregasi suhu
    st.subheader("📊 Agregasi Suhu Maksimum, Rata-rata, dan Minimum per Stasiun dan Arah Angin")
    st.markdown("Tabel di bawah menunjukkan suhu maksimum, suhu rata-rata, dan suhu minimum di setiap stasiun berdasarkan arah angin yang terdeteksi.")

  # Pastikan all_stations dalam bentuk list
    all_stations = list(grouped_df['station'].unique())  # Mendapatkan semua stasiun unik dan mengonversi ke list
    default_stations = all_stations[:2]  # Pilih dua stasiun pertama sebagai default
    selected_stations = st.multiselect('Pilih Stasiun', all_stations, default=default_stations)

    # Memfilter data berdasarkan stasiun yang dipilih
    filtered_station_df = grouped_df[grouped_df['station'].isin(selected_stations)]


    # Memilih kolom numerik untuk formatting
    numeric_columns = filtered_station_df.select_dtypes(include='number').columns

    # Menampilkan tabel dengan format untuk kolom numerik
    st.table(filtered_station_df.style.format({col: "{:.2f}" for col in numeric_columns}).set_properties(**{
        'background-color': '#292929',
        'color': 'white',
        'border-color': 'white',
        'font-size': '11pt',
    }).set_caption("Agregasi Suhu per Stasiun dan Arah Angin"))


    st.markdown(
        """
        ### Wind Direction
        """
    )
    # Plot Mean TEMP berdasarkan station dan wd dengan background hitam dan teks putih
    plt.style.use('dark_background')  # Mengatur style dengan background gelap
    plt.figure(figsize=(10, 5))  # Memperbesar ukuran plot

    sns.barplot(x='station', y='Mean TEMP', hue='wd', data=grouped_df)

    # Mengatur judul, label, dan warna teks
    plt.title('Mean TEMP per Station dan Wind Direction (wd)', color='white', fontsize=12)
    plt.xlabel('Station', color='white', fontsize=10)
    plt.ylabel('Mean TEMP', color='white', fontsize=10)

    # Mengatur posisi legend di luar plot
    plt.legend(title='Wind Direction', loc='upper left', bbox_to_anchor=(1, 1), title_fontsize='8', labelcolor='white', fontsize=7, frameon=False)

    # Mengatur rotasi x-axis dan warna ticks
    plt.xticks(rotation=45, color='white', fontsize=8)
    plt.yticks(color='white', fontsize=8)

    # Mengatur layout agar lebih rapi
    plt.tight_layout()

    # Tampilkan plot di Streamlit
    st.pyplot(plt)


elif menu == 'Pollutan Trend By Month':
    # Plot tren PM2.5 dan PM10 berdasarkan filter yang dipilih
    pollutan_trend_by_month(all_df)

elif menu == 'Treshold Breach' :
    plot_who_threshold_breach(filtered_df)
    st.markdown(
        """
        #### Treshold Breach - Pelampauan Ambang Batas WHO
        """
    )
    st.markdown(
        """
        ##### Note :
        - Pink menunjukkan bahwa konsentrasi PM2.5 atau PM10 di stasiun tersebut melebihi ambang batas WHO (lebih dari 25 µg/m³ untuk PM2.5 dan lebih dari 50 µg/m³ untuk PM10)
        - Biru menunjukkan bahwa konsentrasi PM2.5 atau PM10 tidak melebihi ambang batas WHO
        """
    )

elif menu == 'PM2.5' :
        scatter_plot_rain_polutan(filtered_df)

elif menu == 'Station' :
        box_plot_station(filtered_df)