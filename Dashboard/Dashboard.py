import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(
    page_title="Dashboard Polutan",  # Judul halaman
    page_icon="🌍",                  # Ikon halaman
    # layout="wide",                   # Menggunakan layout lebar
    initial_sidebar_state="expanded" # Sidebar dalam keadaan terbuka
)


# Fungsi untuk membuat plot tren polutan
def plot_pollutant_trends(df, start_date, end_date):
    st.subheader(f'Tren PM2.5 dan PM10 dari {start_date} hingga {end_date}')

    # Plotting PM2.5 over time for all stations
    plt.figure(figsize=(5, 3))
    sns.lineplot(x='date_time', y='PM2.5', hue='station', data=df, errorbar=None)
    plt.title(f'Tren PM2.5 dari {start_date} hingga {end_date}')
    
    # Mengatur judul, label, dan warna teks
    plt.title('Mean TEMP per Station dan Wind Direction (wd)', color='white', fontsize = 10)
    plt.xlabel('Station', color='white', fontsize=5)
    plt.ylabel('Mean TEMP', color='white', fontsize=5)

    # Mengatur rotasi x-axis dan warna ticks
    plt.xticks(rotation=45, color='white', fontsize=5)
    plt.yticks(color='white', fontsize=5)

    # Mengatur posisi legend di luar plot
    plt.legend(title='Wind Direction', loc='upper left', bbox_to_anchor=(1, 1), title_fontsize='8', labelcolor='white',fontsize=5, frameon=False)

    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

    # Plotting PM10 over time for all stations
    plt.figure(figsize=(5, 3))
    sns.lineplot(x='date_time', y='PM10', hue='station', data=df, errorbar=None)
    plt.title(f'Tren PM10 dari {start_date} hingga {end_date}')

     # Mengatur judul, label, dan warna teks
    plt.title('Mean TEMP per Station dan Wind Direction (wd)', color='white', fontsize = 10)
    plt.xlabel('Station', color='white', fontsize=5)
    plt.ylabel('Mean TEMP', color='white', fontsize=5)

    # Mengatur rotasi x-axis dan warna ticks
    plt.xticks(rotation=45, color='white', fontsize=5)
    plt.yticks(color='white', fontsize=5)

    # Mengatur posisi legend di luar plot
    plt.legend(title='Wind Direction', loc='upper left', bbox_to_anchor=(1, 1), title_fontsize='8', labelcolor='white',fontsize=5, frameon=False)

    plt.xticks(rotation=45)
    plt.tight_layout()
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

    # Plotting frekuensi pelampauan ambang batas WHO untuk PM2.5 dengan warna pink dan biru
    plt.figure(figsize=(5, 3))
    sns.countplot(x='station', hue='PM2.5_Above_WHO', data=df, palette=['#FF69B4', 'blue'])  # Pink untuk True, Blue untuk False
    plt.title('Frekuensi Pelampauan Batas WHO untuk PM2.5 di Setiap Stasiun')

    # Mengatur rotasi x-axis dan warna ticks
    plt.xticks(rotation=45, color='white', fontsize=5)
    plt.yticks(color='white', fontsize=5)
    plt.xlabel('station', color='white', fontsize=7)
    plt.ylabel('count', color='white', fontsize=7)

    # Mengatur posisi legend di luar plot
    plt.legend(title='Wind Direction', loc='upper left', bbox_to_anchor=(1, 1), title_fontsize='8', labelcolor='white',fontsize=5, frameon=False)

    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

    # Plotting frekuensi pelampauan ambang batas WHO untuk PM10 dengan warna pink dan biru
    plt.figure(figsize=(5, 3))
    sns.countplot(x='station', hue='PM10_Above_WHO', data=df, palette=['#FF69B4', 'blue'])  # Pink untuk True, Blue untuk False
    plt.title('Frekuensi Pelampauan Batas WHO untuk PM10 di Setiap Stasiun')

    # Mengatur rotasi x-axis dan warna ticks
    plt.xticks(rotation=45, color='white', fontsize=5)
    plt.yticks(color='white', fontsize=5)
    plt.xlabel('station', color='white', fontsize=7)
    plt.ylabel('count', color='white', fontsize=7)

    # Mengatur posisi legend di luar plot
    plt.legend(title='Wind Direction', loc='upper left', bbox_to_anchor=(1, 1), title_fontsize='8', labelcolor='white',fontsize=5, frameon=False)

    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

