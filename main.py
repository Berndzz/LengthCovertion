import streamlit as st


def meter_ke_piksel(panjang_m, lebar_m, dpi):
    # Konversi meter ke inci
    panjang_inci = panjang_m * 39.3701
    lebar_inci = lebar_m * 39.3701

    # Konversi inci ke piksel
    panjang_piksel = int(panjang_inci * dpi)
    lebar_piksel = int(lebar_inci * dpi)

    return panjang_piksel, lebar_piksel


def cm_ke_piksel(panjang_cm, lebar_cm, dpi):
    # Konversi centimeter ke inci
    panjang_inci = panjang_cm / 2.54
    lebar_inci = lebar_cm / 2.54

    # Konversi inci ke piksel
    panjang_piksel = int(panjang_inci * dpi)
    lebar_piksel = int(lebar_inci * dpi)

    return panjang_piksel, lebar_piksel


def main():
    st.title("Konversi Ukuran untuk Cetak")
    unit = st.radio(
        "Pilih unit ukuran yang ingin Anda konversi:", ("Meter", "Centimeter")
    )

    if unit == "Meter":
        panjang = st.number_input(
            "Masukkan panjang spanduk (dalam meter):", min_value=0.0, format="%f"
        )
        lebar = st.number_input(
            "Masukkan lebar spanduk (dalam meter):", min_value=0.0, format="%f"
        )
    elif unit == "Centimeter":
        panjang = st.number_input(
            "Masukkan panjang spanduk (dalam centimeter):", min_value=0.0, format="%f"
        )
        lebar = st.number_input(
            "Masukkan lebar spanduk (dalam centimeter):", min_value=0.0, format="%f"
        )

    # Input untuk DPI
    dpi = st.number_input("Masukkan DPI (Dots Per Inch):", min_value=1, value=300)
    if st.button("Hitung Ukuran dalam Piksel"):
        if unit == "Meter":
            panjang_piksel, lebar_piksel = meter_ke_piksel(panjang, lebar, dpi)
        elif unit == "Centimeter":
            panjang_piksel, lebar_piksel = cm_ke_piksel(panjang, lebar, dpi)
        st.markdown(
            f"<span style='font-size: 24px;'>Ukuran dalam piksel: {panjang_piksel} Width x {lebar_piksel} Height </span>",
            unsafe_allow_html=True,
        )

    with st.expander("Lihat Rekomendasi DPI"):
        st.write(
            """
    - **Spanduk dan Banner Kecil**: 150-300 DPI (dilihat dari jarak dekat)
    - **Spanduk dan Banner Sedang**: 100-150 DPI (dilihat dari jarak menengah)
    - **Baliho atau Billboard**: 30-100 DPI (dilihat dari jarak jauh)
    - **Media Massa Terpadu (MMT)**: 30-100 DPI (dilihat dari berbagai jarak)
    - **Poster dan Cetak Foto**: 200-300 DPI (untuk detail tinggi dan dilihat dari dekat)
    - **Flyer dan Brosur**: 300 DPI (untuk pembacaan dekat)
    - **Kartu Nama**: 300-600 DPI (untuk kualitas cetak terbaik pada ukuran kecil)
    """
        )


if __name__ == "__main__":
    main()
