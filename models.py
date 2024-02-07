from connection import db_connection
from itertools import groupby
from operator import itemgetter

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

# insert data to tabel pesanan
def dine_in(datajson, time):
    data = datajson

    conn, cursor = db_connection()
    
    query = "insert into pesanan(pembelian, harga_pembelian, jumlah_pembelian, total_harga_pembelian, waktu) values(%s, %s, %s, %s, %s)"
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


# INSER DATA CUSTEMER TO TABEL CUSTEMER_TAKE_AWAY
def  custemer_table(dataform, time):
    data = dataform 
    conn, cursor = db_connection()

    query = "select email from custemer where email = %s"
    cursor.execute(query, (data[1],))
    email = cursor.fetchone()

    if email is not None:
        message = "Email sudah pernah digunakan!"
        return message
    else:
        query = "insert into custemer(nama, email, nohp, address, waktu, password) value(%s, %s, %s, %s, %s, %s)"
        parameters = [data[0], data[1], data[2], data[3], time, data[4]]
        cursor.execute(query, parameters)

    cursor.close()
    conn.commit()
    conn.close()


# INSERT INTO CUSTMER DETAIL AND PESANAN BY ID 
def pesanan_and_custemer_details(pemesanan, pesanan, payment, time, id_custemer):
    idpesanan_list = []

    conn, cursor = db_connection()

    query = "insert into pesanan(pembelian, harga_pembelian, jumlah_pembelian, total_harga_pembelian, waktu, opsi_pembelian, biaya_layanan, ongkos_kirim, payment_method) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    for key, value in pesanan.items():
        pembelian = value['name']
        harga_pembelian = value['price']
        jumlah_pembelian = value['quantity']
        total_harga_pembelian = value['totalPerItem']

        ongkos_kirim = pemesanan.get('ongkos kirim', '') # get() nilai default kosong jika kunci tidak ada

        parameters = (pembelian, harga_pembelian, jumlah_pembelian, total_harga_pembelian, time, pemesanan['opsi pembelian'], pemesanan['biaya layanan'], ongkos_kirim, payment)

        cursor.execute(query, parameters)

        idpesanan = cursor.lastrowid
        idpesanan_list.append(idpesanan)

    cursor.close()
    conn.commit()

    conn, cursor = db_connection()

    query = "insert into custemer_details(id_custemer, id_pesanan) values(%s, %s)"
    for idpesanan in idpesanan_list:    
        parameters = [id_custemer, idpesanan]
        cursor.execute(query, parameters)

    

    cursor.close()
    conn.commit()
    return idpesanan_list

# dine in pesanan
# def dine_in_pesanan(id_Custemer, list_idpesanan):
#     conn, cursor = db_connection()

#     query = "insert into dine_in_details(id_custemer, id_pesanan) values(%s, %s)"
#     for idPesanan in list_idpesanan:
#         parameters = (id_Custemer, idPesanan)
#         cursor.execute(query, parameters)
    
#     conn.commit()
#     cursor.close()

# take away pesanan
# def take_away_pesanan(id_Custemer, list_idpesanan):
#     conn, cursor = db_connection()

#     query = "insert into take_away_details(id_custemer, id_pesanan) values(%s, %s)"
#     for idPesanan in list_idpesanan:
#         parameters = (id_Custemer, idPesanan)
#         cursor.execute(query, parameters)

#     conn.commit()
#     cursor.close()

# delivered pesanan
# def delivered_pesanan(id_custemer, list_idpesanan):
#     conn, cursor = db_connection()

#     query = "insert into delivered_details(id_custemer, id_pesanan) values(%s, %s)"
#     for idPesanan in list_idpesanan:
#         parameters = [id_custemer, idPesanan]
#         cursor.execute(query, parameters)
    
#     conn.commit()
#     cursor.close()

# login
def login_sql(email, password):
    conn, cursor = db_connection()

    query = "select id, email from custemer where password = %s"
    cursor.execute(query, [password])
    result = cursor.fetchall()

    id = 0
    Email = ""

    for row in result: 
        id = row[0]
        Email = row[1]
    
    cursor.close()
    conn.close()

    return id, Email


# admin fitur penjualan 
def get_data_penjualan():
    conn, cursor = db_connection()

    email_list = []
    pembelian_list = []
    harga_pembelian_list = []
    jumlah_pembelian_list = []
    total_harga_pembelian_list = []
    waktu_list = []
    opsi_pembelian_list = []
    biaya_layanan_list = []
    ongkos_kirim_list = []
    payment_method_list = []

    query1 = "select email, pembelian, harga_pembelian, jumlah_pembelian, total_harga_pembelian, pesanan.waktu, opsi_pembelian, biaya_layanan, ongkos_kirim, payment_method  from custemer_details"
    query2 = " join custemer on (custemer_details.id_custemer = custemer.id)"
    query3 = " join pesanan on (custemer_details.id_pesanan = pesanan.id)"
    query4 = "order by pesanan.waktu desc"

    cursor.execute(query1 + query2 + query3 + query4)
    result  = cursor.fetchall()

    for row in result:
        email = row[0]
        pembelian = row[1]
        harga_pembelian = row[2]
        jumlah_pembelian = row[3]
        total_harga_pembelian = row[4]
        waktu = row[5]
        opsi_pembelian = row[6]
        biaya_layanan = row[7]
        ongkos_kirim = row[8]
        payment_method = row[9]
        email_list.append(email)
        pembelian_list.append(pembelian)
        harga_pembelian_list.append(harga_pembelian)
        jumlah_pembelian_list.append(jumlah_pembelian)
        total_harga_pembelian_list.append(total_harga_pembelian)
        waktu_list.append(waktu)
        opsi_pembelian_list.append(opsi_pembelian)
        biaya_layanan_list.append(biaya_layanan)
        ongkos_kirim_list.append(ongkos_kirim)
        payment_method_list.append(payment_method)

    cursor.close()
    conn.close()

    return email_list, pembelian_list, harga_pembelian_list, jumlah_pembelian_list, total_harga_pembelian_list, waktu_list, opsi_pembelian_list, biaya_layanan_list, ongkos_kirim_list, payment_method_list
        

