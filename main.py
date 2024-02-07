from models import get_alldata
from models import custemer_table
from models import dine_in
from models import pesanan_and_custemer_details
from models import login_sql
from models import get_data_penjualan
from models import dine_in_pesanan
from models import take_away_pesanan
from models import delivered_pesanan
# from models import dine_in_admin
# from models import take_away_admin
# from models import delivered_admin
from datetime import datetime
from flask import redirect, url_for, jsonify
import json



def logout(session):
    session.pop('id_Custemer', None)
    return redirect(url_for('handle_main')) 



def login(request, template, session):
    if request.method == 'GET':
        return template('login.html')
    if request.method == 'POST':
        email = request.form.get("email")
        password  = request.form.get("password")
        datalogin = [email, password]
        print(datalogin)

        if all(data.strip() for data in datalogin):
            id, Email = login_sql(email,  password)
            if id == 0 and Email == "":
                message = "Email dan Passward Salah"
                return template('login.html', messageEmail=message)
            # meniympan data dalam sesi
            session['id_Custemer'] = id
            return redirect(url_for('handle_addandbuy', id=session['id_Custemer']))
        else:
            message = "Data Tidak Boleh Kosong!"
        return template('login.html', message=message)


def signup(request, template):
    if request.method == 'GET':
        return template("signup.html")
    if request.method == 'POST':
        name = request.form.get("nama")
        email = request.form.get("email")
        password = request.form.get("password")
        number = request.form.get("hp")
        address = request.form.get("alamat")
        dataform = [name, email, number, address, password]
        print(dataform)

        if all(data.strip() for data in dataform):
            now = datetime.now()
            duplikasi = custemer_table(dataform, now)
            if duplikasi == "" or duplikasi is None:
                succesfuly = "Registrasi berhasil silahkan Login"
                return template('signup.html', succesfuly=succesfuly)
            else:
                return template("signup.html", duplikasi=duplikasi)
        else:
           message = "Data tidak boleh kosong!"
        return template('signup.html', message=message)



def home_page(request, template, session):
    if request.method == 'GET':
        nama, harga = get_alldata()
        data = [nama, harga]
        if 'id_Custemer' in session and session['id_Custemer'] is not None:
            logout = True
            return template("main.html", data=data, logout=logout)
        else:
            return template("main.html", data=data)


def addandbuy_page(request, template, session):
    if 'id_Custemer' in session and session['id_Custemer'] is not None:
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
            dataPesanan = {}
            dataPemesan = {}
            datajson = request.get_json()
            for key, value in datajson.items():
                if isinstance(value, dict):
                    dataPesanan[key] = value
                else:
                    dataPemesan[key] = value
            session['pesanan'] = dataPesanan
            session['statusPesanan'] = dataPemesan
            print(dataPesanan)
            print(dataPemesan)

            return jsonify({'message':'berhasil mengirim data'})
    else:
        return redirect(url_for('handle_login'))


def payment_method_page(request, template, session):
    if 'id_Custemer' in session and session['id_Custemer'] is not None:
        referrer = request.referrer 
        if referrer and '/pesan/addandbuy' in referrer:
            if request.method == "GET":
                dataPesanan = session['pesanan']
                dataPemesan = session['statusPesanan']
                return template('payment.html', dataPesanan=dataPesanan, dataPemesan=dataPemesan)
            elif request.method == "POST":
                datajson = request.get_json()  
                print(datajson)
                time = datetime.now()
                id_custemer = session['id_Custemer'] 
                list_idpesanan = pesanan_and_custemer_details(datajson['pemesanan'], datajson['pesanan'], datajson['payment'], time, id_custemer)
                # print(list_idpesanan)
                # if datajson['pemesanan']['opsi pembelian'] == "Dine In":
                #     dine_in_pesanan(id_custemer, list_idpesanan)
                # elif datajson['pemesanan']['opsi pembelian'] == "Take Away":
                #     take_away_pesanan(id_custemer, list_idpesanan)
                # elif datajson['pemesanan']['opsi pembelian'] == "Delivered":
                #     delivered_pesanan(id_custemer, list_idpesanan)
                return jsonify({"message": "berhasil mengirim data"})
        else:
            return redirect(url_for('handle_addandbuy'))
    else:
        return redirect(url_for('handle_login'))


def admin_page(request, template):
    if request.method == "GET" :
        email, pembelian, harga_pembelian, jumlah_pembelian, total_harga_pembelian, waktu, opsi_pembelian, biaya_layanan, ongkos_kirim, payment_method = get_data_penjualan()
        items = [email, pembelian, harga_pembelian, jumlah_pembelian, total_harga_pembelian, waktu, opsi_pembelian, biaya_layanan, ongkos_kirim, payment_method]
        print(items)
        return template('admin.html', items=items)

# def dine_in_admin_page(request, template):
#     if request.method == "GET":
#         item = dine_in_admin()
#         data = item
#         print(data)
#         return template('dine_in.html', item=item)
        




    
    





