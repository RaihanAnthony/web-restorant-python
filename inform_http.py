from flask import Flask, request

app = Flask(__name__)

@app.route('/example', methods=['POST'])
def example_route():
    # Mengakses JSON dari permintaan
    json_data = request.get_json()

    # Mengetahui URL permintaan
    request_url = request.url

    # Mengetahui metode HTTP permintaan
    request_method = request.method

    # Mengetahui informasi tambahan, misalnya header atau parameter
    request_headers = request.headers

    # Menampilkan informasi yang diakses
    print(f"JSON Data: {json_data}")
    print(f"Request URL: {request_url}")
    print(f"Request Method: {request_method}")
    print(f"Request Headers: {request_headers}")

    # Proses lebih lanjut atau respons sesuai kebutuhan
    return "OK"

if __name__ == '__main__':
    app.run(debug=True)
