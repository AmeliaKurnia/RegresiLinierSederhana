import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Menghitung nilai korelasi
def calculate_correlation(X, Y):
    mean_X = np.mean(X)
    mean_Y = np.mean(Y)
    numerator = np.sum((X - mean_X) * (Y - mean_Y))
    denominator = np.sqrt(np.sum((X - mean_X)**2) * np.sum((Y - mean_Y)**2))
    correlation = numerator / denominator
    return correlation

# Menghitung koefisien regresi beta 0 dan beta 1
def calculate_regression_coefficients(X, Y):
    mean_X = np.mean(X)
    mean_Y = np.mean(Y)
    numerator = np.sum((X - mean_X) * (Y - mean_Y))
    denominator = np.sum((X - mean_X)**2)
    beta_1 = numerator / denominator
    beta_0 = mean_Y - beta_1 * mean_X
    return beta_0, beta_1

# Menghitung R-Squared
def calculate_r_squared(X, Y, beta_0, beta_1):
    mean_Y = np.mean(Y)
    predicted_Y = beta_0 + beta_1 * X
    numerator = np.sum((Y - predicted_Y)**2)
    denominator = np.sum((Y - mean_Y)**2)
    r_squared = 1 - (numerator / denominator)
    return r_squared

# Halaman Home
def home():
    st.title("Regresi Linier Sederhana")
    st.write("Selamat datang di aplikasi Regresi Linier Sederhana!")
    st.write("Aplikasi ini digunakan untuk melakukan analisis regresi linier sederhana.")
    st.write("Regresi linier sederhana adalah metode statistik yang digunakan untuk memodelkan hubungan antara sebuah variabel dependen (Y) dengan sebuah variabel independen (X).")
    st.write("Dengan menggunakan regresi linier sederhana, kita dapat memprediksi nilai variabel dependen berdasarkan nilai variabel independen.")
    st.write("Aplikasi ini memiliki dua halaman utama: Korelasi dan Regresi. Silakan pilih halaman yang ingin diakses pada sidebar di sebelah kiri.")

# Halaman Korelasi
def korelasi():
    st.title("Analisis Korelasi")
    st.write("Halaman ini digunakan untuk melakukan analisis korelasi antara dua variabel.")
    
    option = st.radio("Pilih Opsi", ("Data Manual", "Upload File"))
    
    if option == "Data Manual":
        num_data = st.number_input("Jumlah Data", min_value=2, value=10, step=1)
        data = []
        for i in range(num_data):
            x = st.number_input(f"Nilai X{i+1}", key=f"X{i+1}")
            y = st.number_input(f"Nilai Y{i+1}", key=f"Y{i+1}")
            data.append((x, y))
        
        if st.button("Hitung Korelasi"):
            X = np.array([d[0] for d in data])
            Y = np.array([d[1] for d in data])
            
            correlation = calculate_correlation(X, Y)
            st.write(f"Nilai Korelasi: {correlation:.4f}")
            
            # Plot grafik korelasi
            plt.scatter(X, Y)
            plt.xlabel("X")
            plt.ylabel("Y")
            plt.title("Grafik Korelasi")
            st.pyplot(plt)
            
            # Analisis hasil korelasi
            if correlation > 0:
                st.write("Terdapat hubungan positif antara X dan Y.")
            elif correlation < 0:
                st.write("Terdapat hubungan negatif antara X dan Y.")
            else:
                st.write("Tidak terdapat hubungan linier antara X dan Y.")
    
    # Tambahkan bagian untuk opsi upload file jika diperlukan

# Halaman Regresi
def regresi():
    st.title("Analisis Regresi")
    st.write("Halaman ini digunakan untuk melakukan analisis regresi linier sederhana.")
    
    option = st.radio("Pilih Opsi", ("Data Manual", "Upload File"))
    
    if option == "Data Manual":
        num_data = st.number_input("Jumlah Data", min_value=2, value=10, step=1)
        data = []
        for i in range(num_data):
            x = st.number_input(f"Nilai X{i+1}", key=f"X{i+1}")
            y = st.number_input(f"Nilai Y{i+1}", key=f"Y{i+1}")
            data.append((x, y))
        
        if st.button("Hitung Regresi"):
            X = np.array([d[0] for d in data])
            Y = np.array([d[1] for d in data])
            
            beta_0, beta_1 = calculate_regression_coefficients(X, Y)
            r_squared = calculate_r_squared(X, Y, beta_0, beta_1)
            
            st.write(f"Nilai Beta 0: {beta_0:.4f}")
            st.write(f"Nilai Beta 1: {beta_1:.4f}")
            st.write(f"Nilai R-Squared: {r_squared:.4f}")
            
            # Model regresi
            plt.scatter(X, Y)
            plt.plot(X, beta_0 + beta_1 * X, color='red')
            plt.xlabel("X")
            plt.ylabel("Y")
            plt.title("Model Regresi")
            st.pyplot(plt)
            
            # Analisis kebaikan model
            if r_squared >= 0.7:
                st.write("Model regresi memiliki kebaikan yang baik.")
            elif r_squared >= 0.5:
                st.write("Model regresi memiliki kebaikan yang cukup.")
            else:
                st.write("Model regresi memiliki kebaikan yang rendah.")
    
    # Tambahkan bagian untuk opsi upload file jika diperlukan

# Main Program
def main():
    st.sidebar.title("Menu")
    menu = st.sidebar.radio("Navigasi", ("Home", "Korelasi", "Regresi"))
    
    if menu == "Home":
        home()
    elif menu == "Korelasi":
        korelasi()
    elif menu == "Regresi":
        regresi()

if __name__ == "__main__":
    main()
