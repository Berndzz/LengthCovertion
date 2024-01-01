import streamlit as st


def meter_ke_piksel(panjang_m, lebar_m, dpi):
    # Konversi meter ke inci
    panjang_inci = panjang_m * 39.3701
    lebar_inci = lebar_m * 39.3701

    # Konversi inci ke piksel
    panjang_piksel = int(panjang_inci * dpi)
    lebar_piksel = int(lebar_inci * dpi)

    return panjang_piksel, lebar_piksel


def main():
    st.title("Konversi Ukuran Spanduk dari Meter ke Piksel")

    # Input untuk ukuran spanduk dalam meter
    panjang_m = st.number_input(
        "Masukkan panjang spanduk (dalam meter):", min_value=0.0, format="%f"
    )
    lebar_m = st.number_input(
        "Masukkan lebar spanduk (dalam meter):", min_value=0.0, format="%f"
    )

    # Input untuk DPI
    dpi = st.number_input("Masukkan DPI (Dots Per Inch):", min_value=1, value=300)

    # Tombol untuk melakukan perhitungan
    if st.button("Hitung Ukuran dalam Piksel"):
        panjang_piksel, lebar_piksel = meter_ke_piksel(panjang_m, lebar_m, dpi)
        # st.write(f"Ukuran dalam piksel: {panjang_piksel} x {lebar_piksel}")
        st.markdown(
            f"<span style='font-size: 24px;'>Ukuran dalam piksel: {panjang_piksel} Width x {lebar_piksel} Height </span>",
            unsafe_allow_html=True,
        )


if __name__ == "__main__":
    main()
