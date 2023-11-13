from main import home_page
from main import order_page
from main import  delivered_page
from main import addandbuy_page
from flask import Flask, request, render_template
# from main import fitur_food 
# from main import fitur_drink 
# from main import fitur_dessert

app = Flask(__name__, template_folder='view', static_folder='static')

@app.route('/', methods=['GET', 'POST'])
def handle_main():
    return home_page(request, render_template)

@app.route('/pesan', methods=['GET', 'POST'])
def handle_order():
    return order_page(request, render_template)

@app.route('/pesan/delivered', methods=['GET', 'POST'])
def handle_delivered():
    return delivered_page(request, render_template)

@app.route('/pesan/delivered/addandbuy', methods=['GET', 'POST'])
def handle_addandbuy():
    return addandbuy_page(request, render_template)

# @app.route('/makanan', methods=['GET', 'POST'])
# def handle_get_makanan():
#     return fitur_food(request, render_template)

# @app.route('/minuman', methods=['GET', 'POST'])
# def handle_get_minuman():
#     return fitur_drink(request, render_template)

# @app.route('/dessert', methods=['GET', 'POST'])
# def handle_get_dessert():
#     return fitur_dessert(request, render_template)


if __name__ == '__main__':
    app.run()
