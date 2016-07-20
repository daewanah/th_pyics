my_alphabet_list = list('abcdefghijklmnopqrstuvwxyz')
count = 0
for letter in my_alphabet_list:
    print('{}: {}'.format(count, letter))
    count += 1

# >>> 1: a
# >>> 2: b
# >>> ...
# >>> ...
# >>> 25: z

for index, letter in enumerate(my_alphabet_list):
    print('{}: {}'.format(index, letter))

# >>> 1: a
# >>> 2: b
# >>> ...
# >>> ...
# >>> 25: z

for step in enumerate(my_alphabet_list):
    print('{}: {}'.format(step[0], step[1]))

# >>> 1: a
# >>> 2: b
# >>> ...
# >>> ...
# >>> 25: z

my_dict = {'name': 'Sholmergan', 'career': 'Software Engineer', 'location': 'Mars'}
for key, value in my_dict.items():
    print('{}: {}'.format(key.title(), value))

# >>> Name: Sholmergan
# >>> Career: Software Engineer
# >>> Location: Mars
