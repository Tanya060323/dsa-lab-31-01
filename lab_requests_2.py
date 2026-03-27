import requests
import random

url = "http://127.0.0.1:5000/number/"

# GET
param = random.randint(1, 10)
get_res = requests.get(url, params={"param": param}).json()

# POST
json_param = random.randint(1, 10)
post_res = requests.post(url, json={"jsonParam": json_param}).json()

# DELETE
delete_res = requests.delete(url).json()


def calc(a, b, op):
    if op == 'sum':
        return a + b
    elif op == 'sub':
        return a - b
    elif op == 'mul':
        return a * b
    elif op == 'div':
        return a / b if b != 0 else 0


print(f"GET: {{'number': {get_res['number']}, 'operation': '{get_res['operation']}'}}")
print(f"POST: {{'number': {post_res['number']}, 'operation': '{post_res['operation']}'}}")
print(f"DELETE: {{'number': {delete_res['number']}, 'operation': '{delete_res['operation']}'}}")


# Начинаем с результата GET запроса
result = get_res['number']

# Применяем операцию из POST запроса с числом из POST
result = calc(result, post_res['number'], post_res['operation'])

# Применяем операцию из DELETE запроса с числом из DELETE
result = calc(result, delete_res['number'], delete_res['operation'])


print("Итог:", int(result))

