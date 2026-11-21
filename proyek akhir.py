while True:
    print("\n=======================")
    print("    FASHION STORE")
    print("=======================")

    print("1. Tampilkan Daftar Produk")
    print("2. Cari Produk")
    print("3. Tambahkan ke Keranjang")
    print("4. Lihat Keranjang")
    print("5. Checkout")
    print("6. Riwayat Transaksi")
    print("7. Keluar")
    
    print("=======================")

    pilihan = input("Pilih menu (1-7): ")

    if pilihan == "1":
        print("Anda memilih Daftar Produk")
        produk = [
            {
                "nama":"Kaos Polos",
                "kategori":"Atasan",
                "harga":60000,
                "stok":35
            },
            {
                "nama":"Kemeja Flanel",
                "kategori":"Atasan",
                "harga":100000,
                "stok":20
            },
            {
                "nama":"Celana Jeans",
                "kategori":"Bawahan",
                "harga":160000,
                "stok":15
            },
            {
                "nama":"Celana Training",
                "kategori":"Bawahan",
                "harga":120000,
                "stok":10
            },
            {
                "nama":"Sepatu Converse",
                "kategori":"Sepatu",
                "harga":240000,
                "stok":10
            }
        ]
        def tampilkan_produk():
            print("----=> DAFTAR PRODUK <=----")
            nomor = 1
            for p in produk:
                print(f"|Nomor {nomor}|")
                print("Nama     :",p["nama"])
                print("Kategori :",p["kategori"])
                print("Harga    : Rp",p["harga"])
                print("Stok     :",p["stok"])
                print("---------------------------")
                nomor += 1
        tampilkan_produk()

    elif pilihan == "2":
        print("Anda memilih Cari Produk")

        cari = input("Masukkan nama produknya: ").lower()
        ditemukan = False
        for p in produk:
            if cari in p["nama"].lower():
                print("\nProduk ditemukan!")
                print("Nama     :",p["nama"])
                print("Harga    : Rp",p["harga"])
                print("Stok     :",p["stok"])
                ditemukan = True

        if ditemukan == False:
            print("Produk tidak ditemukan! Coba lagi")

    elif pilihan == "3":
        print("Anda memilih Tambahkan ke Keranjang")

    elif pilihan == "4":
        print("Anda memilih Lihat Keranjang")

    elif pilihan == "5":
        print("Anda memilih Checkout")

    elif pilihan == "6":
        print("Anda memilih Riwayat Transaksi")

    elif pilihan == "7":
        print("Terima ksaih telah berbelanja:)")
        break
    else:
        print("Pilihan tidak valid! Pilih (1-7)")