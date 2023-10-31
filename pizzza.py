# Tampilkan menu pizza
print("Menu Pizza:")
print("1. Margherita")
print("2. Pepperoni")
print("3. Mushroom")
print("4. Veggie")

# Meminta input dari pelanggan
pilihan_pizza = int(input("Silakan pilih nomor pizza yang ingin Anda pesan: "))

# Proses pemilihan pizza
if pilihan_pizza == 1:
    pizza = "Margherita"
    harga_pizza = 43000
elif pilihan_pizza == 2:
    pizza = "Pepperoni"
    harga_pizza = 50000
elif pilihan_pizza == 3:
    pizza = "Mushroom"
    harga_pizza = 45000
elif pilihan_pizza == 4:
    pizza = "Veggie"
    harga_pizza = 44000
else:
    print("Pilihan pizza tidak valid. Silakan pilih nomor yang benar.")
    pizza = ""
    harga_pizza = 0.00

# Proses pilihan crust
if pizza != "":
    print("Pilihan Crust:")
    print("1. Thin Crust")
    print("2. Thick Crust")
    pilihan_crust = int(input("Silakan pilih nomor crust yang Anda inginkan: "))

    if pilihan_crust == 1:
        crust = "Thin Crust"
        harga_crust = 15000
    elif pilihan_crust == 2:
        crust = "Thick Crust"
        harga_crust = 23000
    else:
        print("Pilihan crust tidak valid. Menggunakan Thin Crust secara default.")
        crust = "Thin Crust"
        harga_crust = 22000

    # Proses pilihan topping
    print("Pilihan Topping:")
    print("1. Pepperoni")
    print("2. Jamur")
    print("3. Keju Tambahan")
    print("4. Tanpa Topping Tambahan")
    pilihan_topping = int(input("Silakan pilih nomor topping yang Anda inginkan: "))

    topping = ""
    harga_topping = 0.00
    if pilihan_topping == 1:
        topping = "Pepperoni"
        harga_topping = 10000
    elif pilihan_topping == 2:
        topping = "Jamur"
        harga_topping = 13000
    elif pilihan_topping == 3:
        topping = "Keju Tambahan"
        harga_topping = 15000

    # Hitung total harga
    total_harga = (harga_pizza + harga_crust + harga_topping)

    # Meminta input jumlah pesanan
    jumlah = int(input(f"Berapa banyak {pizza} yang ingin Anda pesan? "))
    total_harga *= jumlah

    print(f"Anda memesan {jumlah} {pizza} dengan {crust}, {topping}. Total harga: ${total_harga:.2f}")
   