# create price list
price_apple = 10000
price_orange = 15000
price_grape = 20000

# create user input
amount_apple = input("Masukkan Jumlah Apple = ")
amount_orange = input("Masukkan Jumlah Orange = ")
amount_grape = input("Masukkan Jumlah Grape = ")

# convert user input to integer
amount_apple = int(amount_apple)
amount_orange = int(amount_orange)
amount_grape = int(amount_grape)

# calculate price
price_apple_total = price_apple * amount_apple
price_orange_total = price_orange * amount_orange
price_grape_total = price_grape * amount_grape

# show the detail
print("Detail Belanja")
print(f"Apel = {amount_apple} x { price_apple} = {price_apple_total}")
print(f"Orange = {amount_orange} x { price_orange} = {price_orange_total}")
print(f"Apel = {amount_grape} x { price_grape} = {price_grape_total}")

print("Total Belanja = ", price_apple_total+price_orange_total+price_grape_total)

uang_pelanggan = int(input("Masukkan jumlah uang = "))
total_belanja = price_apple_total+price_orange_total+price_grape_total
if uang_pelanggan == total_belanja:
    print("Terima Kasih")
elif uang_pelanggan < total_belanja:
    kekurangan = total_belanja - uang_pelanggan
    print(f"Transaksi anda dibatalkan. Anda kurang {kekurangan}")
else:
    kelebihan = uang_pelanggan - total_belanja
    print("Terima Kasih")
    print(f"Uang Kembali Anda = {kelebihan}")