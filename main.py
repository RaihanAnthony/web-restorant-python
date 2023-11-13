from models import get_alldata
from models import dine_in
from datetime import datetime
from flask import jsonify
# from models import get_datamakanan
# from models import get_datadrink
# from models import get_datadessert


def home_page(request, template):
    if request.method == 'GET':
        nama, harga = get_alldata()
        data = [nama, harga]
        print(data[0], data[1])
        return template("main.html", data=data)

def order_page(request, template):
    if request.method == 'GET':
        nama= request.args.get("nama")
        harga= request.args.get("harga")
        data = [nama, harga]
        print(nama, harga)
        return template("order.html", data=data)

def delivered_page(request, template):
    if request.method == 'GET':
        nama = request.args.get("nama")
        harga = request.args.get("harga")
        data = [nama, harga]
        return template("delivered.html", data=data)

def addandbuy_page(request, template):
    if request.method == 'GET':
        meals = request.args.get("meal")
        harga = request.args.get("harga")
        name = request.args.get("name")
        email = request.args.get("email")
        number = request.args.get("number")
        address = request.args.get("address")
        dataurl = [meals, harga, name, email, number, address]
        nama, harga = get_alldata()
        data = [nama, harga]
        return template("addandbuy.html", dataurl=data, data=data)
    if request.method == 'POST':
        datajson = request.get_json()
        print("isi data: ", datajson)
        now = datetime.now()
        dine_in(datajson, now)
        return jsonify({'message': 'Data berhasil diterima'})
        




# def fitur_food(request, template):
#     if request.method == 'GET':
#         input = "makanan"
#         nama, harga = get_alldata(input)
#         data = [nama, harga]
        
#         print(data[0], data[1])
#         return template("makanan.html", data=data)
#     elif request.method == 'POST':
#         nama = request.form.get('nama')
#         return template("makanan.html", nama=nama)


# def fitur_drink(request, template):
#     if request.method == 'GET':
#         input = "drink"
#         nama, harga = get_alldata(input)
#         data = [nama, harga]

#         print(data)

#         return template("minuman.html", data=data)
#     elif request.method == 'POST':
#         nama = request.form.get('nama')
#         return template("minuman.html", nama=nama)


# def fitur_dessert(request, template):
#     if request.method == 'GET':
#         input = "dessert"
#         nama, harga = get_alldata(input)
#         data = [nama, harga]

#         return template("dessert.html", data=data)
#     elif request.method == 'POST':
#         nama = request.form.get('nama')
#         return template("dessert.html", nama=nama)



# print("anda mau pesan apa")
# opsi = input("Food|Dessert|Drink : ")

# if opsi == "Food" or opsi =="food":
#     print("|=======================================|")
#     print("|          Meat Guy brother             |")
#     print("|              Food                     |")
#     print("|=======================================|")
#     print("|    Nama    |    Price   |   Rating    |")
#     print("|_______________________________________|")
#     print("|   Steak    | Rp.250,000 |    *****    |")
#     print("|   Pasta    | Rp.100,000 |    *****    |")
#     print("|   Burger   | Rp.80,000  |    *****    |")
#     print("|   Toast    | Rp.85,000  |    *****    |")
#     print("|=======================================|")
#     print("masukan nama makanan")
#     food = input("Food  Menu : ")
#     valuestuple = tuple(food.split(','))
#     nama, harga = get_datadrink(valuestuple)
#     amountfood = int(input("Berapa Banyak Makanan : "))
#     kalkulasi = harga * amountfood
#     print("Total Harga makanan : ", kalkulasi)
#     amountmoney = int(input("Total Uang : "))
#     kalkulasiamount = amountmoney - kalkulasi

