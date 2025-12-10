class Mobil:
    #Constructor
    def __init__(self, nama_mobil, seater, transmisi, harga_rental, jumlah_tersedia):
        self._nama_mobil = nama_mobil
        self._seater = seater     # 2 atau 3 seater
        self._transmisi = transmisi    # matic atau manual 
        self._harga_rental = harga_rental
        self._jumlah_tersedia = jumlah_tersedia 

# Getter
    @property
    def nama_mobil(self):
        return self._nama_mobil
    
    @property
    def seater(self):    
        return self._setaer 
    
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
        self._setaer = value
        
    @transmisi.setter
    def transmisi(self, value):
        self._transmisi = value
        
    @harga_rental.setter
    def harga_rental(self, value):
        self._harga_rental = value
        
    @jumlah_tersedia.setter
    def jumlah_tersedia(self, value):
        self._jumlah_tersedia = value(value)
        
# Hitung Biaya Sewa Berdasarkan Hari 
def hitung_biaya(self, hari):
    if hari <= 0:
        return 0
    elif hari < 7:
        diskon = 0.05
    else:
        diskon = 0.10
    total = self._harga_rental * hari * (1 - diskon)
    return total
    
if __name__ == "__main__":
    mobil1 = Mobil("Mazda 3", 5, "Matic", 500000, 1)
    print(mobil1.nama_mobil)
    print(mobil1.seater)
    print(mobil1.transmisi)
    print(mobil1.harga_rental)
    print(mobil1.jumlah_tersedia) 
    
    mobil2 = Mobil("BYD Seal", 5, "Matic", 700000, 1)
    print(mobil2.nama_mobil)
    print(mobil2.seater)
    print(mobil2.transmisi)
    print(mobil2.harga_rental)
    print(mobil2.jumlah_tersedia)
    
    mobil3 = Mobil("Pajero", 7, "Manual", 650000, 2)
    print(mobil3.nama_mobil)
    print(mobil3.seater)
    print(mobil3.transmisi)
    print(mobil3.harga_rental)
    print(mobil3.jumlah_tersedia)
    
    mobil4 = Mobil("Lexus", 7, "Matic", 750000, 1)
    print(mobil4.nama_mobil)
    print(mobil4.seater)
    print(mobil4.transmisi)
    print(mobil4.harga_rental)
    print(mobil4.jumlah_tersedia)
    
    mobil5 = Mobil("BMW 7 Series", 5, "Matic", 900000, 1)
    print(mobil5.nama_mobil)
    print(mobil5.seater)
    print(mobil5.transmisi)
    print(mobil5.harga_rental)
    print(mobil5.jumlah_tersedia)

# Array 2 dimensi (list of lists): Nama dan Harga Rental
data_singkat = [[mobil.nama_mobil, mobil.harga_rental] for mobil in daftar_mobil]
print("\n=== DAFTAR HARGA RENTAL ===")
for item in data_singkat:
    print(f"{item[0]} : Rp{item[1]:,}")
    
#Dictionary: Nama Mobil Sebagai Key dan Objek Sebagai Value 
dict_mobil = {mobil.nama_mobil.lower(): mobil for mobil in daftar_mobil}

#Looping 
while true:
    print("\n=== MENU RENTAL MOBIL ===")
    print("1. Lihat daftar mobil")
    print("2. Sewa mobil")
    print("3. Keluar")
    pilihan = input("Pilih menu (1/2/3):")
    
    if pilihan == "1":
        print("\n=== DAFTAR MOBIL TERSEDIA ===")
        for mobil in daftar_mobil:
            status = "Tersedia" if mobil.jumlah_tersedia > 0 else "Tidak Tersedia"
            print(f"{mobil.nama_mobil:6}, {mobil.transmisi}, {mobil.seater}, Rp{mobil.harga_rental:,}/hari, {status}")
            
    elif pilihan == "2":
        nama = input ("Masukkan nama mobil yang ingin disewa: ").lower().strip()
        if nama in dict_mobil:
            mobil = dict_mobil[nama]
            if mobil.jumlah_tersedia > 0:
                hari = int(input("Berapa hari yang ingin disewa? "))
                total = mobil.hitung_biaya(hari)
                mobil.jumlah_tersedia -= 1
                print(f"\n✅ Mobil {mobil.nama_mobil} telah Anda sewa selama {hari} hari ✅")
                print(f"Total biaya: Rp{total:, .0f}")
            else:
                print("Maaf, mobil telah disewa🙏🏻")
        else:
            print ("Maaf, mobil tidak ada dalam daftar🙅🏻‍♀️")
    elif pilihan == "3":
        print("Terima kasih telah menggunakan layanan kami. Sampai jumpa lagi😆👋🏻")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi‼️")
