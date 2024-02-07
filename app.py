from main import home_page
from main import addandbuy_page
from main import payment_method_page
from main import admin_page
from main import login
from main import signup
from main import logout
from flask import Flask, request, render_template, session
from flask_bootstrap import Bootstrap

app = Flask(__name__, template_folder='view', static_folder='static')
app.config['SECRET_KEY'] = '087hvfbvbofh894g4r'
Bootstrap(app)

@app.route('/logout', methods=['POST'])
def handle_logout():
    return logout(session) 

@app.route('/login', methods=['GET', 'POST'])
def handle_login():
    return login(request, render_template, session)

@app.route('/signup', methods=['GET', 'POST'])
def handle_signup():
    return signup(request, render_template)

@app.route('/', methods=['GET', 'POST'])
def handle_main():
    return home_page(request, render_template, session)

@app.route('/pesan/addandbuy', methods=['GET', 'POST'])
def handle_addandbuy():
    return addandbuy_page(request, render_template, session)

@app.route('/pesan/addandbuy/paymentmethod', methods=['GET', 'POST'])
def handle_payment_method():
    return payment_method_page(request, render_template, session)

@app.route('/restorant/meetguybrother/admin', methods=['GET', 'POST'])
def handle_admin():
    return admin_page(request, render_template)

# @app.route('/restorant/meetguybrother/admin/dineIn', methods=['GET', 'POST'])
# def handle_admin_dine_in():
#     return dine_in_admin_page(request, render_template)


if __name__ == '__main__':
    app.run()
