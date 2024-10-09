fruit_list={
    "name": ["apple","orange","grape"], 
    "price": [10000,15000,20000],
    "stock":[10,10,10]
}

print("selamat datang di pasar buah")
i=1
while 1<=i<=5:
    print("\nlist menu: ")
    print("1.menampilkan daftar buah")
    print("2.menambahkan buah")
    print("3.menghapus buah")
    print("4.membeli buah")
    print("5.exit program")
    i=int(input("\nmasukkan menu angka yang akan dijalankan: "))
    if i==1:
        print("\ndaftar nama buah")
        print("index |  nama buah |  harga  |  stok")
        for i in range(len(fruit_list["name"])):
            print(f'{i}     |   {fruit_list["name"][i]}   |   {fruit_list["price"][i]}   |   {fruit_list["stock"][i]}  ')
    elif i==2:
        print("\nmenambahkan buah")
        nama_buah=input("masukkan nama buah: ")
        stock_buah=int(input("masukkan stock buah: "))
        harga_buah=int(input("masukkan harga buah: "))
        fruit_list["name"].append(nama_buah)
        fruit_list["stock"].append(stock_buah)
        fruit_list["price"].append(harga_buah)
        print("\ndaftar nama buah")
        print("index |  nama buah |  harga  |  stok")
        for i in range(len(fruit_list["name"])):
            print(f'{i}     |   {fruit_list["name"][i]}   |   {fruit_list["price"][i]}   |   {fruit_list["stock"][i]}  ')
    elif i==3:
        print("\nmenghapus buah")
        print("\ndaftar nama buah")
        print("index |  nama buah |  harga  |  stok")
        for i in range(len(fruit_list["name"])):
            print(f'{i}     |   {fruit_list["name"][i]}   |   {fruit_list["price"][i]}   |   {fruit_list["stock"][i]}  ')
        index_remove=int(input("\nmasukkan index buah yang akan dihapus: "))
        fruit_list["name"].pop(index_remove)
        fruit_list["stock"].pop(index_remove)
        fruit_list["price"].pop(index_remove)
        print("\ndaftar nama buah")
        print("index |  nama buah |  harga  |  stok")
        for i in range(len(fruit_list["name"])):
            print(f'{i}     |   {fruit_list["name"][i]}   |   {fruit_list["price"][i]}   |   {fruit_list["stock"][i]}  ')
    elif i==4:
        print("membeli buah")
        print("\ndaftar nama buah")
        print("index |  nama buah |  harga  |  stok")
        for i in range(len(fruit_list["name"])):
            print(f'{i}     |   {fruit_list["name"][i]}   |   {fruit_list["price"][i]}   |   {fruit_list["stock"][i]}  ')
        option="ya"
        total_pay=0
        list_buy={"name":[],"price":[],"stock":[]}
        while option=="ya":
            buy_fruit=int(input("masukkan index buah yang ingin dibeli:"))
            if buy_fruit<=len(fruit_list["name"])-1:
                stock_buy=int(input("masukkan jumlah buah yang ingin dibeli:"))
                if stock_buy<=fruit_list["stock"][buy_fruit]:
                    fruit_list["stock"][buy_fruit]=fruit_list["stock"][buy_fruit]-stock_buy
                    list_buy["name"].append(fruit_list["name"][buy_fruit])
                    list_buy["price"].append(fruit_list["price"][buy_fruit])
                    list_buy["stock"].append(stock_buy)
                else:
                    print(f"stok buah tidak cukup, stock {fruit_list["name"][buy_fruit]} tinggal  {fruit_list["stock"][buy_fruit]}")
            else:
                print("index tidak ada dalam daftar")
            print("isi chart: ")
            print("nama    |   harga   |   qty")
            for i in range(len(list_buy["name"])):
                print(f'{list_buy["name"][i]}   |   {list_buy["price"][i]}   |   {list_buy["stock"][i]}  ')
            option=input("mau beli yang lain?(ya/tidak) ")
        else:
            for i in range (len(list_buy["name"])):
                total_pay=total_pay+(list_buy["price"][i]*list_buy["stock"][i])
            print("total yang harus dibayar: ", total_pay)
            pay=0
            while total_pay>pay:
                pay=int(input("\nmasukkan jumlah uang:"))
                if total_pay>pay:
                    mines_money=total_pay-pay
                    print("transaksi anda dibatalkan")
                    print(f"uang kurang sebesar {mines_money}\n\n")
                elif total_pay==pay:
                    print("terimakasih\n\n")
                else:
                    surplus_money=pay-total_pay
                    print("terimakasih")
                    print(f"\nuang kembali anda: {surplus_money}\n\n")
    elif i==5:
        print("exit program")
        break
    else:
        print("menu tidak tersedia")
        break