#     print("|======================================|")
#     print("|          struct pembayaran           |")
#     print("|           Meat Guy brother           |")
#     print("|======================================|")
#     print("|                                      |")
#     print("|      Nama Makanan   = ", nama,"        |")
#     print("|      Jumlah Makanan = ", amountfood,"           |")
#     print("|      Total Harga    = ", kalkulasi,"       |")
#     print("|      Total uang     = ", amountmoney,"       |")
#     print("|    ===============================   |")
#     print("|   kembalian  :     ", kalkulasiamount,"          |")
#     print("|                                      |")
#     print("|======================================|")
#     print("|            Terima Kasih              |")
#     print("|         Telah Memesan Makanan        |")
#     print("|======================================|")
    
    
# elif opsi == "Dessert" or  opsi == "dessert" :
#     print("|=======================================|")
#     print("|          Meat Guy brother             |")
#     print("|             Dessert                   |")
#     print("|=======================================|")
#     print("|      Price   |    Harga   |   Rating  |")
#     print("|=======================================|")
#     print("|     Pancake  | Rp.150,000 |   *****   |")
#     print("|   Choco Plan | Rp.100,000 |   *****   |")
#     print("|   Apple Pie  | Rp.90,000  |   *****   |")
#     print("|   Cheesecake | Rp.105,000 |   *****   |")
#     print("|=======================================|")
#     dessert = input("Dessert Menu : ")
#     valuestuple = tuple(dessert.split(","))
#     nama, harga = get_datadessert(valuestuple)
#     amountdessert = int(input("Berapa Banyak Dessert : "))
#     kalkulasi = harga * amountdessert
#     print("Total Harga Dessert : ", kalkulasi)
#     amountmoney = int(input("Total Uang : "))
#     kalkulasiamount = amountmoney - kalkulasi

#     print("|======================================|")
#     print("|          struct pembayaran           |")
#     print("|           Meat Guy brother           |")
#     print("|======================================|")
#     print("|                                      |")
#     print("|      Nama Dessert   = ", nama,"       |")
#     print("|      Jumlah Makanan = ", amountdessert,"            |")
#     print("|      Total Harga    = ", kalkulasi,"       |")
#     print("|      Total uang     = ", amountmoney,"       |")
#     print("|    ===============================   |")
#     print("|     kembalian  :     ", kalkulasiamount,"        |")
#     print("|                                      |")
#     print("|======================================|")
#     print("|            Terima Kasih              |")
#     print("|         Telah Memesan Makanan        |")
#     print("|======================================|")
    

# elif opsi == "Drink" or opsi == "drink" : 
#     print("|=======================================|")
#     print("|          Meat Guy brother             |")
#     print("|             Drink                     |")
#     print("|=======================================|")
#     print("|     Nama     |      Harga   |  Rating |")
#     print("|  Lychee Tea  |   Rp.70,000  |  *****  |")
#     print("|  Ice Caramel |   Rp.80,000  |  *****  |")
#     print("|  Green Tea   |   Rp.60,000  |  *****  |")
#     print("|  Matcha Tea  |   Rp.65,000  |  *****  |")
#     print("|=======================================|")
#     drink = input("drink Menu : ")
#     valuestuple = tuple(drink.split(','))
#     nama, harga = get_datadrink(valuestuple)
#     amountdrink = int(input("berapa banyak minuman : "))
#     kalkulasi = harga * amountdrink
#     print("Total Harga Minuman : ", kalkulasi)
#     amountmoney = int(input("Total Uang : "))
#     kalkulasiamount = amountmoney - kalkulasi

#     print("|======================================|")
#     print("|          struct pembayaran           |")
#     print("|           Meat Guy brother           |")
#     print("|======================================|")
#     print("|                                      |")
#     print("|      Nama Drink     = ", nama,"       |")
#     print("|      Jumlah Drink   = ", amountdrink,"            |")
#     print("|      Total Harga    = ", kalkulasi,"       |")
#     print("|      Total uang     = ", amountmoney,"       |")
#     print("|    ===============================   |")
#     print("|     kembalian  :     ", kalkulasiamount,"        |")
#     print("|                                      |")
#     print("|======================================|")
#     print("|            Terima Kasih              |")
#     print("|         Telah Memesan Makanan        |")
#     print("|======================================|")

    
    
    
# else :
#     print("Daftar menu tidak ditemukan")
#     print("isi Food or Dessert or Drink")


    
    





