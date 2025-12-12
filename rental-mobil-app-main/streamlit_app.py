import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import random

class Mobil:
    # Constructor
    def __init__(self, nama_mobil, seater, transmisi, harga_rental, jumlah_tersedia):
        self._nama_mobil = nama_mobil
        self._seater = seater
        self._transmisi = transmisi
        self._harga_rental = harga_rental
        self._jumlah_tersedia = jumlah_tersedia
    
    # Getter
    @property
    def nama_mobil(self):
        return self._nama_mobil
    
    @property
    def seater(self):    
        return self._seater
    
    @property
    def transmisi(self):
        return self._transmisi
    
    @property
    def harga_rental(self):
        return self._harga_rental
    
    @property
    def jumlah_tersedia(self):
        return self._jumlah_tersedia
    
    # Setter
    @nama_mobil.setter
    def nama_mobil(self, value):
        self._nama_mobil = value
        
    @seater.setter
    def seater(self, value):
        self._seater = value
        
    @transmisi.setter
    def transmisi(self, value):
        self._transmisi = value
        
    @harga_rental.setter
    def harga_rental(self, value):
        self._harga_rental = value
        
    @jumlah_tersedia.setter
    def jumlah_tersedia(self, value):
        self._jumlah_tersedia = value
        
    # Hitung Biaya Sewa Berdasarkan Hari 
    def hitung_biaya(self, hari):
        if hari <= 0:
            return 0
        elif hari <= 7:             # 1-7 hari itu diskon 5%
            diskon = 0.05
        else:                       # >7 hari itu diskon 10%
            diskon = 0.10
        total = self._harga_rental * hari * (1 - diskon)
        return total