def scatter_plot_rain_polutan(df):
    Suhu_V_PM25 , Angin_V_pm25, Hujan_V_PM25 = st.tabs(['Suhu v PM2.5', 'Angin v PM2.5', 'Hujan v PM2.5'])
    
    with Suhu_V_PM25 :
        # Scatter plot between Temperature and PM2.5
        plt.figure(figsize=(5,3))
        sns.scatterplot(x='TEMP', y='PM2.5', hue='station', data=df, alpha=0.5)
    
        # Mengatur rotasi x-axis dan warna ticks
        plt.xticks(rotation=45, color='white', fontsize=5)
        plt.yticks(color='white', fontsize=5)
        plt.xlabel('TEMP', color='white', fontsize=7)
        plt.ylabel('PM2.5', color='white', fontsize=7)

        # Mengatur posisi legend di luar plot
        plt.legend(title='station', loc='upper left', bbox_to_anchor=(1, 1), title_fontsize='8', labelcolor='white',fontsize=5, frameon=False)
        plt.title('Pengaruh Suhu terhadap PM2.5')
        st.pyplot(plt)

    with Angin_V_pm25 :
        # Scatter plot between Wind Speed and PM2.5
        plt.figure(figsize=(5,3))
        sns.scatterplot(x='WSPM', y='PM2.5', hue='station', data=df, alpha=0.5)
        plt.title('Pengaruh Kecepatan Angin terhadap PM2.5')
        
        # Mengatur rotasi x-axis dan warna ticks
        plt.xticks(rotation=45, color='white', fontsize=5)
        plt.yticks(color='white', fontsize=5)
        plt.xlabel('WSPM', color='white', fontsize=7)
        plt.ylabel('PM2.5', color='white', fontsize=7)

        # Mengatur posisi legend di luar plot
        plt.legend(title='Wind Direction', loc='upper left', bbox_to_anchor=(1, 1), title_fontsize='8', labelcolor='white',fontsize=5, frameon=False)
        st.pyplot(plt)

    with Hujan_V_PM25 :
        # Scatter plot between Rain and PM2.5
        plt.figure(figsize=(5,3))
        sns.scatterplot(x='RAIN', y='PM2.5', hue='station', data=df, alpha=0.5)
        plt.title('Pengaruh Curah Hujan terhadap PM2.5')
        # Mengatur rotasi x-axis dan warna ticks
        plt.xticks(rotation=45, color='white', fontsize=5)
        plt.yticks(color='white', fontsize=5)
        plt.xlabel('RAIN', color='white', fontsize=7)
        plt.ylabel('PM2.5', color='white', fontsize=7)

        # Mengatur posisi legend di luar plot
        plt.legend(title='stataion', loc='upper left', bbox_to_anchor=(1, 1), title_fontsize='8', labelcolor='white',fontsize=5, frameon=False)
        st.pyplot(plt)

def box_plot_station(df):

    # Membuat custom flierprops untuk memberi warna pada outliers (lingkaran)
    flierprops = dict(marker='o', markerfacecolor='white', markersize=4  , linestyle='none')
    
    # Boxplot untuk melihat distribusi PM2.5 di setiap stasiun
    plt.figure(figsize=(5,3))
    sns.boxplot(x='station', y='PM2.5', data=df, palette='Set3', flierprops=flierprops)
    plt.title('Perbandingan Distribusi PM2.5 Antar Stasiun')
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
    plt.title('Perbandingan Distribusi PM10 Antar Stasiun')
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
   'Menu', options=['Home', 'Temperature Trends', 'PM2.5', 'Station', 'Treshold Breach']
)

# Bagian utama untuk visualisasi dan tabel
if menu == 'Home':
    # 1. Menampilkan tabel suhu rata-rata berdasarkan stasiun dan arah angin
    station_wd = create_station_temp_wind_df(filtered_df)
    st.title("Dashboard Suhu dan Arah Angin per Stasiun")
    st.write(f"Tabel suhu rata-rata berdasarkan stasiun dan arah angin dari {start_date} hingga {end_date}")
    st.dataframe(station_wd)

    # 2. Agregasi suhu maksimum, rata-rata, dan minimum per stasiun dan arah angin
    grouped_df = create_aggregate_and_visualize(filtered_df)
    grouped_df.columns = ['Max TEMP', 'Mean TEMP', 'Min TEMP']
    grouped_df = grouped_df.reset_index()

    # Plot Mean TEMP berdasarkan station dan wd dengan background hitam dan teks putih
    plt.style.use('dark_background')  # Mengatur style dengan background gelap
    plt.figure(figsize=(5, 3))
    sns.barplot(x='station', y='Mean TEMP', hue='wd', data=grouped_df)

    # Mengatur judul, label, dan warna teks
    plt.title('Mean TEMP per Station dan Wind Direction (wd)', color='white', fontsize=10)
    plt.xlabel('Station', color='white', fontsize=5)
    plt.ylabel('Mean TEMP', color='white', fontsize=5)

    # Mengatur posisi legend di luar plot
    plt.legend(title='Wind Direction', loc='upper left', bbox_to_anchor=(1, 1), title_fontsize='8', labelcolor='white',fontsize=5, frameon=False)

    # Mengatur rotasi x-axis dan warna ticks
    plt.xticks(rotation=45, color='white', fontsize=5)
    plt.yticks(color='white', fontsize=5)


    # Mengatur layout agar lebih rapi
    plt.tight_layout()

    # Tampilkan plot di Streamlit
    st.pyplot(plt)

elif menu == 'Temperature Trends':
    # Plot tren PM2.5 dan PM10 berdasarkan filter yang dipilih

    plot_pollutant_trends(filtered_df, start_date, end_date)

elif menu == 'Treshold Breach' :
    st.title('Treshold Breach - Pelampauan Ambang Batas WHO')
    plot_who_threshold_breach(filtered_df)

elif menu == 'PM2.5' :
        scatter_plot_rain_polutan(filtered_df)

elif menu == 'Station' :
        box_plot_station(filtered_df)