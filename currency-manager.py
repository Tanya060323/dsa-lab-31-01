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


@app.route('/load', methods=['POST'])
def load_currency():
    data = request.json

    currency_name = data.get('currency_name')
    rate = data.get('rate')

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM currencies WHERE currency_name = %s",
        (currency_name,)
    )

    currency = cursor.fetchone()

    if currency:
        cursor.close()
        connection.close()

        return jsonify({
            "message": "Валюта уже существует"
        }), 400

    cursor.execute(
        """
        INSERT INTO currencies (currency_name, rate)
        VALUES (%s, %s)
        """,
        (currency_name, rate)
    )

    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({
        "message": "Валюта добавлена"
    }), 200


@app.route('/update_currency', methods=['POST'])
def update_currency():
    data = request.json

    currency_name = data.get('currency_name')
    rate = data.get('rate')

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM currencies WHERE currency_name = %s",
        (currency_name,)
    )

    currency = cursor.fetchone()

    if not currency:
        cursor.close()
        connection.close()

        return jsonify({
            "message": "Валюта не найдена"
        }), 404

    cursor.execute(
        """
        UPDATE currencies
        SET rate = %s
        WHERE currency_name = %s
        """,
        (rate, currency_name)
    )

    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({
        "message": "Валюта обновлена"
    }), 200


@app.route('/delete', methods=['POST'])
def delete_currency():
    data = request.json

    currency_name = data.get('currency_name')

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM currencies WHERE currency_name = %s",
        (currency_name,)
    )

    currency = cursor.fetchone()

    if not currency:
        cursor.close()
        connection.close()

        return jsonify({
            "message": "Валюта не найдена"
        }), 404

    cursor.execute(
        """
        DELETE FROM currencies
        WHERE currency_name = %s
        """,
        (currency_name,)
    )

    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({
        "message": "Валюта удалена"
    }), 200


if __name__ == '__main__':
    app.run(port=5001, debug=True)