# Daftar Pembayaran
class Pembayaran:
    def __init__(self):
        self.bank_options = {
            "BCA": "7770001234567", 
            "Mandiri": "8880007654321", 
            "BRI": "9990009876543"
        }
    
    def generate_va(self, bank, total):
        """Generate Virtual Account Number"""
        base_va = self.bank_options[bank]
        unique_code = random.randint(100, 999)
        va_number = f"{base_va}{unique_code}"
        return va_number, unique_code

    def generate_invoice(self, mobil, hari, tanggal_mulai, tanggal_selesai, total, metode):
        """Generate invoice details"""
        invoice_id = f"INV-{datetime.now().strftime('%Y%m%d')}-{random.randint(1000, 9999)}"
    
        invoice_data = {
            "invoice_id": invoice_id,
            "mobil": mobil,
            "hari": hari,
            "tanggal_mulai": tanggal_mulai,
            "tanggal_selesai": tanggal_selesai,
            "total": total,
            "metode_pembayaran": metode,
            "status": "Pending",
            "waktu_pemesanan": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        return invoice_data

# Daftar data mobil
def init_mobil():
    mobil1 = Mobil("Mazda", 5, "Matic", 600000, 2)
    mobil2 = Mobil("BYD Seal", 5, "Matic", 800000, 3)
    mobil3 = Mobil("Pajero", 7, "Manual", 750000, 1)
    mobil4 = Mobil("Lexus", 7, "Matic", 850000, 1)
    mobil5 = Mobil("BMW 7 Series", 5, "Matic", 1000000, 2)
    
    return [mobil1, mobil2, mobil3, mobil4, mobil5]

# Aplikasi Streamlit
def main():
    st.set_page_config(
        page_title="Bloom Car Rental",
        page_icon="🎀🚘🎀",
        layout="wide"
    )
    
    st.title("🎀🚘🎀 Bloom Car Rental")
    st.markdown("---")
    
    # Daftar session state untuk menyimpan data mobil
    if 'daftar_mobil' not in st.session_state:
        st.session_state.daftar_mobil = init_mobil()
    
    # Sidebar untuk menu
    st.sidebar.title("📋 Menu")
    menu = st.sidebar.radio(
        "Pilih menu:",
        ["🏠 Beranda", "📋 Daftar Mobil", "💸 Sewa Mobil", "🧾 Invoice & Pembayaran", "🗂️ Riwayat Sewa"]
    )
    
    # Dictionary untuk pencarian mobil
    dict_mobil = {mobil.nama_mobil.lower(): mobil for mobil in st.session_state.daftar_mobil}
    
    if menu == "🏠 Beranda":
        st.header("Welcome to Bloom Car Rental")
        st.markdown("""
        ### Layanan Rental Mobil Terbaik
        - Mobil-mobil premium 🚗
        - Harga murah dengan diskon 🤑
        - Pelayanan 24/7 🕰️
        - Lepas kunci (tanpa supir) 🔑
        
        ### Diskon Spesial:
        - 🎯 Sewa 1-7 hari: Diskon 5%
        - 🎯 Sewa ≥ 7 hari: Diskon 10%
        """)
        
        st.image("https://www.bmw.co.id/content/dam/bmw/marketID/bmw_co_id/images/seo-images/bmw-7-series-sedan-cp-heritage-desktop.jpg/jcr:content/renditions/cq5dam.resized.img.980.medium.time1654500439983.jpg", 
                width=300, caption="Mobil BMW 7 Series")
    
    elif menu == "📋 Daftar Mobil":
        st.header("📋 Daftar Mobil Tersedia")
        
        # Tampilkan daftar mobil dalam tabel
        data = []
        for i, mobil in enumerate(st.session_state.daftar_mobil, start=1):
            status = "✅ Tersedia" if mobil.jumlah_tersedia > 0 else "❌ Habis"
            data.append([
                i,
                mobil.nama_mobil,
                mobil.transmisi,
                mobil.seater,
                f"Rp{mobil.harga_rental:,}/hari",
                status,
                mobil.jumlah_tersedia
            ])
        
        # Tampilkan tabel
        import pandas as pd
        df = pd.DataFrame(
            data,
            columns=["No", "Nama Mobil", "Transmisi", "Seater", "Harga Rental", "Status", "Jumlah Tersedia"]
        )
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        # Statistik
        col1, col2, col3, col4= st.columns(4)
        with col1:
            total_jenis_mobil = len(st.session_state.daftar_mobil)
            st.metric("Jenis Mobil", total_jenis_mobil)
        with col2:
            total_unit_mobil = sum(mobil.jumlah_tersedia for mobil in st.session_state.daftar_mobil)
            st.metric("Unit Tersedia", total_unit_mobil) 
        with col3:
            if 'riwayat' in st.session_state:
                unit_disewa = len(st.session_state.riwayat)
            else:
                unit_disewa = 0
            st.metric("Sedang Disewa", unit_disewa)
        with col4:
            habis = sum(1 for m in st.session_state.daftar_mobil if m.jumlah_tersedia == 0)
            st.metric("Mobil Habis", habis)
    
    elif menu == "💸 Sewa Mobil":
        st.header("💸 Sewa Mobil")
        
        # Inisialisasi pembayaran
        pembayaran = Pembayaran()
        
        # Pilihan mobil
        mobil_tersedia = [m for m in st.session_state.daftar_mobil if m.jumlah_tersedia > 0]
        mobil_names = [m.nama_mobil for m in mobil_tersedia]
        
        if not mobil_tersedia:
            st.warning("🙏🏻 Maaf, semua mobil telah tersewa 🙏🏻")
        else:
            col1, col2 = st.columns(2)
            
            with col1:
                selected_mobil_name = st.selectbox(
                    "Pilih Mobil:",
                    mobil_names,
                    help="Pilih mobil yang ingin disewa"
                )
                
                # Dapatkan objek mobil yang dipilih
                selected_mobil = dict_mobil[selected_mobil_name.lower()]
                
                # Tampilkan detail mobil
                st.subheader("Detail Mobil")
                st.write(f"**Nama Mobil:** {selected_mobil.nama_mobil}")
                st.write(f"**Transmisi:** {selected_mobil.transmisi}")
                st.write(f"**Seater:** {selected_mobil.seater} orang")
                st.write(f"**Harga per Hari:** Rp{selected_mobil.harga_rental:,}")
                st.write(f"**Stok Tersedia:** {selected_mobil.jumlah_tersedia} unit")
            
            with col2:
                st.subheader("Form Penyewaan")
                
                # Input tanggal mulai
                min_date = datetime.now().date()
                max_date = min_date + timedelta(days=30)
                
                tanggal_mulai = st.date_input(
                    "📅 Tanggal Mulai Sewa:",
                    min_value=min_date,
                    max_value=max_date,
                    value=min_date
                )
                
                # Input jumlah hari
                hari = st.number_input(
                    "Jumlah Hari:",
                    min_value=1,
                    max_value=30,
                    value=3,
                    step=1,
                    help="Minimal 1 hari, maksimal 30 hari"
                )
                
                # Hitung tanggal selesai
                tanggal_selesai = tanggal_mulai + timedelta(days=hari)
                st.info(f"**Tanggal Selesai:** {tanggal_selesai.strftime('%d %B %Y')}")
                
                # Hitung total
                if hari > 0:
                    total_setelah_diskon = selected_mobil.hitung_biaya(hari)
                    diskon_persen = "10%" if hari > 7 else "5%" 
                    
                    # Hitung harga normal (sebelum diskon)
                    harga_normal = selected_mobil._harga_rental * hari

                    # Tampilkan semua informasi
                    st.info(f"**Harga Normal:** Rp{harga_normal:,.0f}")
                    st.info(f"**Diskon:** {diskon_persen}")
                    st.success(f"**Total Biaya Setelah Diskon:** Rp{total_setelah_diskon:,.0f}")
                
                # Pilihan metode pembayaran
                st.subheader("💳 Metode Pembayaran")
                metode_pembayaran = st.radio(
                    "Pilih metode pembayaran:",
                    ["Transfer Bank (Virtual Account)", "Tunai (Bayar di Tempat)"]
                )
                # Jika pilih Virtual Account
                if metode_pembayaran == "Transfer Bank (Virtual Account)":
                    st.warning("⚠️ Harap selesaikan pembayaran dalam 1x24 jam!")
                    
                    bank = st.selectbox(
                        "Pilih Bank:",
                        list(pembayaran.bank_options.keys())
                    )
                    
                    if bank:
                        va_number, unique_code = pembayaran.generate_va(bank, total_setelah_diskon)
                        
                        st.success(f"**Virtual Account {bank}:**")
                        st.code(va_number, language=None)
                        st.info(f"**Kode Unik:** {unique_code}")
                        st.info(f"**Total Transfer:** Rp{total_setelah_diskon + unique_code:,.0f}")
                        
                # Tombol sewa
                if st.button("❕ Sewa Sekarang & Bayar ❕", type="primary"):
                    
                    st.balloons()
                    st.success(f"✅ Mobil {selected_mobil.nama_mobil} berhasil Anda sewa selama {hari} hari‼️")
                    
                    # Generate invoice
                    invoice = pembayaran.generate_invoice(
                        mobil=selected_mobil.nama_mobil,
                        hari=hari,
                        tanggal_mulai=tanggal_mulai.strftime('%d %B %Y'),
                        tanggal_selesai=tanggal_selesai.strftime('%d %B %Y'),
                        total=total_setelah_diskon,
                        metode=metode_pembayaran
                    )
                    # Simpan invoice ke session state
                    if 'invoices' not in st.session_state:
                        st.session_state.invoices = []
                    st.session_state.invoices.append(invoice)
                    
                    # Kurangi stok
                    selected_mobil.jumlah_tersedia -= 1
                    
                    # Simpan riwayat
                    if 'riwayat' not in st.session_state:
                        st.session_state.riwayat = []
                    
                    st.session_state.riwayat.append({
                        'mobil': selected_mobil.nama_mobil,
                        'hari': hari,
                        'tanggal_mulai': tanggal_mulai.strftime('%d-%m-%Y'),
                        'tanggal_selesai': tanggal_selesai.strftime('%d-%m-%Y'),
                        'total': total_setelah_diskon,
                        'diskon': diskon_persen,
                        'metode_bayar': metode_pembayaran,
                        'invoice_id': invoice['invoice_id']
                    })
    
                    #Tampilkan invoice details
                    st.markdown("---")
                    st.subheader("📋 Detail Pemesanan")
                    
                    col_detail1, col_detail2 = st.columns(2)
                    with col_detail1:
                        st.write(f"**Mobil:** {selected_mobil.nama_mobil}")
                        st.write(f"**Durasi:** {hari} hari")
                        st.write(f"**Tanggal:** {tanggal_mulai.strftime('%d %B %Y')} - {tanggal_selesai.strftime('%d %B %Y')}")
                    with col_detail2:
                        st.write(f"**Total:** Rp{total_setelah_diskon:,.0f}")
                        st.write(f"**Metode Bayar:** {metode_pembayaran}")
                        st.write(f"**Invoice ID:** {invoice['invoice_id']}")
                        
                    #Informasi pembayaran
                    st.markdown("---")
                    st.subheader("🖋️ Instruksi Pembayaran")
                    
                    if metode_pembayaran == "Transfer Bank (Virtual Account)":
                        st.info("🏦 **Silakan transfer ke Virtual Account yang tertera**")
                        st.warning("⏰ **Batas waktu pembayaran: 1x24 jam**")
                    else:
                        st.info("💰 **Silakan bayar tunai saat pengambilan mobil**")
                        st.info("🧾 **Tunjukkan invoice ini saat pengambilan mobil**")
                        
                    # Tombol aksi
                    st.markdown("---")
                    col_btn1, col_btn2 = st.columns(2)
                    with col_btn1:
                        if st.button("📥 Download Invoice", use_container_width=True):
                            st.download_button(
                                label="Klik untuk Download",
                                data=f"INVOICE BLOOM CAR RENTAL\n{'='*30}\n\n" +
                                     f"Invoice ID: {invoice['invoice_id']}\n" +
                                     f"Tanggal: {invoice['waktu_pemesanan']}\n" +
                                     f"{'='*30}\n" +
                                     f"Mobil: {invoice['mobil']}\n" +
                                     f"Lama Sewa: {invoice['hari']} hari\n" +
                                     f"Periode: {invoice['tanggal_mulai']} - {invoice['tanggal_selesai']}\n" +
                                     f"Metode Bayar: {invoice['metode_pembayaran']}\n" +
                                     f"{'='*30}\n" +
                                     f"TOTAL: Rp{invoice['total']:,.0f}\n" +
                                     f"{'='*30}\n\n" +
                                     f"Terima kasih telah menggunakan Bloom Car Rental‼️",
                                file_name=f"invoice_{invoice['invoice_id']}.txt",
                                mime="text/plain"
                            )
                    
                    with col_btn2:
                        if st.button("🔄 Pesan Mobil Lain", use_container_width=True):
                            st.rerun()
                            
                    #Update session state
                    st.session_state.daftar_mobil = st.session_state.daftar_mobil
    
    elif menu == "🧾 Invoice & Pembayaran":
        st.header("🧾 Invoice & Status Pembayaran")
        
        if 'invoices' not in st.session_state or not st.session_state.invoices:
            st.info("Belum ada invoice.")
        else:
            # Tampilkan semua invoice
            for invoice in st.session_state.invoices:
                with st.expander(f"Invoice: {invoice['invoice_id']} - {invoice['mobil']}"):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write(f"**Invoice ID:** {invoice['invoice_id']}")
                        st.write(f"**Mobil:** {invoice['mobil']}")
                        st.write(f"**Lama Sewa:** {invoice['hari']} hari")
                        st.write(f"**Tanggal:** {invoice['tanggal_mulai']} - {invoice['tanggal_selesai']}")
                    with col2:
                        st.write(f"**Total:** Rp{invoice['total']:,.0f}")
                        st.write(f"**Metode:** {invoice['metode_pembayaran']}")
                        st.write(f"**Status:** {invoice['status']}")
                        st.write(f"**Waktu:** {invoice['waktu_pemesanan']}")
                        
                    # Tombol update status
                    col_btn1, col_btn2 = st.columns(2)
                    with col_btn1:
                        if st.button(f"✅ Tandai Sudah Dibayar", key=f"pay_{invoice['invoice_id']}"):
                            invoice['status'] = 'Paid'
                            st.success("Status diperbarui menjadi Paid!")
                            st.rerun()
                    with col_btn2:
                        if st.button(f"❌ Batalkan Pesanan", key=f"cancel_{invoice['invoice_id']}"):
                            invoice['status'] = 'Cancelled'
                            st.success("Pesanan dibatalkan!")
                            st.rerun()
                            
    elif menu == "🗂️ Riwayat Sewa":
        st.header("🗂️ Riwayat Penyewaan")
        
        if 'riwayat' not in st.session_state or not st.session_state.riwayat:
            st.info("Belum ada riwayat penyewaan.")
        else:
            # Tampilkan riwayat dengan detail tanggal
            for i, transaksi in enumerate(st.session_state.riwayat, 1):
                with st.expander(f"Transaksi #{i} - {transaksi['mobil']} ({transaksi['invoice_id']})"):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write(f"**Mobil:** {transaksi['mobil']}")
                        st.write(f"**Lama Sewa:** {transaksi['hari']} hari")
                        st.write(f"**Tanggal Mulai:** {transaksi['tanggal_mulai']}")
                        st.write(f"**Tanggal Selesai:** {transaksi['tanggal_selesai']}")
                    with col2:
                        st.write(f"**Diskon:** {transaksi['diskon']}")
                        st.write(f"**Total Biaya:** Rp{transaksi['total']:,.0f}")
                        st.write(f"**Metode Bayar:** {transaksi['metode_bayar']}")
                        st.write(f"**Invoice ID:** {transaksi['invoice_id']}")
            
            # Statistik
            total_transaksi = len(st.session_state.riwayat)
            total_pengeluaran = sum(t['total'] for t in st.session_state.riwayat)
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Total Transaksi", total_transaksi)
            with col2:
                st.metric("Total Pengeluaran", f"Rp{total_pengeluaran:,.0f}")
            
            # Tombol reset riwayat
            if st.button("🗑️ Hapus Semua Riwayat", type="secondary"):
                st.session_state.riwayat = []
                st.rerun()

    # Footer
    st.sidebar.markdown("---")
    st.sidebar.info("© 2025 Bloom Car Rental")
    
    # Debug info (opsional)
    if st.sidebar.checkbox("Show Debug Info"):
        st.sidebar.write("Session State:", st.session_state.keys())

if __name__ == "__main__":
    main()
