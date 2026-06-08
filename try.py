class Barang:
    def __init__(self, jenis, merk, stok, harga=None):
        self.jenis = jenis
        self.merk = merk
        self.stok = stok
        self.harga = harga  

    def tampilkan_info(self):
        print(f"Jenis Barang : {self.jenis}")
        print(f"Merk         : {self.merk}")
        print(f"Stok         : {self.stok}")
        if self.harga is not None:
            print(f"Harga        : Rp{self.harga:,}")
        print("-" * 35)

    def terjual(self, jumlah):
        if jumlah <= 0:
            print("Jumlah penjualan harus lebih dari 0!")
            return

        if jumlah <= self.stok:
            self.stok -= jumlah
            if self.harga is not None:
                total = jumlah * self.harga
                print(f"{jumlah} {self.jenis} ({self.merk}) berhasil dijual.")
                print(f"Total penjualan: Rp{total:,}")
            else:
                print(f"{jumlah} {self.jenis} ({self.merk}) berhasil dijual.")
        else:
            print(f"Stok {self.jenis} ({self.merk}) tidak mencukupi!")
        print(f"Sisa stok: {self.stok}")
        print("-" * 35)



class BarangIterator:
    def __init__(self, daftar_barang):
        self.daftar = daftar_barang
        self.index = 0

    def __next__(self):
        if self.index < len(self.daftar):
            barang = self.daftar[self.index]
            self.index += 1
            return barang
        else:
            raise StopIteration


class BarangIterable:
    def __init__(self, daftar_barang):
        self.daftar = daftar_barang

    def __iter__(self):
        return BarangIterator(self.daftar)


# ==== PROGRAM UTAMA ====
def main():
    print("=" * 55)
    print("   SISTEM PENJUALAN BARANG E-COMMERCE DEV ACADEMY")
    print("   Dibuat oleh: Kornelius Sitompul (NIM 241112624)")
    print("=" * 55)
    jenis_barang = ["Hand Sanitizer", "Ban Mobil", "Buah-buahan", "Botol Bayi"]
    daftar_barang = []

    while True:
        print("\n===== MENU E-COMMERCE DEV ACADEMY =====")
        print("1. Tambah Barang")
        print("2. Jual Barang")
        print("3. Lihat Daftar Barang (pakai iterator)")
        print("4. Keluar")
        pilihan = input("Pilih menu (1-4): ").strip()

        if pilihan == "1":
            print("\n=== TAMBAH BARANG BARU ===")
            print("Pilih jenis barang:")
            for i, jenis in enumerate(jenis_barang, start=1):
                print(f"{i}. {jenis}")

            try:
                pilih_jenis = int(input("Masukkan nomor jenis barang: "))
                if 1 <= pilih_jenis <= len(jenis_barang):
                    jenis = jenis_barang[pilih_jenis - 1]
                    merk = input("Masukkan nama/merk barang: ").strip()
                    stok = int(input("Masukkan stok: "))

                    if stok < 0:
                        print("Stok harus bernilai positif!")
                        continue

                    if jenis == "Buah-buahan":
                        barang_baru = Barang(jenis, merk, stok)
                    else:
                        harga = int(input("Masukkan harga per unit: "))
                        if harga < 0:
                            print("Harga harus bernilai positif!")
                            continue
                        barang_baru = Barang(jenis, merk, stok, harga)

                    daftar_barang.append(barang_baru)
                    print(f"Barang '{merk}' berhasil ditambahkan!")
                else:
                    print("Nomor jenis barang tidak valid!")
            except ValueError:
                print("Input tidak valid! Gunakan angka untuk pilihan, stok, dan harga.")

        elif pilihan == "2":
            print("\n=== PENJUALAN BARANG ===")
            if not daftar_barang:
                print("Belum ada barang yang tersedia untuk dijual.")
                continue

            for i, b in enumerate(daftar_barang, start=1):
                if b.harga is not None:
                    print(f"{i}. ({b.merk}) - Stok: {b.stok} - Harga: Rp{b.harga:,}")
                else:
                    print(f"{i}. ({b.merk}) - Stok: {b.stok} ")

            try:
                pilih = int(input("Pilih nomor barang: "))
                jumlah = int(input("Masukkan jumlah yang dijual: "))
                if 1 <= pilih <= len(daftar_barang):
                    daftar_barang[pilih - 1].terjual(jumlah)
                else:
                    print("Nomor barang tidak valid!")
            except ValueError:
                print("Input harus berupa angka!")

        elif pilihan == "3":
            print("\n=== DAFTAR BARANG (ITERATOR) ===")
            if not daftar_barang:
                print("Belum ada barang yang terdaftar.")
            else:
                iterable = BarangIterable(daftar_barang)
                iterator = iter(iterable)
                try:
                    while True:
                        barang = next(iterator)
                        barang.tampilkan_info()
                except StopIteration:
                    print("Semua barang telah ditampilkan.")

        elif pilihan == "4":
            print("\nTerima kasih telah menggunakan sistem E-Commerce Dev Academy.")
            break

        else:
            print("Pilihan salah! Silakan coba lagi.")


if __name__ == "__main__":
    main()
