import json

pizzas = []
with open('/home/lilia/PycharmProjects/bot_aio/smth/dishes.json') as f:
    pizzas = json.load(f)
    print(type(pizzas))
    print(pizzas)


def get_menu(n):
    menu = ''
    for pizza in pizzas[:n]:
        menu += pizza['name'] +' - ' + pizza['price'] +"р"+ '\n'
    return menu

print(type(get_menu(1)))

def get_pizzas_by_ingradients(ingredients:list):
    hits = dict() # pizza['name'] -> No of ingredients found
    for pizza in pizzas:
        for addon in ingredients:
            if addon[:3] in pizza['contents']:
                if pizza['name'] in hits.keys():
                    hits[pizza['name']] += 1
                else:
                    hits[pizza['name']] = 1
    return sorted(hits.items(), key=lambda x: x[1])[-1]

def get_pizza_price(name):
    name = name[6:]
    for pizza in pizzas:
        if pizza['name'] == name:
            return pizza['price']
    return None
