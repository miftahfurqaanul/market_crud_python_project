#Create prrice list
price_apple = 10000
price_orange = 15000
price_grape = 20000

#stock feature
stock_apple = 30
stock_orange = 40
stock_grape = 50

#while condition
amount_apple = int(input("Masukkan Jumlah Apel: "))
while amount_apple > stock_apple:
    print("Jumlah yang dimasukkan terlalu banyak")
    amount_apple = int(input("Masukkan Jumlah Apel: "))

amount_orange = int(input("Masukkan Jumlah jeruk: "))
while amount_orange > stock_orange:
    print("Jumlah yang dimasukkan terlalu banyak")
    amount_orange = int(input("Masukkan Jumlah jeruk: "))

amount_grape = int(input("Masukkan Jumlah anggur: "))
while amount_grape > stock_grape:
    print("Jumlah yang dimasukkan terlalu banyak")
    amount_grape = int(input("Masukkan Jumlah anggur: "))

#calculate price 
price_apple_total = price_apple * amount_apple
price_orange_total = price_orange * amount_orange
price_grape_total = price_grape * amount_grape

#show the detail 
print()
print("Detail Belanja")
print()
print(f"Apel: {amount_apple} x {price_apple} = {price_apple_total}")
print(f"Jeruk: {amount_orange} x {price_orange} = {price_orange_total}")
print(f"Anggur: {amount_grape} x {price_grape} = {price_grape_total}")

print()

print("Total Belanja: ", price_apple_total+price_orange_total+price_grape_total)

print()

#Create ask amount of money
yangdibayar = int(input("Masukkan  Jumlah Uang : "))

total_beli = price_apple_total+price_orange_total+price_grape_total

#condition 1 2 dan 3
while yangdibayar < total_beli:
    selisih_kurang_bayar = total_beli - yangdibayar
    print(f"Uang Kurang Sebesar {selisih_kurang_bayar}")
    yangdibayar = int(input("Masukkan  Jumlah Uang : "))

if yangdibayar == total_beli:
    print("Terima Kasih")
else:
    lebih_bayar =  yangdibayar - total_beli
    print(f"Uang Kembalian Anda Sebesar {lebih_bayar}")
    print("Terima Kasih ")


