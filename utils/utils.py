import json
import datetime


with open("../operations.json", "r", encoding="utf8") as file:
    operations = json.load(file)


def selection(list_op:list):
    sel_op = []
    for item in list_op:
        if not item:
            pass
        elif ('from' in item) and (item['state'] == 'EXECUTED'):
            sel_op.append(item)
    return sel_op


def print_last(list_op:list):
    for item in list_op[:5:]:
        date = datetime.datetime.strptime(item['date'], '%Y-%m-%dT%H:%M:%S.%f')
        print(f"{date.strftime("%d.%m.%Y")} {item['description']}\n"
              f"{disguise(item['from'])} -> {disguise(item['to'])}\n"
              f"{item['operationAmount']['amount']} {item['operationAmount']['currency']['name']}\n"
              )


def disguise(string_pay:str):
    string_pay = string_pay.split(' ')
    if string_pay[0] == 'Счет':
        return f"Счет **{string_pay[1][-4:]}"
    elif len(string_pay) == 2:
        return f"{string_pay[0]} {string_pay[1][:4]} {string_pay[1][4:6]}** **** {string_pay[1][-4:]}"
    else:
        return f"{string_pay[0]} {string_pay[1]} {string_pay[2][:4]} {string_pay[2][4:6]}** **** {string_pay[2][-4:]}"


