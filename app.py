import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Page: Home
def home():
    st.title("Aplikasi Regresi Linier Sederhana")
    st.write("Regresi linier sederhana adalah metode statistik untuk memodelkan hubungan antara variabel independen (X) dan variabel dependen (Y). Regresi linier sederhana digunakan untuk mengestimasi nilai Y berdasarkan nilai X.")
    st.write("Regresi linier sederhana berguna untuk memahami dan memprediksi hubungan linier antara dua variabel. Sehingga dapat membantu dalam analisis dan prediksi data dalam berbagai bidang seperti ilmu sosial, ekonomi, dan ilmu alam.")

# Page: Korelasi
def korelasi():
    st.title("Korelasi")
    st.write("Silakan pilih opsi untuk memasukkan data:")
    
    option = st.selectbox("Pilih opsi:", ("Masukkan data manual", "Upload file CSV/Excel"))
    
    if option == "Masukkan data manual":
        st.write("Masukkan jumlah data:")
        num_data = st.number_input("Jumlah data", min_value=1, step=1, value=10)
        
        data = []
        for i in range(num_data):
            x = st.number_input(f"Masukkan nilai X{i+1}")
            y = st.number_input(f"Masukkan nilai Y{i+1}")
            data.append([x, y])
        
        df = pd.DataFrame(data, columns=["X", "Y"])
    else:
        file = st.file_uploader("Upload file CSV/Excel", type=["csv", "xlsx"])
        if file is not None:
            df = pd.read_excel(file)  
        else:
            df = None
    
    if df is not None:
        st.write("Data:")
        st.table(df)
        
        correlation = df['X'].astype(float).corr(df['Y'].astype(float))
        st.write(f"Korelasi antara X dan Y: {correlation}")
        
        plt.scatter(df['X'].astype(float), df['Y'].astype(float))
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Hubungan antara X dan Y')
        st.pyplot(plt)

        st.write("Hasil analisis:")
        if correlation > 0:
            st.write("Variabel X dan Y memiliki hubungan linier.")
        elif correlation < 0:
            st.write("Variabel X dan Y memiliki hubungan berbanding terbalik.")

# Page: Regresi
def regresi():
    st.title("Regresi")
    st.write("Silakan pilih opsi untuk memasukkan data:")
    
    option = st.selectbox("Pilih opsi:", ("Masukkan data manual", "Upload file CSV/Excel"))
    
    if option == "Masukkan data manual":
        st.write("Masukkan jumlah data:")
        num_data = st.number_input("Jumlah data", min_value=1, step=1, value=10)
        
        data = []
        for i in range(num_data):
            x = st.number_input(f"Masukkan nilai X{i+1}")
            y = st.number_input(f"Masukkan nilai Y{i+1}")
            data.append([x, y])
        
        df = pd.DataFrame(data, columns=["X", "Y"])
    else:
        file = st.file_uploader("Upload file CSV/Excel", type=["csv", "xlsx"])
        if file is not None:
            df = pd.read_excel(file)  
        else:
            df = None
    
    if df is not None:
        st.write("Data:")
        st.table(df)
        
        X = df['X'].astype(float).values.reshape(-1, 1)
        Y = df['Y'].astype(float).values.reshape(-1, 1)
        
        model = LinearRegression()
        model.fit(X, Y)
        
        beta_0 = model.intercept_[0]
        beta_1 = model.coef_[0][0]
        
        st.write(f"Koefisien Beta 0: {beta_0}")
        st.write(f"Koefisien Beta 1: {beta_1}")
        
        plt.scatter(X, Y)
        plt.plot(X, model.predict(X), color='red')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Regresi Linier Sederhana')
        st.pyplot(plt)
        
        Y_pred = model.predict(X)
        r2 = r2_score(Y, Y_pred)
        st.write(f"Koefisien determinasi: {r2*100:.2f}%")

# Main
def main():
    pages = {
        "Home": home,
        "Korelasi": korelasi,
        "Regresi": regresi
    }
    
    st.sidebar.title("Navigasi")
    selection = st.sidebar.radio("Pergi ke:", list(pages.keys()))
    page = pages[selection]
    page()

if __name__ == "__main__":
    main()
