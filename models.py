from connection import db_connection

def get_datamakanan(input):
    conn, cursor = db_connection()

    query = "SELECT nama, harga FROM makanan WHERE nama = %s"
    cursor.execute(query, input)
    result = cursor.fetchall()

    for row in result:
        nama = row[0]
        harga = row[1]

    # print(f"Nama: {nama}, harga: {harga}")

    # Selalu tutup cursor dan koneksi setelah selesai
    cursor.close()
    conn.close()
    return nama, harga

if __name__ == "__main__":
    get_datamakanan()





def get_datadrink(input):
    conn, cursor = db_connection()

    query = "select nama, harga from drink where nama = %s"
    cursor.execute(query, input)
    result = cursor.fetchall()

    for row in result:
        nama = row[0]
        harga = row[1]

    cursor.close()
    conn.close()
    return nama, harga

if __name__ == "__main__":
    get_datadrink()



def get_datadessert(input):
    conn, cursor = db_connection()

    query = "select nama, harga from dessert where nama = %s"
    cursor.execute(query, input)
    result = cursor.fetchall()

    for row in result:
        nama = row[0]
        harga = row[1]

    cursor.close()
    conn.close()

    return nama, harga

if __name__ == "__main__":
    get_datadessert()



# mengambil data dari database
def get_alldata():
    conn, cursor = db_connection()

    query = "SELECT nama, harga FROM makanan" 
    cursor.execute(query)
    result = cursor.fetchall()

    nama_list = []
    harga_list = []

    for row in result:
        nama = row[0]
        harga = row[1]
        nama_list.append(nama)
        harga_list.append(harga)


    cursor.close()
    conn.close()

    conn, cursor = db_connection()

    query = "SELECT nama, harga FROM minuman"
    cursor.execute(query)
    result = cursor.fetchall()

    for row in result:
        nama = row[0]
        harga = row[1]
        nama_list.append(nama)
        harga_list.append(harga)

    cursor.close()
    conn.close()

    conn, cursor = db_connection()

    query = "SELECT nama, harga FROM dessert"
    cursor.execute(query)
    result = cursor.fetchall()

    for row in result:
        nama = row[0]
        harga = row[1]
        nama_list.append(nama)
        harga_list.append(harga)

    cursor.close()
    conn.close()


    return nama_list, harga_list

# insert data to tabel dine_in
def dine_in(datajson, time):
    data = datajson

    conn, cursor = db_connection()
    
    query = "insert into  dine_in(pembelian, harga_pembelian, jumlah_pembelian, total_harga_pembelian, waktu) values(%s, %s, %s, %s, %s)"
    for key, value in data.items():
        pembelian = value['name']
        harga_pembelian = value['price']
        jumlah_pembelian = value['quantity']
        total_harga_pembelian = value['totalPerItem']

        print(pembelian, harga_pembelian, jumlah_pembelian, total_harga_pembelian, time)

        parameters = (pembelian, harga_pembelian, jumlah_pembelian, total_harga_pembelian, time)

        result = cursor.execute(query, parameters)
        print("query executed succesfuly : ", result)

    cursor.close()
    conn.commit()


