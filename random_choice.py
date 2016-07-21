my_list = list(range(50))
my_list
# >>> [0, 1, ....., 49]

import random

random.choice(my_list)
# >>> 15

random.choice(my_list)
# >>> 36

random.choice(my_list)
# >>> 43

random.choice([(0, 1), (2, 3), (3, 4)])
# >>> (0, 1)

random.choice({'a': True, 'b': False})
# >>> KeyErro: 0
