import random
from flask import Flask, request, jsonify

app = Flask(__name__)

operations = ['sum', 'sub', 'mul', 'div']


# Функция для выполнения операции
def calculate(a, b, operation):
    if operation == 'sum':
        return a + b
    elif operation == 'sub':
        return a - b
    elif operation == 'mul':
        return a * b
    elif operation == 'div':
        return a / b if b != 0 else 0


# Получает параметр param из URL и умножает его на случайное число
@app.route('/number/', methods=['GET'])
def get_number():
    # получаем параметр из строки запроса
    param = request.args.get('param')

    # проверяем, передан ли параметр
    if not param:
        return jsonify({"error": "Задайте значение param"}), 400

    # преобразуем в число
    param = int(param)

    # генерируем случайное число
    rand_num = random.randint(1, 100)

    # умножаем
    result = rand_num * param

    # возвращаем результат в формате JSON
    return jsonify({
        "number": result,
        "operation": "mul"
    })


# Принимает JSON с jsonParam и выполняет случайную операцию
@app.route('/number/', methods=['POST'])
def post_number():
    data = request.json

    if not data or 'jsonParam' not in data:
        return jsonify({"error": "Требуется параметр jsonParam"}), 400

    param = int(data['jsonParam'])

    rand_num = random.randint(1, 100)

    operation = random.choice(operations)

    result = calculate(rand_num, param, operation)

    return jsonify({
        "number": result,
        "operation": operation
    })


# Возвращает случайное число и случайную операцию
@app.route('/number/', methods=['DELETE'])
def delete_number():
    rand_num = random.randint(1, 100)

    operation = random.choice(operations)

    return jsonify({
        "number": rand_num,
        "operation": operation
    })


if __name__ == '__main__':
    app.run(debug=True)

    