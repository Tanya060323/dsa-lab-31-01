from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)


DB_CONFIG = {
    "dbname": "microservices_db",
    "user": "postgres",
    "password": "postgres",
    "host": "localhost",
    "port": "5432"
}


def get_connection():
    return psycopg2.connect(**DB_CONFIG)


@app.route('/convert', methods=['GET'])
def convert_currency():
    currency_name = request.args.get('currency_name')
    amount = request.args.get('amount')

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT rate
        FROM currencies
        WHERE currency_name = %s
        """,
        (currency_name,)
    )

    currency = cursor.fetchone()

    if not currency:
        cursor.close()
        connection.close()

        return jsonify({
            "message": "Валюта не найдена"
        }), 404

    rate = float(currency[0])

    converted = float(amount) * rate

    cursor.close()
    connection.close()

    return jsonify({
        "currency": currency_name,
        "amount": amount,
        "converted_value": converted
    }), 200


@app.route('/currencies', methods=['GET'])
def get_currencies():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT id, currency_name, rate FROM currencies"
    )

    currencies = cursor.fetchall()

    result = []

    for currency in currencies:
        result.append({
            "id": currency[0],
            "currency_name": currency[1],
            "rate": float(currency[2])
        })

    cursor.close()
    connection.close()

    return jsonify(result), 200


if __name__ == '__main__':
    app.run(port=5002, debug=True)