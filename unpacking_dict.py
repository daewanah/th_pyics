my_string = "Hi! My name is {name} and I live in {state}."
my_string.format(name='Sholmergan', state='Palo Alto')
# >>> Hi! My name is Sholmergan and I live in Palo Alto.
my_string.format(state='Palo Alto', name='Sholmergan')
# >>> Hi! My name is Sholmergan and I live in Palo Alto.
my_dict = {'name': 'Sholmergan', 'state': 'Palo Alto'}
my_string.format(**my_dict)
# >>> Hi! My name is Sholmergan and I live in Palo Alto.