# dine in admin
# def dine_in_admin():
#     conn, cursor = db_connection()
#     all_data = []
#     email_list = []
#     nohp_list = []
#     pembelian_list = []
#     jumlah_pembelian_list = []
#     waktu_list = []

#     query1 = "select custemer.email, custemer.nohp, pembelian, jumlah_pembelian, pesanan.waktu from dine_in_details"
#     query2 = " join custemer on (dine_in_details.id_custemer = custemer.id)"
#     query3 = " join pesanan on (dine_in_details.id_pesanan = pesanan.id)"
#     query4 = "order by pesanan.waktu desc;"

#     cursor.execute(query1 + query2 + query3 + query4)
#     result = cursor.fetchall()

#     for row in result:
#         email = row[0]
#         nohp = row[1]
#         pembelian = row[2]
#         jumlah_pembelian = row[3]
#         waktu = row[4]
#         email_list.append(email)
#         nohp_list.append(nohp)
#         pembelian_list.append(pembelian)
#         jumlah_pembelian_list.append(jumlah_pembelian)
#         waktu_list.append(waktu)
#     all_data = [email_list, pembelian_list, jumlah_pembelian_list, waktu_list]
#     # Mengelompokkan data berdasarkan waktu yang sama
#     grouped_data = [list(group) for key, group in groupby(zip(*all_data), key=itemgetter(-1))]
#     # Menggabungkan data setelah dielompokkan
#     result = [list(zip(*group))[:-1] for group in grouped_data]
#     conn.close()
#     cursor.close()

#     return result


# Take Away admin
# def take_away_admin():
#     conn, cursor = db_connection()
#     all_data = []
#     email_list = []
#     nohp_list = []
#     pembelian_list = []
#     jumlah_pembelian_list = []
#     waktu_list = []    
    
#     query1 = "select custemer.email, custemer.nohp, pembelian, jumlah_pembelian, pesanan.waktu from take_away_details"
#     query2 = " join custemer on(take_away_details.id_custemer = custemer.id)"
#     query3 = " join pesanan on(take_away_details.id_pesanan = pesanan.id)"
#     query4 = "order by pesanan.waktu desc;"
#     cursor.execute(query1 + query2 + query3 + query4)
#     result = cursor.fetchall()

#     for row in result:
#         email = row[0]
#         nohp = row[1]
#         pembelian = row[2]
#         jumlah_pembelian = row[3]
#         waktu = row[4]
#         email_list.append(email)
#         nohp_list.append(nohp)
#         pembelian_list.append(pembelian)
#         jumlah_pembelian_list.append(jumlah_pembelian)
#         waktu_list.append(waktu)
#     all_data = [email_list, pembelian_list, jumlah_pembelian_list, waktu_list]
#     # Mengelompokkan data berdasarkan waktu yang sama
#     grouped_data = [list(group) for key, group in groupby(zip(*all_data), key=itemgetter(-1))]
#     # Menggabungkan data setelah dielompokkan
#     result = [list(zip(*group))[:-1] for group in grouped_data]
#     print(result)

#     cursor.close()
#     conn.close()

#     return result


# delivered admin
# def delivered_admin():
#     conn, cursor = db_connection()
#     all_data = []
#     email_list = []
#     nohp_list = []
#     pembelian_list = []
#     jumlah_pembelian_list = []
#     waktu_list = []    
    
#     query1 = "select custemer.email, custemer.nohp, pembelian, jumlah_pembelian, pesanan.waktu from delivered_details"
#     query2 = " join custemer on(delivered_details.id_custemer = custemer.id)"
#     query3 = " join pesanan on(delivered_details.id_pesanan = pesanan.id)"
#     query4 = "order by pesanan.waktu desc;"
#     cursor.execute(query1 + query2 + query3 + query4)
#     result = cursor.fetchall()

#     for row in result:
#         email = row[0]
#         nohp = row[1]
#         pembelian = row[2]
#         jumlah_pembelian = row[3]
#         waktu = row[4]
#         email_list.append(email)
#         nohp_list.append(nohp)
#         pembelian_list.append(pembelian)
#         jumlah_pembelian_list.append(jumlah_pembelian)
#         waktu_list.append(waktu)
#     all_data = [email_list, pembelian_list, jumlah_pembelian_list, waktu_list]
#     # Mengelompokkan data berdasarkan waktu yang sama
#     grouped_data = [list(group) for key, group in groupby(zip(*all_data), key=itemgetter(-1))]
#     # Menggabungkan data setelah dielompokkan
#     result = [list(zip(*group))[:-1] for group in grouped_data]

#     cursor.close()
#     conn.close()
#     print(result)

#     return result
        
        





