dicts = [
    {'name': 'Michelangelo',
     'food': 'PIZZA'},
    {'name': 'Garfield',
     'food': 'lasanga'},
    {'name': 'Walter',
     'food': 'pancakes'},
    {'name': 'Galactus',
     'food': 'worlds'}
]

string = "Hi, I'm {name} and I love to eat {food}!"

new_list = []

def string_factory(dicts, string):
    for each_dict in dicts:
        new_string = string.format(**each_dict)
        new_list.append(new_string)
    return new_list
